# Serializers

## Serializers

```ruby
# app/serializers/user_serializer.rb
class UserSerializer
  def initialize(user)
    @user = user
  end

  def to_json
    {
      id: @user.id,
      email: @user.email,
      first_name: @user.first_name,
      last_name: @user.last_name,
      full_name: @user.full_name,
      role: @user.role,
      is_active: @user.is_active,
      created_at: @user.created_at.iso8601,
      updated_at: @user.updated_at.iso8601
    }
  end
end

# In controller
def show
  render json: UserSerializer.new(@user).to_json
end
```
