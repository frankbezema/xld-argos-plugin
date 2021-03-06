#
# Copyright (C) 2019 - 2020 Rabobank Nederland
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

'''
Created on Oct 19, 2018

@author: borstg
'''
import com.xebialabs.deployit.community.argos.ArgosConfiguration as ArgosConfiguration
import com.xebialabs.deployit.community.argos.ArgosVerifier as ArgosVerifier

global params, thisCi, context, permissionService, metadataService, repositoryService

version = context.getRepository().read(thisCi.id);

if ArgosVerifier.versionIsValid(context, version):
    context.logOutput("This package has a valid Argos Notary Verification")
else:
    context.logError("This package has an invalid Argos Notary Verification")

