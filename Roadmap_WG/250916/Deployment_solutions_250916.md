# MoM - Deployment solutions 16/09/2025
**Eclipse Arrowhead and ColonyOS federation possibilities**

## Attendees

* Johan Kristiansson <johan.kristiansson@ltu.se>, LTU
* Bocsi Rajmund <rbocsi@aitia.ai>, AITIA
* Tamás Bordi <tbordi@aitia.ai>, AITIA

## Meeting Target

The target of the meeting was to start a thinking about how we can achieve some really improved ways of providing very smooth installation and deployment solution of both Eclipse Arrowhead Core/Support systems and also application systems (consumers/providers).

## Outcome

ColonyOS could provide a "deployment orchestration" solution. The main idea is having "deployment description" or "deployment blueprint" files about a LocalCloud what ColonyOS is capable to process and manage the deployments of the Core, Support and Application system as decribed in the "blueprints". Also, the "deployment orchestration" could cover some resiliance features meaning that the ideal state (defined in the "blueprint") of the deployed systems could be monitored and automatic actions could be taken if states aren't ideal (scale up/down, backup, etc...).

ColonyOS is already capable to assign proper executors to given function descriptions. Similar way, proper "deployment executors" could be assigned the to given deployment jobs, that are defined in the "deployment blueprint". "Deployment executors" would run on the devices of the network and could cover various solutions from a single runtime environment to a containerized environment or virtual machines, etc... Just like ColonyOS does it currently with the existing executors.

**What could be necessary from Arrowhead side?**

The monitoring mechanism - that would be required by ColonyOS to enable the resiliance features - should be implemented by the systems in a LocalCloud.
* In case of Core/Support sytems there is no issue to do it.
* In case of Application systems it violates the principle of "minimal requirements towards application system", but could work with an optional manner. (This is the same concern what always comes up in case of the planned Monitoring and QoS Support Systems). Maybe we could involve these systems into the decision making about "what is the ideal state".
* Certificates can be tricky due to the hostname verification mechanism in the context of system deployment into an environment where the network addresses are dynamically assigned and not known in advance (experienced by Johan in a Kubernetees setup).
  * Hostname verification mechanism can be disabled in the system configuration in case of Core/Support systems for sure. In case of Application system this could be a requirement.
  * Arrowhead5 offers other secure alternatives as well.

**Would this deployment orchestration be benefical in the Arrowhead community?**

We agreed that such a "cloud operator friendly" deployment would be really powerful and would save lot of work **in case of large and complex LocalClouds**.

## Next step

A paper will be created anyway in this topic by LTU within the frames of an ongoing EU projects and that paper will contain more detailed ideas. Once this paper will be available (somewhere around end of december) the content of it should be discussed in an Arrowhead RoadMap meeting or in a separate meeting. Meanwhile, any question comes up in connection with Arrowhead5 to detail the ideas, AITIA is there to support the work. 
