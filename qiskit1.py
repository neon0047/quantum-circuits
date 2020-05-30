#!/usr/bin/env python
# coding: utf-8

# In[9]:


import qiskit as q
get_ipython().run_line_magic('matplotlib', 'inline')

circuit= q.QuantumCircuit(2,2)

circuit.x(0)

circuit.cx(0,1)
circuit.measure([0,1], [0,1])
circuit.draw()


# In[13]:


circuit.draw(output="mpl")


# In[22]:


from qiskit import IBMQ
IBMQ.save_account('f46e7329de9306c7e8e8123431956539b36e9b103e9df2ed99555cf2f7963e8acc0337b5d36cc2159268f1699fedb4322e8b4acce911448453a965fadf126c82')


# In[27]:


IBMQ.load_account()


# In[40]:


provider = IBMQ.get_provider('ibm-q')

for backend in provider.backends():
    try:
        qubit_count = len(backend.properties().qubits)
    except:
        qubit_count = 'simulated'
    print(f"{backend.name()} has {backend.status().pending_jobs} queued and {qubit_count} qubits")   
          


# In[39]:


from qiskit.tools.monitor import job_monitor
backend = provider.get_backend('ibmq_burlington')
job = q.execute(circuit, backend=backend,shots = 100)
job_monitor(job)


# In[45]:


from qiskit.visualization import plot_histogram
from matplotlib import style

style.use('dark_background')
result = job.result()
counts = result.get_counts(circuit)
plot_histogram([counts])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




