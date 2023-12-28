import json
from datetime import datetime
from writer import XlsAnalyticPaymentWriter
from constants import *

if __name__ == '__main__':
    data_clients = json.load(CLIENTS)
    data_payments = json.load(PAYMENTS)
    data = {'clients': data_clients['clients'], 'payments': data_payments['payments']}

    output = XlsAnalyticPaymentWriter(data)
    output.write_excel_report(f'payments_analytics_{datetime.now().strftime("%Y-%m-%d")}.xlsx')
