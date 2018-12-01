Database used is SQLite with the following fields for different models:

#Advert
	operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default_business.jpg', upload_to='business_pics')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='advert',
            name='products',
            field=models.ManyToManyField(to='advert.Item'),
        ),
    ]

#Post
	operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('document', models.FileField(upload_to='tender_docs/')),
                ('description', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='tender_docs/')),
                ('comment', models.TextField()),
                ('user_name', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.Post')),
            ],
        ),
    ]

#Users
	operations = [
	    migrations.CreateModel(
	        name='UserProfile',
	        fields=[
	            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
	            ('image', models.ImageField(default='default_pic.jpg', upload_to='user_pics')),
	            ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
	        ],
	    ),
	]