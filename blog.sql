--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- Name: bank_users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bank_users (
    user_id integer NOT NULL,
    username text NOT NULL,
    email text,
    password text NOT NULL,
    account_number integer NOT NULL,
    routing_number integer NOT NULL,
    balance integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.bank_users OWNER TO postgres;

--
-- Name: bank_users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bank_users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bank_users_user_id_seq OWNER TO postgres;

--
-- Name: bank_users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bank_users_user_id_seq OWNED BY public.bank_users.user_id;


--
-- Name: bank_users user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bank_users ALTER COLUMN user_id SET DEFAULT nextval('public.bank_users_user_id_seq'::regclass);


--
-- Data for Name: bank_users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bank_users (user_id, username, email, password, account_number, routing_number, balance) FROM stdin;
37	alex91617	alex91617@yahoo.com	123456789	84445520	869544707	0
40	man1234	man7@yahoo.com	d671fa701db60f4430b632dda770e3395004dafe15241ddf7bf8526257ef3750d98bfbadf12a8c7b07a032272574433841452a67a3eb69977163f5521fde2e4e	46192305	576004498	0
41	man12341	man73@yahoo.com	ebba7e88f1df8ae6635d3c7e67c9fe94690e64de67dcc7f8b891ca1e85d8c82e7c62db69704b0cad496810ca5ed17bb67ee1afc2818075f7c6f39cfa97550cb2	15967085	302077125	0
42	man123411	man731@yahoo.com	a520f642cc0bca4c01117c933244a6795fdb45d48f76d4a3260add8a38bb82d0371c5109cbaf9f292c517603e971d7b17e985394f9cd93caf7abf3ee846b8a87	41508645	760970462	0
\.


--
-- Name: bank_users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bank_users_user_id_seq', 42, true);


--
-- Name: bank_users bank_users_account_number_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bank_users
    ADD CONSTRAINT bank_users_account_number_key UNIQUE (account_number);


--
-- Name: bank_users bank_users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bank_users
    ADD CONSTRAINT bank_users_email_key UNIQUE (email);


--
-- Name: bank_users bank_users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bank_users
    ADD CONSTRAINT bank_users_pkey PRIMARY KEY (user_id);


--
-- Name: bank_users bank_users_routing_number_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bank_users
    ADD CONSTRAINT bank_users_routing_number_key UNIQUE (routing_number);


--
-- Name: bank_users bank_users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bank_users
    ADD CONSTRAINT bank_users_username_key UNIQUE (username);


--
-- PostgreSQL database dump complete
--

