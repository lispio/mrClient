#!/bin/bash

#Script for create venv and install needed package

create_venv(){
    echo create venv
    python3 -m venv /opt/lispio/mrClient/mrClient_venv
    echo done
}

install_py_package()
{
  echo insall requirements package
  source /opt/lispio/mrClient/mrClient_venv/bin/activate
  pip install wheel
  pip install -r /opt/lispio/mrClient/requirements.txt
  deactivate
  echo done
}

create_venv
install_py_package
