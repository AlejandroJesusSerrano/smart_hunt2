
POSTGRESQL = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'smartHunt2',
    'USER': 'postgres',

    #!EN CASA:
    # 'PASSWORD': 'tecnico'
    #!EN TRABAJO:
    'PASSWORD': 'Tecnico+123',

    'HOST': 'localhost',
    'PORT': '5432',
    'OPTIONS': {
      'client_encoding': 'UTF8',
    }
  }
}