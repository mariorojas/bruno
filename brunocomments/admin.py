from django.contrib import admin

from .models import Comment

SHORT_COMMENT_LENGTH = 50


class CommentAdmin(admin.ModelAdmin):
    list_display = ['short_comment', 'author', 'created_at']
    ordering = ['-created_at']

    @admin.display(description='Comment')
    def short_comment(self, obj):
        comment = obj.comment[:SHORT_COMMENT_LENGTH]
        extra = '...' if len(obj.comment) > SHORT_COMMENT_LENGTH else ''
        return f'{comment}{extra}'


admin.site.register(Comment, CommentAdmin)
