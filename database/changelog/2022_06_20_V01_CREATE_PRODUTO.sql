create table if not exists produto (
    id serial unique not null primary key,
    sku varchar(20) unique not null,
    descricao varchar(256) not null,
    estoque numeric(6) not null default 0,
    valor numeric(10, 2) not null default 0,
    tier char(1) not null,
    ativo boolean not null default false
)