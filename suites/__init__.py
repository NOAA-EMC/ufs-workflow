from solo.factory import Factory
from .ufs_forecast import UFSForecast

suite_factory = Factory.get_factory('SuiteFactory')
suite_factory.register('UFSForecast', UFSForecast)
