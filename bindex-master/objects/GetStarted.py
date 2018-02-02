from objects.Models import Funds

import json
import ast

fund = Funds()

class GetStarted:
    def __init__(self):
        pass

    def getPlanData(self, formData):
        length = len(formData)
        jsonForm = json.dumps(formData)

        ##convert str to dict
        dictJsonForm = ast.literal_eval(jsonForm)

        userRiskValue = 0

        for key, value in dictJsonForm.iteritems():
            try:
                if value[0] == '':
                    userRiskValue += 0
                else:
                    userRiskValue += int(value[0])
            except IndexError:
                userRiskValue += 0

        print userRiskValue

        if 18 > userRiskValue:
            #user is low risk
            print 'low'
            userFund = fund.query.filter(Funds.fund == 'low').all()
        elif 18 < userRiskValue < 36:
            #user is med risk
            print 'mid'
            userFund = fund.query.filter(Funds.fund == 'mid').all()
        elif 36 < userRiskValue:
            print 'high'
            #user is high risk
            userFund = fund.query.filter(Funds.fund == 'high').all()

        selectedFund = []
        for u in userFund:
            f = {}
            f['symbol'] = u.symbol
            f['percent'] = u.percent
            f['fund'] = u.fund
            f['description'] = u.description
            f['selection'] = u.selection
            selectedFund.append(f)


        return selectedFund
