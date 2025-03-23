-- Create index idx_name_first_score
-- on name table
CREATE INDEX idx_first_score ON names (name(1), score);
