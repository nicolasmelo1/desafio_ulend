from desafio_ulend.service import InvestmentService
import os

TOTAL_IN_EACH_BATCH_BY_LOAN = {
    147: [226000, 164000],
    148: [94000, 26000]
}
FILE_NAME = 'base_json.json'


def main():
    investment_service = InvestmentService(TOTAL_IN_EACH_BATCH_BY_LOAN, os.path.join(os.path.dirname(__file__), FILE_NAME))
    investment_service.run()
    

if __name__ == '__main__':
    main()
