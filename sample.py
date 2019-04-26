import clipboard

str = """
	uv_projections::time_type as time_type,
	uv_projections::time_id as time_id,
	uv_projections::tsv_window as tsv_window,
	(int)'$TDP_LOCATION' as location_id,
	(int)'$TOTAL_BREAK' as break_id,
	uv_projections::person_id as person_id,
	uv_projections::web_id as web_id,
	uv_projections::level_id as level_id,
	uv_projections::genderage as genderage,
	uv_projections::stratum_language as stratum_language,
	uv_projections::presence_of_children as presence_of_children,
	uv_projections::hh_size as hh_size,
	uv_projections::stratum_income as stratum_income,
	uv_projections::base_weight as base_weight,
	uv_projections::minutes_tdp as minutes_raw,
	uv_projections::videos_tdp as videos_raw,
	uv_projections::streams_tdp as streams_raw,
	uv_projections::uv_projection_weight as visitors_proj,
	uv_projections::projected_videos_tdp as videos_proj,
	uv_projections::projected_minutes_tdp as minutes_proj,
	uv_projections::projected_streams_tdp as streams_proj
"""
l = str.split(',\n')
l1 = map(lambda x: x.split(' as ')[1], l)
# print('\n,'.join(l1))

clipboard.copy('\n,'.join(l1))
