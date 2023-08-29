from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    #外部キー
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #カスケード：ユーザーが削除された時に同時にタスクも全て削除する
    #null=True ユーザーを持っていなくても大丈夫という意味あい
    #blank = True 空白でOK
    title = models.CharField(max_length=100)
    #CharField:文字列の情報を書き込むことができる

    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    #タスクが完了したかしていないかのチェックマーク
    createdDate = models.DateTimeField(auto_now_add=True)
    #タスクを完了した日にち auto_now_add:自動的に現在の時間を自動的に付け加える

#データベースを管理するパネルでユーザータイトルディスクリプションの名前を見やすくするための記述

    def __str__(self):
        return self.title
    
    class Meta:
        #順番を決めることができる
        ordering = ["completed"]