# -*- coding: utf-8 -*-

class InfrastructureDeployOverview(object):
	"""
	Important infrastructure changes which need to be reviewed before a deploy.
	"""

	def __init__(self):
		pass;


	"""
	Unused reservations across all owned infrastructures.
	"""
	unusedServerTypeReservations = [];

	"""
	Licenses which are created, reassigned or unused.
	"""
	licenses = [];

	"""
	Infrastructure elements such as <a:schema>SharedDrive</a:schema> or
	<a:schema>Drive</a:schema> which will be shrinked, stopped or deleted.
	"""
	dataLoss = [];

	"""
	Infrastructure elements which are swapping, allocating or deallocating
	servers, allocating or expanding disk space, etc.
	"""
	resourceChanges = [];

	"""
	LAN networks that have no InstanceArrays attached to them.
	"""
	unusedLANNetworks = [];

	"""
	Infrastructure elements with changed subdomains.
	"""
	subdomainChanges = [];

	"""
	If this is true, at the end of the deploy, all the servers on the
	infrastructure will be powered on.
	"""
	willAllServersPowerOnAtDeployEnd = None;

	"""
	The schema type
	"""
	type = None;
