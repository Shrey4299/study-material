search_pattern = "natural language processing"
pattern = preprocess(search_pattern)
words_pattern = pattern.replace(" ", "|")
complete_pattern = pattern.replace(" ", " & ")

# Phrase search in title
phrase_tsquery_filter = f"title @@ phraseto_tsquery('english', '{search_pattern}')"
phrase_tsquery = query_builder(ts_filter_str=phrase_tsquery_filter)

# Complete pattern search
all_ts_query_filter = f"""ts @@ to_tsquery('english', '"{complete_pattern}":*')"""
all_ts_query = query_builder(ts_filter_str=all_ts_query_filter)

# Words pattern search (prefix search)
prefix_tsquery_filter = f"""ts @@ to_tsquery('english', '"{words_pattern}":*')"""
prefix_tsquery = query_builder(ts_filter_str=prefix_tsquery_filter)

# Description search with words pattern
description_tsquery_filter = f"""dts @@ to_tsquery('english', '"{words_pattern}":*')"""
description_tsquery = query_builder(ts_filter_str=description_tsquery_filter)

# Additional LIKE and EQUAL filters
like_filter = "title LIKE '%processing%'"
equal_filter = "category = 'AI'"

# Combining all filters into a single query
final_query = f"""
SELECT * FROM my_table
WHERE ({phrase_tsquery_filter})
OR ({all_ts_query_filter})
OR ({prefix_tsquery_filter})
OR ({description_tsquery_filter})
OR ({like_filter})
OR ({equal_filter})
"""

print(final_query)
