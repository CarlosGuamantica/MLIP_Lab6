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
                echo Ejecutando pruebas con pytest...
                C:\\Users\\javi_\\miniconda3\\Scripts\\activate.bat mlip && pytest
                '''
            }
        }
        stage('Deploy') {
            steps {
                bat '''
                echo Paso de despliegue: nada que hacer aquí
                '''
            }
        }
    }
}
