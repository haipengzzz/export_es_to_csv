

datas = {
	'_index': 'winlogbeat-7.13.2-2023.06.04-000002',
	'_id': 'V5_OH4kBTlmfK5AWouJF',
	'_score': 4.216394e-06,
	'_source': {
		'@timestamp': '2023-07-04T07:29:40.228Z',
		'message': '已检查网络共享对象是否可以授予客户端所需的访问权限。\n\t\n使用者:\n\t安全 ID:\t\tS-1-5-21-1016609146-4195733450-292096815-1108\n\t帐户名:\t\tCNSHISE01$\n\t帐户域:\t\thftech01\n\t登录 ID:\t\t0xD4BD3638\n\n网络信息:\t\n\t对象类型:\t\tFile\n\t源地址:\t\t172.16.66.110\n\t源端口:\t\t61068\n\t\n共享信息:\n\t共享名称:\t\t\\\\*\\IPC$\n\t共享路径:\t\t\n\t相对目标名称:\tnetlogon\n\n访问请求信息:\n\t访问掩码:\t\t0x2019F\n\t访问:\t\tREAD_CONTROL\n\t\t\t\tReadData (或 ListDirectory)\n\t\t\t\tWriteData (或 AddFile)\n\t\t\t\tAppendData (或 AddSubdirectory 或 CreatePipeInstance)\n\t\t\t\tReadEA\n\t\t\t\tWriteEA\n\t\t\t\tReadAttributes\n\t\t\t\tWriteAttributes\n\t\t\t\t\n访问检查结果:\n\t-',
		'host': {
			'os': {
				'type': 'windows',
				'platform': 'windows',
				'version': '10.0',
				'family': 'windows',
				'name': 'Windows Server 2019 Standard',
				'kernel': '10.0.17763.4252 (WinBuild.160101.0800)',
				'build': '17763.4252'
			},
			'id': '27a99269-aca3-421d-b8c4-9e23121043a4',
			'ip': ['fe80::8d2c:867f:8db9:3671', '169.254.57.178', '172.16.66.17', 'fe80::3cdd:f84b:d3d9:82b0', '169.254.243.148'],
			'mac': ['00:09:0f:aa:00:01', '00:0c:29:5c:9b:a5', '00:09:0f:fe:00:01'],
			'hostname': 'CNSHAD01',
			'architecture': 'x86_64',
			'name': 'CNSHAD01.hftech.cc'
		},
		'winlog': {
			'channel': 'Security',
			'task': 'Detailed File Share',
			'api': 'wineventlog',
			'keywords': ['审核成功'],
			'opcode': '信息',
			'event_id': '5145',
			'event_data': {
				'ShareName': '\\\\*\\IPC$',
				'AccessList': '%%1538\n\t\t\t\t%%4416\n\t\t\t\t%%4417\n\t\t\t\t%%4418\n\t\t\t\t%%4419\n\t\t\t\t%%4420\n\t\t\t\t%%4423\n\t\t\t\t%%4424\n\t\t\t\t',
				'SubjectDomainName': 'hftech01',
				'IpPort': '61068',
				'SubjectUserSid': 'S-1-5-21-1016609146-4195733450-292096815-1108',
				'SubjectUserName': 'CNSHISE01$',
				'AccessMask': '0x2019f',
				'AccessReason': '-',
				'ObjectType': 'File',
				'SubjectLogonId': '0xd4bd3638',
				'IpAddress': '172.16.66.110',
				'RelativeTargetName': 'netlogon'
			},
			'record_id': 3337822,
			'process': {
				'pid': 4,
				'thread': {
					'id': 832
				}
			},
			'provider_guid': '{54849625-5478-4994-a5ba-3e3b0328c30d}',
			'computer_name': 'CNSHAD01.hftech.cc',
			'provider_name': 'Microsoft-Windows-Security-Auditing'
		},
		'event': {
			'outcome': 'success',
			'action': 'Detailed File Share',
			'created': '2023-07-04T07:29:41.938Z',
			'code': '5145',
			'kind': 'event',
			'provider': 'Microsoft-Windows-Security-Auditing'
		},
		'tags': ['172.16.66.17', 'windows'],
		'ecs': {
			'version': '1.9.0'
		},
		'agent': {
			'hostname': 'CNSHAD01',
			'ephemeral_id': '4e8fb121-0f10-48b7-aae3-e275c98dc7be',
			'id': '39496c28-1b5d-4d21-abde-84e46cdb8171',
			'name': 'winlogbeat',
			'type': 'winlogbeat',
			'version': '7.13.2'
		},
		'log': {
			'level': '信息'
		}
	}
}

print(datas['_source']['message'])
print(datas['_source']['host']['hostname'])
print(datas["_source"]["@timestamp"])