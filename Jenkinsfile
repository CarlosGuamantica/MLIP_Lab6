pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '''
                echo En Python no es necesario compilar.
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                echo Instalando dependencias y ejecutando pruebas desde entorno mlip...

                C:\\Users\\javi_\\Documents\\MLIP_Lab6\\mlip\\Scripts\\pip.exe install pytest numpy pandas scikit-learn

                C:\\Users\\javi_\\Documents\\MLIP_Lab6\\mlip\\Scripts\\python.exe -m pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                echo Etapa de despliegue simulada completada.
                '''
            }
        }
    }
}

