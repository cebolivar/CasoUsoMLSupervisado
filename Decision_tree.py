from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

def decision_tree():
    # Datos de ejemplo
    X = np.array([[25, 5000, 1], [40, 10000, 0], [30, 7000, 1], [50, 15000, 0]])
    y = np.array([1, 0, 1, 0])  # 1: Compra, 0: No compra
    
    modelo = DecisionTreeClassifier()
    modelo.fit(X, y)

    # Datos de prueba (Ejemplo: [1, 0, 1])
    datos_cliente = np.array([[30, 6000, 1]])  # Edad: 30, Ingreso: 6000, Ubicación: 1
    prediccion = modelo.predict(datos_cliente)[0]

    datos = {'edad': 30, 'ingreso': 6000, 'ubicacion': 1}
