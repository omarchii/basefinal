--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: activities; Type: TABLE; Schema: public; Owner: app_user
--

CREATE TABLE public.activities (
    id integer NOT NULL,
    case_id integer NOT NULL,
    description character varying(200) NOT NULL,
    activity_date timestamp without time zone NOT NULL,
    created_at timestamp without time zone
);


ALTER TABLE public.activities OWNER TO app_user;

--
-- Name: activities_id_seq; Type: SEQUENCE; Schema: public; Owner: app_user
--

CREATE SEQUENCE public.activities_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.activities_id_seq OWNER TO app_user;

--
-- Name: activities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: app_user
--

ALTER SEQUENCE public.activities_id_seq OWNED BY public.activities.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: app_user
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO app_user;

--
-- Name: cases; Type: TABLE; Schema: public; Owner: app_user
--

CREATE TABLE public.cases (
    id integer NOT NULL,
    client_name character varying(100) NOT NULL,
    case_type character varying(50) NOT NULL,
    start_date date NOT NULL,
    end_date date,
    status character varying(50)
);


ALTER TABLE public.cases OWNER TO app_user;

--
-- Name: cases_id_seq; Type: SEQUENCE; Schema: public; Owner: app_user
--

CREATE SEQUENCE public.cases_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.cases_id_seq OWNER TO app_user;

--
-- Name: cases_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: app_user
--

ALTER SEQUENCE public.cases_id_seq OWNED BY public.cases.id;


--
-- Name: clients; Type: TABLE; Schema: public; Owner: app_user
--

CREATE TABLE public.clients (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    phone character varying(20),
    address character varying(255)
);


ALTER TABLE public.clients OWNER TO app_user;

--
-- Name: clients_id_seq; Type: SEQUENCE; Schema: public; Owner: app_user
--

CREATE SEQUENCE public.clients_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.clients_id_seq OWNER TO app_user;

--
-- Name: clients_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: app_user
--

ALTER SEQUENCE public.clients_id_seq OWNED BY public.clients.id;


--
-- Name: activities id; Type: DEFAULT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.activities ALTER COLUMN id SET DEFAULT nextval('public.activities_id_seq'::regclass);


--
-- Name: cases id; Type: DEFAULT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.cases ALTER COLUMN id SET DEFAULT nextval('public.cases_id_seq'::regclass);


--
-- Name: clients id; Type: DEFAULT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.clients ALTER COLUMN id SET DEFAULT nextval('public.clients_id_seq'::regclass);


--
-- Data for Name: activities; Type: TABLE DATA; Schema: public; Owner: app_user
--

COPY public.activities (id, case_id, description, activity_date, created_at) FROM stdin;
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: app_user
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Data for Name: cases; Type: TABLE DATA; Schema: public; Owner: app_user
--

COPY public.cases (id, client_name, case_type, start_date, end_date, status) FROM stdin;
1	Mauricio Cifuentes	Divorcio	2024-12-08	\N	\N
2	Clark Kent	Civil	2024-12-10	\N	\N
4	Bruce Wayne	Destruccion	2024-12-10	\N	\N
3	Peter Parker	Boda	2024-12-10	\N	\N
\.


--
-- Data for Name: clients; Type: TABLE DATA; Schema: public; Owner: app_user
--

COPY public.clients (id, name, email, phone, address) FROM stdin;
1	Omar Chi	example@mail.com	123456789	Merida
5	Miles Morales	example@mail4.com	123456784	Brooklin
3	Peter Parker	example@mail2.com	987654321	New York
4	Bruce Wayne	example@mail3.com	123456784335	Gothica
\.


--
-- Name: activities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: app_user
--

SELECT pg_catalog.setval('public.activities_id_seq', 1, false);


--
-- Name: cases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: app_user
--

SELECT pg_catalog.setval('public.cases_id_seq', 4, true);


--
-- Name: clients_id_seq; Type: SEQUENCE SET; Schema: public; Owner: app_user
--

SELECT pg_catalog.setval('public.clients_id_seq', 5, true);


--
-- Name: activities activities_pkey; Type: CONSTRAINT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.activities
    ADD CONSTRAINT activities_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: cases cases_pkey; Type: CONSTRAINT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.cases
    ADD CONSTRAINT cases_pkey PRIMARY KEY (id);


--
-- Name: clients clients_email_key; Type: CONSTRAINT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_email_key UNIQUE (email);


--
-- Name: clients clients_pkey; Type: CONSTRAINT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_pkey PRIMARY KEY (id);


--
-- Name: activities activities_case_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: app_user
--

ALTER TABLE ONLY public.activities
    ADD CONSTRAINT activities_case_id_fkey FOREIGN KEY (case_id) REFERENCES public.cases(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

GRANT USAGE ON SCHEMA public TO admin;


--
-- Name: TABLE activities; Type: ACL; Schema: public; Owner: app_user
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.activities TO admin;


--
-- Name: TABLE cases; Type: ACL; Schema: public; Owner: app_user
--

GRANT SELECT,INSERT,DELETE,UPDATE ON TABLE public.cases TO admin;


--
-- PostgreSQL database dump complete
--

