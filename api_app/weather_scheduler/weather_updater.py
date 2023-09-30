from apscheduler.schedulers.background import BackgroundScheduler
from api_app.views import ForecastViewset

def start():
  scheduler = BackgroundScheduler()
  weather = ForecastViewset()

  scheduler.add_job(weather.save_data, 'interval', minutes=2, id='weather_001', replace_existing=True)
  scheduler.start()
