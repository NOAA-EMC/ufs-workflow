from ewok.suite import Suite


class UFSForecast:

    @staticmethod
    def build():
        with Suite() as suite:
            with suite.add('setup') as setup:
                create = setup.add('CreateExperiment')
                stage = setup.add('Stage', create)
            start = 'config.init_cycle'
            stop = 'config.last_cycle'
            step = 'config.step_cycle'
            with suite.add('fcCycle', start=start, stop=stop, step=step) as cycle:
                analysis = cycle.add('GetAnalysis')
                prep = cycle.add('PrepareRun', stage, analysis)
                fc = cycle.add('Forecast', setup, analysis, prep)
                archive = cycle.add('SaveForecast', fc)
                cycle.add('CleanCycles', archive, )
            suite.add('FinishExperiment', cycle, defstatus='suspended')
        return suite
