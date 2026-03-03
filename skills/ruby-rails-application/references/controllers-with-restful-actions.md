# Controllers with RESTful Actions

## Controllers with RESTful Actions

```ruby
# app/controllers/api/v1/users_controller.rb
module Api
  module V1
    class UsersController < ApplicationController
      before_action :authenticate_request, except: [:create]
      before_action :set_user, only: [:show, :update, :destroy]
      before_action :authorize_user!, only: [:update, :destroy]

      def index
        users = User.all
        users = users.where("email ILIKE ?", "%#{params[:q]}%") if params[:q].present?
        users = users.page(params[:page]).per(params[:limit] || 20)

        render json: {
          data: users,
          pagination: pagination_data(users)
        }
      end

      def show
        render json: @user
      end

      def create
        user = User.new(user_params)

        if user.save
          token = encode_token(user.id)
          render json: {
            user: user,
            token: token
          }, status: :created
        else
          render json: { errors: user.errors.full_messages }, status: :unprocessable_entity
        end
      end

      def update
        if @user.update(user_params)
          render json: @user
        else
          render json: { errors: @user.errors.full_messages }, status: :unprocessable_entity
        end
      end

      def destroy
        @user.destroy
        head :no_content
      end

      private

      def set_user
        @user = User.find(params[:id])
      rescue ActiveRecord::RecordNotFound
        render json: { error: 'User not found' }, status: :not_found
      end

      def authorize_user!
        unless current_user.id == @user.id || current_user.admin?
          render json: { error: 'Unauthorized' }, status: :forbidden
        end
      end

      def user_params
        params.require(:user).permit(:email, :password, :first_name, :last_name)
      end

      def pagination_data(collection)
        {
          page: collection.current_page,
          per_page: collection.limit_value,
          total: collection.total_count,
          total_pages: collection.total_pages
        }
      end
    end
  end
end

# app/controllers/api/v1/posts_controller.rb
module Api
  module V1
    class PostsController < ApplicationController
      before_action :authenticate_request, except: [:index, :show]
      before_action :set_post, only: [:show, :update, :destroy, :publish]
      before_action :authorize_post_owner!, only: [:update, :destroy, :publish]

      def index
        posts = Post.published.recent
        posts = posts.by_author(params[:author_id]) if params[:author_id].present?
        posts = posts.where("title ILIKE ?", "%#{params[:q]}%") if params[:q].present?
        posts = posts.page(params[:page]).per(params[:limit] || 20)

        render json: {
          data: posts,
          pagination: pagination_data(posts)
        }
      end

      def show
        if @post.published? || current_user&.id == @post.user_id
          render json: @post
        else
          render json: { error: 'Post not found' }, status: :not_found
        end
      end

      def create
        @post = current_user.posts.build(post_params)

        if @post.save
          render json: @post, status: :created
        else
          render json: { errors: @post.errors.full_messages }, status: :unprocessable_entity
        end
      end

      def update
        if @post.update(post_params)
          render json: @post
        else
          render json: { errors: @post.errors.full_messages }, status: :unprocessable_entity
        end
      end

      def destroy
        @post.destroy
        head :no_content
      end

      def publish
        @post.publish!
        render json: @post
      end

      private

      def set_post
        @post = Post.find(params[:id])
      rescue ActiveRecord::RecordNotFound
        render json: { error: 'Post not found' }, status: :not_found
      end

      def authorize_post_owner!
        unless current_user.id == @post.user_id || current_user.admin?
          render json: { error: 'Unauthorized' }, status: :forbidden
        end
      end

      def post_params
        params.require(:post).permit(:title, :content, :status)
      end

      def pagination_data(collection)
        {
          page: collection.current_page,
          per_page: collection.limit_value,
          total: collection.total_count
        }
      end
    end
  end
end
```
