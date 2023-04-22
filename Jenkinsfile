pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch:'senpai'
                url:'https://gitlab.com/nekoill/keyvastopy.git'
            }
        }
        stage('Build') {
            steps {
            sh '''
            docker build -t keyvastopy:${BUILD_NUMBER}
            '''
            }
        }
        // stage('Test') {
            // steps {
            // sh '''
            // docker run -It keyvalstopy:${BUILD_NUMBER}
            // curl localhost:5000
            // '''
            // }
        // }
        // stage('Package') {
            // steps {
            // sh '''
            // docker push nekoill/keyvalstopy:${BUILD_NUMBER}
            // '''
            // }
        // }
        // stage('Deploy') {
            // steps {
            // sh '''
            // echo "TODO: \
            // - [ ] Add some sick deploy logic shit here BAEH-BEEE"
            // '''
            // }
        // }
    }
}
