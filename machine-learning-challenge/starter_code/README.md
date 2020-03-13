# Exoplanet Hunting 

## Model 1 - GradientBoostingClassifier
### without GridSearchCV
#### Training Data Score:    0.9252336448598131
#### Testing Data Score:    0.8901601830663616

### with GridSearchCV 
#### Best Parameters: 
##### {'learning_rate': 0.1, 'max_depth': 5, 'min_samples_split': 0.1, 'n_estimators': 100, 'n_iter_no_change': 20, 'random_state': 29}
#### Best Training Data Score:    0.9046361856802918
#### Best Testing Data Score:    0.8981693363844394

## Model 2 - AdaBoostClassifier
### without GridSearchCV
#### Training Data Score:    0.7638756437154302
#### Testing Data Score:    0.7574370709382151

### with GridSearchCV 
#### Best Parameters:
##### {'algorithm': 'SAMME', 'learning_rate': 1.0, 'n_estimators': 100, 'random_state': 29}
#### Best Training Data Score:    0.8889951535086122
#### Best Testing Data Score:    0.881578947368421

### My Thoughts
My models use all of the data given in the dataset and with further examination I could probably drop some columns. 
My first model didn't improve very much when GridSearch was run. 

My second model improved to a very similar level. Even though it had a larger improvement it did not do better than Model 1.
90% accuracy is really good for a start but if I were to be happy with a model it would have to have a 97% or better accuracy! 
