#!/usr/bin/env python
# coding: utf-8

# ### <center><h2> Ingeniería en Biotecnología </h2></center>
# # <center><h1 style="color:pink">GBI6 - BIOINFORMÁTICA</h1></center>
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Logotipo_Ikiam.png/1200px-Logotipo_Ikiam.png" width=400 height=300/>
# 
# # <center><h1 style="color:turquoise"> Tarea de traducción</h1></center>
# 
# # <center><h1 style="color:purple"> Sofía Cristina Barros Hurtado </h1></center>
# 

# In[8]:


seq ="AAGGACCNGACATCCATCGCTGATGTCAATCCCCCGTGGATCGTAAGTCCGGGAGTAGGAGGAGGAAGGGTCGTCCCACAGTGCGAAGAGGCTTCTGACCTACTGACGGTACCTCCTCAGTGTCAGCCTATAGTCGGAGCTCGAGGGAGACTCGGTCCTCTGTAAAAGTCCGAATACCTTTGATGAAGGAGGTCTTCTATAGGACGGTAG"
print(seq) 
#Secuencia


# In[12]:


#Secuencia sin n
seq2 = seq.replace("N","")#con este comando eliminamos N
print(seq2)


# In[14]:


#Sacamos la cadedena complementaria
seq3 = seq2.replace ("A", "U") #con esto reemplazamos A por U  dado que la timina se sustituye por uracilo en el arn 
seq4 = seq3.replace ("T","a") #con esto reemplazamos T por a
seq5 = seq4.replace ("C","g") #con esto reemplazamos C por g
seq6 = seq5.replace ("G","c") #con esto reemplazamos G por c
cseq = seq6.upper() #Para transformar en mayusculas la secuencia
print(cseq) #para imprimir


# In[6]:


rseq = cseq [::-1] #para obtener el inverso complementario
print(rseq)


# In[7]:


dna_show1= seq2.replace ("ATC","star") #para marcar como codon de inicio
dna_seq = dna_show1.replace ("TAG","stop") #marcar a TAG por codon final
print(dna_seq)


# In[11]:


dna_show2= cseq.replace ("ATC","star") #para marcar como codon de inicio
dna_cseq= dna_show2.replace ("TAG","stop") #marcar a TAG por codon final
print(dna_cseq)


# In[12]:


dna_show3= rseq.replace ("ATC","star") #para marcar como codon de inicio
dna_rseq= dna_show3.replace ("TAG","stop") #marcar a TAG por codon final
print(dna_rseq)


# In[ ]:


rnam_show3= rseq.replace("AUG","star") #Marcamos al AUG como star, sera el codon de inicio en la secuencia
rnam_seq1= rnam_show3.replace("UAA","stop") #se marca al UAA como stOP como codon de fin en nuestra secuencia
rnam_seq2= rnam_show3.replace("UAG","stop") #marca al UAG como stOP para como codon de fin en la secuencia
rnam_seq3= rnam_show3.replace("UGA","stop") #marcar al UGA como stOP como codon de final en la secuencia

