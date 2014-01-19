"""
Some models need manual intervention:
53869 -- press enter after the h.restart
"""

"""
Skipped for now: Traub et al 2005
"""

"""
Next model to setup: AP initiation and propagation in type II cochlear ganglion cell (Hossain et al 2005)
"""
protocol = {
    '32992':
        {
            'compile': ['cd synchro-ca1', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr synchro-ca1']
        },
    '135839':
        {
            'compile': ['cd McCormickEtAl2007YuEtAl2008', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.soma_inj()'],
            'cleanup': ['cd ..', 'rm -fr McCormickEtAl2007YuEtAl2008']
        },
    '145836':
        {
            'compile': ['cd MoradiEtAl2012', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr MoradiEtAl2012']
        },
    '124063':
        {
            'compile': ['cd PublioEtAl2009', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.start()'],
            'cleanup': ['cd ..', 'rm -fr PublioEtAl2009']
        },
    '126637_2c':
        {
            'variant': 'Fig 2C + 2E',
            'compile': ['cd purkinje_ppr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit_spine and spine neck at spinydendrite133.hoc")'],
            'cleanup': ['cd ..', 'rm -fr purkinje_ppr']
        },
    '126637_2d':
        {
            'variant': 'Fig 2D + 2F',
            'compile': ['cd purkinje_ppr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit_reduced_PPR model.hoc")'],
            'cleanup': ['cd ..', 'rm -fr purkinje_ppr']
        },
    '126637_cvode':
        {
            'variant': 'CVODE or other solvers',
            'compile': ['cd purkinje_ppr', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit_reduced_PPR model_cvode.hoc")'],
            'cleanup': ['cd ..', 'rm -fr purkinje_ppr']
        },
    '146026_ex1':
        {
            'variant': 'Example 1',
            'compile': ['cd BahlEtAl2012', 'nrnivmodl channels/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("example1.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr BahlEtAl2012']
        },
    '146026_ex2':
        {
            'variant': 'Example 2',
            'compile': ['cd BahlEtAl2012', 'nrnivmodl channels/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("example2.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr BahlEtAl2012']
        },
    '146026_ex3':
        {
            'variant': 'Example 3',
            'compile': ['cd BahlEtAl2012', 'nrnivmodl channels/'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("example3.hoc")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr BahlEtAl2012']
        },
    '137259':
        {
            'compile': ['cd ca3-synresp', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr ca3-synresp']
        },
    '53869':
        {
            'compile': ['cd MSO_Zhouetal_2005', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("MSO_Zhouetal_2005")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr MSO_Zhouetal_2005']
        },
    '125857_2frb':
        {
            'variant': '2FRB',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("2FRB")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '140249_a1':
        {
            'variant': 'Fig 4 A1',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.runP1MP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },
    '140249_b1':
        {
            'variant': 'Fig 4 B1',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.runP1HP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },
    '140249_a2':
        {
            'variant': 'Fig 4 A2',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.runP2MP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },
    '140249_b2':
        {
            'variant': 'Fig 4 B2',
            'compile': ['cd dLGN_modelDB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.runP2HP()', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr dLGN_modelDB']
        },        
    '125857_frb3':
        {
            'variant': 'FRB3',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("FRB3")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '125857_frb_12_19':
        {
            'variant': 'FRB_12_19',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("FRB_12_19")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '125857_frb_12_21':
        {
            'variant': 'FRB_12_21',
            'compile': ['cd FRB', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")', 'h.restart("FRB_12_21")', 'h.run()'],
            'cleanup': ['cd ..', 'rm -fr FRB']
        },
    '150240':
        {
            'compile': ['cd TCconvergenceModel', 'nrnivmodl'],
            'launch': ['nrngui -python'],
            'run': ['from neuron import h', 'h.load_file("mosinit.hoc")'],
            'cleanup': ['cd ..', 'rm -fr TCconvergenceModel']
        }
}
