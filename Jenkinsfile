pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '''
                echo En Python, no es necesario compilar
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                echo Instalando dependencias y ejecutando pruebas...
                pip install pytest numpy pandas scikit-learn
                pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                echo Despliegue completado (simulado)
                '''
            }
        }
    }
}

