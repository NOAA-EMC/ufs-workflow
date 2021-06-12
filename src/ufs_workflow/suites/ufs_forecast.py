from ewok.suite import Suite


class UFSForecast:

    @staticmethod
    def build():
        with Suite(exec_class='copy') as suite:
            with suite.add('setup') as setup:
                create = setup.add('CreateExperiment')
                stage = setup.add('Stage', create)
            start = 'config.init_cycle'
            stop = 'config.last_cycle'
            step = 'config.step_cycle'
            with suite.add('fcCycle', start=start, stop=stop, step=step) as cycle:
                prep = cycle.add('PrepareRun', stage)
                analysis = cycle.add('GetUFSAnalysis', prep)
                fc = cycle.add('Forecast', setup, analysis, exec_class='executable', exec='forecast')
                archive = cycle.add('SaveForecast', fc, exec_class='r2d2')
                cycle.add('CleanCycles', archive, exec_class='copy')
            suite.add('FinishExperiment', cycle, defstatus='suspended')
        return suite
