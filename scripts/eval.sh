cp models/$2/*gold_test$1 ./results/best_gold_test_$2.dag
cp models/$2/*pred_test$1 ./results/best_pred_test_$2.dag

cp models/$2/*gold_test_two$1 ./results/best_gold_test2_$2.dag
cp models/$2/*pred_test_two$1 ./results/best_pred_test2_$2.dag


python ./scripts/deconvert.py ./results/best_gold_test_$2.dag ./results/best_gold_test_$2.conll2009
python ./scripts/deconvert.py ./results/best_pred_test_$2.dag ./results/best_pred_test_$2.conll2009

python ./scripts/deconvert.py ./results/best_gold_test2_$2.dag ./results/best_gold_test2_$2.conll2009
python ./scripts/deconvert.py ./results/best_pred_test2_$2.dag ./results/best_pred_test2_$2.conll2009

echo 'TEST ID'
./scripts/eval09.pl -q -g ./results/best_gold_test_$2.conll2009 -s ./results/best_pred_test_$2.conll2009 | tail -n 28 | head -n 11 

echo 'TEST OOD' 
./scripts/eval09.pl -q -g ./results/best_gold_test2_$2.conll2009 -s ./results/best_pred_test2_$2.conll2009  | tail -n 28 | head -n 11 

