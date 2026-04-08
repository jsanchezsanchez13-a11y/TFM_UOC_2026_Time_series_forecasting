import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, explained_variance_score

def train_by_cluster(
    train, val, test,
    features,
    target_col='udsVenta_reconstruida',
    cluster_col='cluster',
    model_fn=None,
    verbose=True
):
    """
    Entrena un modelo por cluster y devuelve resultados y modelos.

    Parámetros:
    ----------
    model_fn : función que devuelve un modelo (ej: lambda: RandomForestRegressor(...))
    """

    results = []
    models = {}

    for c in train[cluster_col].unique():

        if verbose:
            print(f"\n🔹 Cluster {c}")

        train_c = train[train[cluster_col] == c]
        val_c = val[val[cluster_col] == c]
        test_c = test[test[cluster_col] == c]

        X_train = train_c[features]
        y_train = train_c[target_col]

        X_val = val_c[features]
        y_val = val_c[target_col]

        X_test = test_c[features]
        y_test = test_c[target_col]

        # Crear modelo
        model = model_fn()

        # Entrenar
        model.fit(X_train, y_train)
        models[c] = model

        # Predicciones
        val_pred = model.predict(X_val)
        test_pred = model.predict(X_test)

        # Métricas
        val_mae = mean_absolute_error(y_val, val_pred)
        test_mae = mean_absolute_error(y_test, test_pred)

        val_rmse = np.sqrt(mean_squared_error(y_val, val_pred))
        test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))

        val_exp_var = explained_variance_score(y_val, val_pred)
        test_exp_var = explained_variance_score(y_test, test_pred)

        if verbose:
            print(f"Val MAE: {val_mae:.4f} | RMSE: {val_rmse:.4f} | ExpVar: {val_exp_var:.4f}")
            print(f"Test MAE: {test_mae:.4f} | RMSE: {test_rmse:.4f} | ExpVar: {test_exp_var:.4f}")

        results.append((
            c,
            val_mae, val_rmse, val_exp_var,
            test_mae, test_rmse, test_exp_var
        ))

    return results, models