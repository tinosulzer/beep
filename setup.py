from setuptools import setup, find_packages

setup(name="beep_ep",
      packages=find_packages(),
      install_requires=["numpy>1.16.0",
                        "monty>=2.0.6",
                        "scipy>=1.2.0",
                        "scikit-learn==0.20.3",
                        "pandas>=0.24.1",
                        "cerberus>=1.2",
                        "tqdm>=4.30.0",
                        "boto3>=1.9.117",
                        "botocore>=1.12.117",
                        "pytz>=2018.9",
                        "watchtower>=0.5.5",
                        "psycopg2==2.7.7",
                        "docopt>=0.6.2",
                        "msgpack-python>=0.5.6",
                        "python-dateutil==2.8.0",
                        "ruamel.yaml==0.16.5",
                        "xmltodict>=0.12.0",
                        "tables==3.6.1"
                        ],
      extras_require={
          "tests": ["nose",
                    "coverage",
                    "pylint",
                    "memory_profiler",
                    "matplotlib"]
      },
      entry_points={
          "console_scripts": [
              "collate = beep_ep.collate:main",
              "validate = beep_ep.validate:main",
              "structure = beep_ep.structure:main",
              "featurize = beep_ep.featurize:main",
              "run_model = beep_ep.run_model:main",
              "generate_protocol = beep_ep.generate_protocol:main"
          ]
      })
