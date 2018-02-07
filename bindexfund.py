from flask import Flask, flash, render_template, request, jsonify, redirect, make_response, session, redirect, url_for
from jinja2 import Template
import time

#from objects.WebScrapers import WebScrapers
#from objects.MarketData import MarketData
#from objects.MarketTrade import MarketTrade
'''from objects.Utilities import Utilities
from objects.Database import db_session
from objects.Mailer import Mailer
from objects.Slack import Slack
from objects.GetStarted import GetStarted

scrape = WebScrapers()
marketdata = MarketData()
util = Utilities()
markettrade = MarketTrade()
mailer = Mailer()
slack = Slack()
getstarted = GetStarted()
'''

'''
if util.getMode() == 'live':
    ##run CRON script
    import objects.cron
'''

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.secret_key = 'asdasdaasd'

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/about')
def aboutPage():
    return render_template('about.html')

@app.route('/services')
def servicesPage():
    return render_template('services.html')

@app.route('/funds')
def fundsPage():
    return render_template('funds.html')

@app.route('/security')
def securityPage():
    return render_template('security.html')

@app.route('/get-started')
def getStartedPage():
    return render_template('get-started.html')

@app.route('/get-plan')
def getPlanPage():
    try:
        formData = session['riskForm']
        planData = getstarted.getPlanData(formData)
        return render_template('get-plan.html', planData=planData)
    except:
        return redirect('/get-started', 302)


@app.route('/form/get-started/risk-submission', methods=['POST'])
def getStartedRiskSubmission():
    #run query and do the number crunching
    time.sleep(2)
    ####

    session['riskForm'] = request.form.to_dict()

    return 'success'
'''
@app.route('/api/v1/get-calculation', methods=['GET'])
def getCalculation():
    amount = request.args.get('amount', default=1, type=int)

    response = marketdata.getCalculation(amount)

    return str(response)
'''

'''
@app.route('/api/v1/get-historical-data', methods=['GET'])
def getHistoricalData():
    search = request.args.get('search', default='BTC,XRP,ETH', type=str)
    time = request.args.get('time', default='15552000', type=int)

    items = [x.strip().upper() for x in search.split(',')]

    historicalData = marketdata.historicalData(time, items)

    return jsonify(historicalData)

'''

@app.route('/api/v1/get-bindex-data', methods=['GET'])
def getBindexData():
    # search = request.args.get('search', default='BTC,XRP,ETH', type=str)
    return 'test'

'''
@app.route('/api/v1/get-top-three')
def getTopThree():
    return jsonify(scrape.recentThreeItems())

@app.route('/api/v1/get-coins')
def getCoinsAPI():
    # coin = request.args.get('coin', default='btc', type=str)
    result = scrape.getCoinPrice()

    return jsonify(result)
'''


@app.template_filter('format_currency')
def format_currency(value):
    value = float(value)
    return "${:,.2f}".format(value)

'''
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
'''


'''
if util.getMode() == 'live':
    @app.errorhandler(Exception)
    def exception_handler(error):
        mailer.sendError(repr(error))
        # slack.notify("500 error " + str(repr(error)))
        return "Error! Please email 'ethan (at) bindexfund (dot) com'"
'''

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=5003)
