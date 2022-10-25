## Installation de l'environnement Docker

Cette installation est recommandée si votre machine n'est pas compatible avec les versions les plus récentes de Python (>= 3.9)

Voici les instructions à suivre:

- Installez Docker: <https://docs.docker.com/get-docker/>
- !! Si vous travaillez sur Windows:
    - assurez-vous d'abord que les system requirements sont respectés (ils sont indiqués sur la page)
    - Téléchargez et installez le [Linux kernel update package](https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package) 
    - Redémarrez votre machine et lancez Docker
- Démarrez le programme Docker
- Ouvrez un terminal et exécutez les commandes suivantes:

```bash
git clone git@github.com:madewild/tac.git
cd tac
docker-compose build
docker-compose up
```

Vous pourrez ouvrir et exécuter les notebooks en utilisant Jupyterlab à l'adresse suivante: <http://localhost:8888/lab>

A parir de maintenant, vous ne devrez plus utiliser le terminal pour lancer Docker. Il vous suffira d'utiliser les bouton `play` et le bouton `stop` dans l'interface Docker pour lancer ou arrêter le container du projet.