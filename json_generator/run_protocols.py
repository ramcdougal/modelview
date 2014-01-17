protocol = {
    '32992':
        {
            'compile': ['cd synchro-ca1', 'nrnivmodl'],
            'launch': ['nrngui -python mosinit.hoc'],
            'run': ['from neuron import h', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr synchro-ca1']
        }
}
