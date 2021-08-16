from ewok.suite import Suite
from ewok.iterators import Iterator


class UFSForecast:

    @staticmethod
    def build():
        with Suite() as suite:
            with suite.add('setup') as setup:
                create = setup.add('CreateExperiment')
                stage = setup.add('Stage', create,
                                  loop_type='parallel', loop_var='MODEL', iterator=Iterator('Models'))
                stage.add('Stage')
            start = 'config.init_cycle'
            stop = 'config.last_cycle'
            step = 'config.step_cycle'
            with suite.add('fcCycle', loop_type='serial',
                           loop_var='DATE', iterator=Iterator('Date', start, stop, step)) as cycle:
                cycle.add('StartCycle')
                with cycle.add('Models', loop_type='parallel',
                               loop_var='MODEL', iterator=Iterator('Models')) as models:
                    analysis = models.add('GetAnalysis')
                    prep = models.add('PrepareModel', stage, analysis)
                    #fc = models.add('Forecast', setup, analysis, analysis)
                    #archive = models.add('SaveForecast', fc)
                cycle.add('EndCycle', models)
                cycle.add('CleanCycles', models)
            finish = suite.add('FinishExperiment', cycle, defstatus='suspended')
            suite.add('CleanupExperiment', finish, defstatus='suspended')
        return suite
