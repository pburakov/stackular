from flask_restful import fields
from sqlalchemy.exc import IntegrityError
from db import session
import datetime

tag_output_fields = {
    'tag': fields.String,
    'created': fields.DateTime,
    'modified': fields.DateTime,
    'synonyms': fields.Raw,
    'places': fields.Raw,
    'image': fields.String,
    'meta': fields.Raw,
}

place_output_fields = {
    'id': fields.Integer,
    'created': fields.DateTime,
    'modified': fields.DateTime,
    'type': fields.String,
    'name': fields.String,
    'lat': fields.Float,
    'lon': fields.Float,
    'address': fields.String,
    'image': fields.String,
    'tags': fields.Raw,
    'description': fields.String,
    'meta': fields.Raw,
}


class Controller:
    def __init__(self, model):
        self.model = model

    def create(self, **args):
        args['created'] = datetime.datetime.utcnow()
        error_message = None
        try:
            new_model = self.model(**args)
            session.add(new_model)
            session.commit()
            self.model = new_model
        except IntegrityError as e:
            print(str(e))
            error_message = 'Faulty or a duplicate record'
        except Exception as e:
            print(str(e))
            error_message = str(e)
        finally:
            if error_message:
                session.rollback()
                raise Exception(error_message)
        return self.model

    def read(self, id):
        self.model = session.query(self.model).filter(self.model.id == id).first()
        return self.model

    def update(self, **args):
        error_message = None
        try:
            model = self.model
            for key, value in args.items():
                setattr(property, key, value)
            session.merge(model)
            session.commit()
            self.model = model
        except IntegrityError as e:
            print(str(e))
            error_message = 'Faulty or a duplicate record'
        except Exception as e:
            print(str(e))
            error_message = str(e)
        finally:
            if error_message:
                session.rollback()
                raise Exception(error_message)
        return self.model


class Place(Controller):
    pass


class Tag(Controller):
    pass
