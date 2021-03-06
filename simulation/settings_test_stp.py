"""Settings to test STP dynamics.

1) Enforces all the HVA neurons to be identical (all clones
   of the default PY cells)

2) Recovery of D,F is infinite so that we can see:
    * Geometric decay for Depression
    * Linear increase for facilitation

3) Feedforward weights of the V1 afferents onto the HVA neurons
   3 different values so that we can ensure the weights are correct
     * the P1 amplitude should be equal to this weight.

4) Dynamics of STP are different across the HVA neurons to check to make
   sure things are correct.

5) Decay of synaptic conductance is instantaneous so that there is no summation
   and the only dynamics of the EPSCs is due to STP (D,F, d,f)

"""

from equations import neuron_eqs, synapse_eqs, onspike_eqs, sinusoid_rate


settings = {
    "neurons": {
        "HVA_PY": {
            "N": 1,
            "eqs": neuron_eqs,
            "tau_m": 0.030,
            "tau_e": 0.002,
            "tau_i": 0.010,
            "thresh": -0.044,
            "reset": -0.050,
            "V_rest": -0.075,
            "refract": 0.0015
        },
        "FS": {
            "N": 1,
            "eqs": neuron_eqs,
            "tau_m": 0.030,
            "tau_e": 0.002,
            "tau_i": 0.010,
            "thresh": -0.044,
            "reset": -0.050,
            "V_rest": -0.075,
            "refract": 0.0015
        },
        "SOM": {
            "N": 1,
            "eqs": neuron_eqs,
            "tau_m": 0.030,
            "tau_e": 0.002,
            "tau_i": 0.010,
            "thresh": -0.044,
            "reset": -0.050,
            "V_rest": -0.075,
            "refract": 0.0015
        }
    },

    "afferents": {
        "N": 1,
        "use_poisson": False,
        "modulation_rate": None,
        "peak_rate": None,
        "spikes_per_second": [1, 10, 50, 100],  # pulse train frequencies
        "eqs": sinusoid_rate,
        "sim_time": 2
    },

    "synapses": {
        ("afferents", "HVA_PY"): {
            "eqs": synapse_eqs,
            "on_spike": onspike_eqs,
            "p_connect": 1,
            "d1": 0.8,
            "d2": 1,
            "f1": 0,
            "f2": 0,
            "tau_D1": 1000,
            "tau_D2": 1000,
            "tau_F1": 1000,
            "tau_F2": 1000,
            "w_e": 10,
            "w_i": 0,
            "delay": 0
        },

        ("afferents", "FS"): {
            "eqs": synapse_eqs,
            "on_spike": onspike_eqs,
            "p_connect": 1,
            "d1": 0.5,
            "d2": 1,
            "f1": 0,
            "f2": 0,
            "tau_D1": 1000,
            "tau_D2": 1000,
            "tau_F1": 1000,
            "tau_F2": 1000,
            "w_e": 5,
            "w_i": 0,
            "delay": 0
        },

        ("afferents", "SOM"): {
            "eqs": synapse_eqs,
            "on_spike": onspike_eqs,
            "p_connect": 1,
            "d1": 1,
            "d2": 1,
            "f1": 2,
            "f2": 0,
            "tau_D1": 100,
            "tau_D2": 100,
            "tau_F1": 100,
            "tau_F2": 100,
            "w_e": 1,
            "w_i": 0,
            "delay": 0
        }
    },

    "monitors": {
        "HVA_PY": 'V Ge_total Gi_total',
        "FS": 'V Ge_total Gi_total',
        "SOM": 'V Ge_total Gi_total',
        "afferents": 'spikes'
    }
}
