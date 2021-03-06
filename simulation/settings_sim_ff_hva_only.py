"""Settings for feedforward Network.

These settings are for a network of FF excitation only. No interneurons.

Parameters for plasticity were drawn from Charlie's data (4/2017)

"""

from equations import neuron_eqs, synapse_eqs, onspike_eqs, sinusoid_rate


settings = {
    "neurons": {
        "MED_PY": {
            "N": 1,
            "eqs": neuron_eqs,
            "tau_m": 0.020,
            "tau_e": 0.002,
            "tau_i": 0.010,
            "thresh": -0.040,
            "reset": -0.044,
            "V_rest": -0.075,
            "refract": 0.0015
        },
        "LAT_PY": {
            "N": 1,
            "eqs": neuron_eqs,
            "tau_m": 0.020,
            "tau_e": 0.002,
            "tau_i": 0.010,
            "thresh": -0.040,
            "reset": -0.044,
            "V_rest": -0.075,
            "refract": 0.0015
        },
        "HVA_PV": {
            "N": 3,  # set to 100 for full model
            "eqs": neuron_eqs,
            "tau_m": 0.010,
            "tau_e": 0.002,
            "tau_i": 0.010,
            "thresh": -0.040,
            "reset": -0.042,
            "V_rest": -0.070,
            "refract": 0.005
        },
        "HVA_SOM": {
            "N": 3,  # set to 100 for full model
            "eqs": neuron_eqs,
            "tau_m": 0.010,
            "tau_e": 0.002,
            "tau_i": 0.010,
            "thresh": -0.040,
            "reset": -0.042,
            "V_rest": -0.070,
            "refract": 0.005
        },
    },

    "afferents": {
        "N": 2000,
        "use_poisson": True,
        "modulation_rate": [0, 0.5, 1, 2, 4, 8, 16, 32],  # [0, 0.5, 1, 2, 4, 8, 16, 32],
        "peak_rate": 20,
        "eqs": sinusoid_rate,
        "spikes_per_second": None,
        "sim_time": 3
    },

    "synapses": {
        ("afferents", "MED_PY"): {
            "eqs": synapse_eqs,
            "on_spike": onspike_eqs,
            "p_connect": 0.50,
            "d1": 0.8,
            "d2": 1,
            "f1": 0,
            "f2": 0,
            "tau_D1": 0.100,
            "tau_D2": 1,
            "tau_F1": 1,
            "tau_F2": 1,
            "w_e": 0.050,
            "w_i": 0,
            "delay": 0.002
        },

        ("afferents", "LAT_PY"): {
            "eqs": synapse_eqs,
            "on_spike": onspike_eqs,
            "p_connect": 0.50,
            "d1": 0.80,
            "d2": 1,
            "f1": 0,
            "f2": 0,
            "tau_D1": 0.100,
            "tau_D2": 1,
            "tau_F1": 1,
            "tau_F2": 1,
            "w_e": 0.050,
            "w_i": 0,
            "delay": 0.002
        },

        ("afferents", "HVA_PV"): {
            "eqs": synapse_eqs,
            "on_spike": onspike_eqs,
            "p_connect": 1,
            "d1": 0.7,
            "d2": 1,
            "f1": 0,
            "f2": 0,
            "tau_D1": 0.250,
            "tau_D2": 1,
            "tau_F1": 1,
            "tau_F2": 1,
            "w_e": 0.025,
            "w_i": 0,
            "delay": 0.002
        },

        ("afferents", "HVA_SOM"): {
            "eqs": synapse_eqs,
            "on_spike": onspike_eqs,
            "p_connect": 1,
            "d1": 1,
            "d2": 1,
            "f1": 0.5,
            "f2": 0,
            "tau_D1": 0.250,
            "tau_D2": 1,
            "tau_F1": 1,
            "tau_F2": 1,
            "w_e": 0.005,
            "w_i": 0,
            "delay": 0.002
        },

        ("HVA_PV", "LAT_PY"): {
            "eqs": synapse_eqs,
            "on_spike": onspike_eqs,
            "p_connect": 1,  # set to 40% for real model
            "d1": 1,
            "d2": 1,
            "f1": 0,
            "f2": 0,
            "tau_D1": 0.250,
            "tau_D2": 1,
            "tau_F1": 1,
            "tau_F2": 1,
            "w_e": 0,
            "w_i": 0.100,
            "delay": 0.002
        },

        ("HVA_SOM", "MED_PY"): {
            "eqs": synapse_eqs,
            "on_spike": onspike_eqs,
            "p_connect": 1,  # set to 40% for real model
            "d1": 1,
            "d2": 1,
            "f1": 0,
            "f2": 0,
            "tau_D1": 0.250,
            "tau_D2": 1,
            "tau_F1": 1,
            "tau_F2": 1,
            "w_e": 0,
            "w_i": 0.100,
            "delay": 0.002
        },
    },

    "monitors": {
        "MED_PY": 'V Ge_total Gi_total spikes',
        "LAT_PY": 'V Ge_total Gi_total spikes',
        "HVA_PV": 'V Ge_total spikes',
        "HVA_SOM": 'V Ge_total spikes',
        "afferents": 'spikes'
    }
}


# add connections b/w INs and PY cells. Make Pconnect higher for som->med
# to reflect the higher number of SOM cells. Possibly make the
# SOM->PYmed weights stronger than the SOM->PVlat weights to reflect
# the lower number of INs in medial areas to begin with.
#
# also update the synaptic params to reflect AM vs. LM
