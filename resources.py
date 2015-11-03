from db import session
from controllers import place_output_fields
from controllers import tag_output_fields
from controllers import Place as PlaceController
from controllers import Tag as TagController
from models import Place as PlaceModel
from models import Tag as TagModel
from flask_restful import abort
from flask_restful import reqparse
from flask_restful import Resource
from flask_restful import marshal_with

parser = reqparse.RequestParser()


class Places(Resource):
    @marshal_with(place_output_fields)
    def get(self):
        return session.query(PlaceModel).all()

    @marshal_with(place_output_fields)
    def post(self):
        try:
            new_place = PlaceController(PlaceModel)
            parser.add_argument('name', type=str, trim=True, required=True)
            parser.add_argument('lat', type=float, required=True)
            parser.add_argument('lon', type=float, required=True)
            parser.add_argument('address', type=str, required=True, trim=True)
            parser.add_argument('image', type=str, trim=True)
            parser.add_argument('description', type=str, trim=True)
            parsed_args = parser.parse_args()
            new_place.create(**parsed_args)
            return new_place.model, 201
        except Exception as e:
            abort(400, message=str(e))


class Tags(Resource):
    @marshal_with(tag_output_fields)
    def get(self):
        return session.query(TagModel).all()

    @marshal_with(tag_output_fields)
    def post(self):
        try:
            new_tag = TagController(TagModel)
            parser.add_argument('tag', type=str, trim=True, required=True)
            parser.add_argument('synonyms', type=str, action='append')
            parser.add_argument('image', type=str, trim=True)
            parsed_args = parser.parse_args()
            new_tag.create(**parsed_args)
            return new_tag.model, 201
        except Exception as e:
            abort(400, message=str(e))
