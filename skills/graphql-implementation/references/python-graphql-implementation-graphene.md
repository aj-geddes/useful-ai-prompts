# Python GraphQL Implementation (Graphene)

## Python GraphQL Implementation (Graphene)

```python
import graphene
from datetime import datetime
from typing import List

class UserType(graphene.ObjectType):
    id = graphene.ID(required=True)
    email = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    posts = graphene.List(lambda: PostType)

class PostType(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    content = graphene.String(required=True)
    author = graphene.Field(UserType)
    created_at = graphene.DateTime(required=True)

class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.ID(required=True))
    users = graphene.List(UserType)
    posts = graphene.List(PostType, author_id=graphene.ID())

    def resolve_user(self, info, id):
        return User.objects.get(pk=id)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_posts(self, info, author_id=None):
        if author_id:
            return Post.objects.filter(author_id=author_id)
        return Post.objects.all()

class CreateUserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    user = graphene.Field(UserType)
    success = graphene.Boolean()

    def mutate(self, info, email, first_name, last_name):
        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        return CreateUserMutation(user=user, success=True)

class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
```
