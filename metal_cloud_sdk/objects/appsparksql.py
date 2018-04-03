# -*- coding: utf-8 -*-

class AppSparkSQL(object):
	"""
	An object which has instance labels as keys and
	<a:schema>AppSparkSQLInstance</a:schema> objects as values.
	"""

	def __init__(self, spark_master, spark_workers):
		self.spark_master = spark_master;
		self.spark_workers = spark_workers;


	"""
	The <a:schema>AppSparkSQLInstance</a:schema> object which represents the
	Master.
	"""
	spark_master = [];

	"""
	The <a:schema>AppSparkSQLInstance</a:schema> objects.
	"""
	spark_workers = [];

	"""
	The URL to access Spark Master.
	"""
	spark_master_url = None;

	"""
	The URL to access the Spark Master Web UI.
	"""
	spark_master_web_ui_url = None;

	"""
	The URL to access the Spark Thrift server.
	"""
	spark_thrift_url = None;

	"""
	The SparkSQL JDBC connection URL.
	"""
	sparksql_jdbc_connection_url = None;

	"""
	Cluster software available versions.
	"""
	container_cluster_software_available_versions = [];

	"""
	The software version detected on the container cluster.
	"""
	container_cluster_software_version = None;

	"""
	Array of compatible and connectable clusters.
	"""
	connectable_container_clusters = [];

	"""
	The schema type
	"""
	type = None;
