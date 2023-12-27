DROP TABLE IF EXISTS email_verify;


CREATE TABLE email_verify (
  email VARCHAR(255) PRIMARY KEY NOT NULL,
  verify_code VARCHAR(255) UNIQUE NOT NULL,
  generate_time DateTime NOT NULL
);



