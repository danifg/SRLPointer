# SRLPointer
This repository includes the code of the transition-based SRL model described in the paper [Transition-based Semantic Role Labeling with Pointer Networks](https://arxiv.org/pdf/2205.10023.pdf). The implementation is based on the SDP parser by Fernández-González and Gómez-Rodríguez (2020) (https://github.com/danifg/SemanticPointer) and reuses part of its code.

### Requirements
This implementation requires Python 2.7, PyTorch 0.3.1 and Gensim >= 0.12.0.
  

### Experiments
First of all, you need to include official CoNLL-2009 datasets in the ``data`` folder, and use the following script to convert them to the proper input format. For instance, for the CoNLL-2009 English dataset:

     python ./scripts/convert.py ./data/en_train.conll09 ./data/en_train.dag
     python ./scripts/convert.py ./data/en_dev.conll09 ./data/en_dev.dag
     python ./scripts/convert.py ./data/en_id_test.conll09 ./data/en_id_test.dag
     python ./scripts/convert.py ./data/en_ood_test.conll09 ./data/en_ood_test.dag

Please note that for the Czech dataset you must use the script ``convertCZ.py`` instead, since the predicate sense annotation of Czech is simply the lemmatized token of the predicate and, therefore, the conversion process is different.

To train the model, you need to include the pre-trained word embeddings in the ``embs`` folder and run the following script (indicating the model name):

    ./scripts/run.sh <model_name>

The script ``run.sh`` is configured for the English dataset, please modify it accordingly to train the model for other CoNLL-2009 languages. 

Finally, to evaluate the best checkpoint on the in-domain and out-of-domain test sets with the oficial script just run (indicating the epoch of the best checkpoint on the development set and the model name):

    ./scripts/eval.sh <best_epoch> <model_name>
    
Please note that for the Czech dataset you must use the script ``evalCZ.py`` instead.


### Citation

	@article{FERNANDEZGONZALEZ2022110127,
	title = {Transition-based semantic role labeling with pointer networks},
	journal = {Knowledge-Based Systems},
	volume = {260},
	pages = {110127},
	year = {2023},
	issn = {0950-7051},
	doi = {https://doi.org/10.1016/j.knosys.2022.110127},
	url = {https://www.sciencedirect.com/science/article/pii/S0950705122012230},
	author = {Daniel Fernández-González},
	keywords = {Natural language processing, Computational linguistics, Semantic role labeling, Neural network, Deep learning},
	abstract = {Semantic role labeling (SRL) focuses on recognizing the predicate-argument structure of a sentence and plays a critical role in many natural language processing tasks such as machine translation and question answering. Practically all available methods do not perform full SRL, since they rely on pre-identified predicates, and most of them follow a pipeline strategy, using specific models for undertaking one or several SRL subtasks. In addition, previous approaches have a strong dependence on syntactic information to achieve state-of-the-art performance, despite being syntactic trees equally hard to produce. These simplifications and requirements make the majority of SRL systems impractical for real-world applications. In this article, we propose the first transition-based SRL approach that is capable of completely processing an input sentence in a single left-to-right pass, with neither leveraging syntactic information nor resorting to additional modules. Thanks to our implementation based on Pointer Networks, full SRL can be accurately and efficiently done in O(n2), achieving the best performance to date on the majority of languages from the CoNLL-2009 shared task.}
	}
    
### Acknowledgments
We acknowledge the European Research Council (ERC), which has funded this research under the European Union’s Horizon 2020 research and innovation programme (FASTPARSE, grant agreement No 714150), ERDF/MICINN-AEI (ANSWER-ASAP, TIN2017-85160-C2-1-R; SCANNER-UDC, PID2020-113230RB-C21), Xunta de Galicia (ED431C 2020/11), and Centro de Investigaci\'on de Galicia ``CITIC'', funded by Xunta de Galicia and the European Union (ERDF - Galicia 2014-2020 Program), by grant ED431G 2019/01. 

### Contact
If you have any suggestion, inquiry or bug to report, please contact d.fgonzalez@udc.es.
