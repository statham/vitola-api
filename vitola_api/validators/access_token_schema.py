from marshmallow import Schema, fields


class AccessTokenSchema(Schema):
    access_token = fields.String(required=True)
    token_type = fields.String(required=True)
    expires_in = fields.Integer(required=True)
