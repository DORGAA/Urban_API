from flask import Flask
import logging
app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s '
                                                                       f'%(name)s %(threadName)s : %(message)s')


@app.route('/records')
def records():
    app.logger.info('Info level log')
    app.logger.warning('warning level log')
    app.logger.error('error lever log')
    return f'welcome'


def logger(message):
    app.logger.info(message)


if __name__ == "__main__":
    app.run()