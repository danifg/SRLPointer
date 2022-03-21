# SRLPointer
This repository includes the code of the transition-based SRL model described in the paper [Transition-based Semantic Role Labeling with Pointer Networks](URL). The implementation is based on the SDP parser by Fernández-González and Gómez-Rodríguez (2020) (https://github.com/danifg/SemanticPointer) and reuses part of its code.

### Requirements
This implementation requires Python 2.7, PyTorch 0.3.1 and Gensim >= 0.12.0.
  

### Experiments
First of all, you need to include official CoNLL-2009 datasets in the ``data`` folder, and use the following script to convert them to the proper input format. For instance, for the CoNLL-2009 English dataset:

     python ./scripts/convert.py ./data/en_train.conll09 ./data/en_train.dag
     python ./scripts/convert.py ./data/en_dev.conll09 ./data/en_dev.dag
     python ./scripts/convert.py ./data/en_id_test.conll09 ./data/en_id_test.dag
     python ./scripts/convert.py ./data/en_ood_test.conll09 ./data/en_ood_test.dag

Please note that for the Czech dataset you must use the script ``convertCZ.py`` instead, since the predicate sense annotation of Czech is simply the lemmatized token of the predicate and, therefore, the conversion process is different.

To train the model, you need to include the pre-trained word embeddings in the ``embs`` folder and run the following script, indicating the model name:

    ./scripts/run.sh <model_name>


Finally, to evaluate the best checkpoint on the in-domain and out-of-domain test sets with the oficial script just run (indicating the epoch of the best reported checkpoint on the development set and the model name):

    ./scripts/eval.sh <best_epoch> <model_name>
    
Please note that for the Czech dataset you must use the script ``evalCZ.py`` instead.


### Citation

	@inproceedings{ACTUALIZARfernandez-gonzalez-gomez-rodriguez-2020-transition,
    title = "Transition-based Semantic Dependency Parsing with Pointer Networks",
    author = "Fern{\'a}ndez-Gonz{\'a}lez, Daniel  and
      G{\'o}mez-Rodr{\'\i}guez, Carlos",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.629",
    pages = "7035--7046"}
    
### Acknowledgments
We acknowledge the European Research Council (ERC), which has funded this research under the European Union’s Horizon 2020 research and innovation programme (FASTPARSE, grant agreement No 714150), ERDF/MICINN-AEI (ANSWER-ASAP, TIN2017-85160-C2-1-R; SCANNER-UDC, PID2020-113230RB-C21), Xunta de Galicia (ED431C 2020/11), and Centro de Investigaci\'on de Galicia ``CITIC'', funded by Xunta de Galicia and the European Union (ERDF - Galicia 2014-2020 Program), by grant ED431G 2019/01. 

### Contact
If you have any suggestion, inquiry or bug to report, please contact d.fgonzalez@udc.es.