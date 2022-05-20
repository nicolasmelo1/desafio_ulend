from .types import TypeInvestment

import json
from dataclasses import dataclass, field


class InvestmentServiceException(Exception):
    pass


@dataclass
class BatchByLoanData:
    total: float=0
    investments: list[str]=field(default_factory=list)
    
    
class InvestmentService:
    def __init__(self, total_batches_by_loan: dict, file_name: str):
        self.file_name = file_name
        self.total_batches_by_loan = total_batches_by_loan
        
    def __open_file_and_load_data(self):
        with open(self.file_name, 'r') as file:
            self.investments_data: list[TypeInvestment] = json.loads(file.read())
        
    def __is_valid_investment(self, investment: TypeInvestment):
        is_status_different_from_status2 = investment.get('status', None) != 2
        is_loan_number_in_desired_totals = investment['loan'] in self.total_batches_by_loan
        return is_status_different_from_status2 and is_loan_number_in_desired_totals

    def __get_total_investments_data(self):
        is_investments_data_not_defined = not hasattr(self, 'investments_data')
        if is_investments_data_not_defined:
            raise InvestmentServiceException('You should call `.__open_file_and_load_data()` before calling `.__get_total_investments_data()`')
        
        self.total_and_investments_by_loan_and_batch = {}
        batch_index_by_loan = {}

        for investment in self.investments_data:
            if self.__is_valid_investment(investment):
                
                investment_uuid: str = investment.get('uuid', None)
                loan_number: int = investment.get('loan', None)
                amount: float = float(investment.get('amount', 0))
                
                was_the_index_not_defined_for_this_loan: bool = loan_number not in batch_index_by_loan
                if was_the_index_not_defined_for_this_loan:
                    batch_index_by_loan[loan_number] = 0
                
                batch_index_to_consider: int = batch_index_by_loan[loan_number]
                total_of_loan_and_batch: float = self.total_and_investments_by_loan_and_batch\
                    .get(loan_number, dict())\
                    .get(batch_index_to_consider, BatchByLoanData())\
                    .total
                
                can_batch_be_filled: bool = self.total_batches_by_loan[loan_number][batch_index_to_consider] > total_of_loan_and_batch
                if can_batch_be_filled:
                    does_not_exist_loan_in_total_and_investments_by_loan_and_batch: bool = loan_number not in self.total_and_investments_by_loan_and_batch
                    if does_not_exist_loan_in_total_and_investments_by_loan_and_batch:
                        self.total_and_investments_by_loan_and_batch[loan_number] = dict()
                        
                    does_not_exist_batch_index_in_total_and_investments_by_loan_and_batch: bool = batch_index_to_consider not in \
                        self.total_and_investments_by_loan_and_batch[loan_number]
                    if does_not_exist_batch_index_in_total_and_investments_by_loan_and_batch:
                        self.total_and_investments_by_loan_and_batch[loan_number][batch_index_to_consider] = BatchByLoanData()
                    
                    self.total_and_investments_by_loan_and_batch[loan_number][batch_index_to_consider].total = total_of_loan_and_batch + amount
                    self.total_and_investments_by_loan_and_batch[loan_number][batch_index_to_consider].investments.append(investment_uuid)
                
                was_batch_filled: bool = self.total_and_investments_by_loan_and_batch[loan_number][batch_index_to_consider].total >= \
                    self.total_batches_by_loan[loan_number][batch_index_to_consider]
                if was_batch_filled:
                    batch_index_by_loan[loan_number] += 1
    
    def __print_investments(self):
        is_total_and_investments_by_loan_not_defined = not hasattr(self, 'total_and_investments_by_loan_and_batch')
        if is_total_and_investments_by_loan_not_defined:
            raise InvestmentServiceException('You should call `.__get_total_investments_data()` before calling `.__print_investments()`')
        
        lean_number: int
        batch_index_and_investments: dict
        for lean_number, batch_index_and_investments in self.total_and_investments_by_loan_and_batch.items():
            print('---')
            print(f'Empréstimo {lean_number}')
            
            batch_index: int
            batch_data: BatchByLoanData
            for batch_index, batch_data in batch_index_and_investments.items():
                formated_total_as_string = '{:.2f}'.format(round(batch_data.total, 2)).replace('.', ',')
                print(f'Lote {batch_index + 1} R$ {formated_total_as_string}')
                for investment_uuid in batch_data.investments:
                    print(f'Investimento {investment_uuid}')
                
            print('---')
            
            
    def run(self):
        self.__open_file_and_load_data()
        self.__get_total_investments_data()
        self.__print_investments()
