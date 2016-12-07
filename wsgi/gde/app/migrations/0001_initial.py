# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('descricao', models.TextField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(null=True, max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(null=True, max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EspecieDocumental',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(null=True, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(null=True, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormaDocumental',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(null=True, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(null=True, max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(null=True, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestricaoAcesso',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('descricao', models.CharField(null=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(null=True, max_length=20)),
                ('sigla', models.CharField(null=True, max_length=20)),
                ('funcao', models.CharField(null=True, max_length=250)),
                ('historico', models.CharField(null=True, blank=True, max_length=250)),
                ('campus', models.ForeignKey(verbose_name='Campus', null=True, to='app.Campus')),
            ],
        ),
        migrations.CreateModel(
            name='Suporte',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(null=True, max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipologia',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('finalidade', models.TextField(null=True, unique=True)),
                ('nome', models.CharField(null=True, max_length=50, unique=True)),
                ('identificacao', models.CharField(null=True, max_length=50, unique=True)),
                ('inicioAcumulo', models.IntegerField(default=2016, choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)])),
                ('fimAcumulo', models.IntegerField(default=2016, choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)])),
                ('quantidadeAcumulada', models.CharField(null=True, max_length=50, unique=True)),
                ('embasamentoLegal', models.CharField(null=True, max_length=50, unique=True)),
                ('producaoSetor', models.BooleanField(default=True, choices=[(True, 'Produzido neste setor'), (False, 'Recebido por este setor')])),
                ('anexo', models.ManyToManyField(to='app.Opcao', related_name='anexo')),
                ('atividade', models.ForeignKey(related_name='atividade', null=True, to='app.Atividade')),
                ('elemento', models.ManyToManyField(to='app.Elemento', related_name='elemento')),
                ('especieDocumental', models.ForeignKey(related_name='especieDocumental', null=True, to='app.EspecieDocumental')),
                ('fases', models.ManyToManyField(to='app.Fase')),
                ('formaDocumental', models.ForeignKey(related_name='formaDocumental', null=True, to='app.FormaDocumental')),
                ('genero', models.ManyToManyField(to='app.Genero', related_name='genero')),
                ('informacaoOutrosDocumentos', models.ManyToManyField(to='app.Opcao', related_name='informacaoOutrosDocumentos')),
                ('relacaoExterna', models.ManyToManyField(to='app.Opcao', related_name='relacaoExterna')),
                ('relacaoInterna', models.ManyToManyField(to='app.Opcao', related_name='relacaoInterna')),
                ('restricaoAcesso', models.ManyToManyField(to='app.RestricaoAcesso', related_name='restricaoAcesso')),
                ('riscoPerda', models.ManyToManyField(to='app.Opcao', related_name='riscoPerda')),
                ('setor', models.ForeignKey(related_name='setor', null=True, to='app.Setor')),
                ('suporte', models.ForeignKey(related_name='suporte', null=True, to='app.Suporte')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('setor', models.ForeignKey(verbose_name='Setor', null=True, to='app.Setor')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tipologia',
            name='usuario',
            field=models.ForeignKey(related_name='usuario', null=True, to='app.Usuario'),
        ),
        migrations.AddField(
            model_name='atividade',
            name='setor',
            field=models.ForeignKey(null=True, to='app.Setor'),
        ),
    ]
