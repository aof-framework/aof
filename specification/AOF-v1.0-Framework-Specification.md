# AI ORCHESTRATION FRAMEWORK

## Framework Specification v1.0

**Status:** Release Candidate — Public-Readiness Hardened / Semantic Freeze Candidate
Freeze Hold **Version:** 1.0 RC-Final-Public-Readiness-Hardening
**Language:** Bahasa Indonesia dengan English Technical Terms\
**Framework Type:** Governed, Risk-Aware, Model-Agnostic, Tool-Agnostic,
Platform-Agnostic\
**Primary Reference Domain:** Secure Software Development Lifecycle
(S-SDLC)\
**Specification Role:** Normative Umbrella Specification

------------------------------------------------------------------------

## Document Convention

Dokumen ini menggunakan Bahasa Indonesia sebagai bahasa utama. Canonical
technical terms, formal identifiers, abbreviations, state names,
component names, dan normative keywords dipertahankan dalam English.

Normative keywords:

-   **MUST** --- requirement wajib untuk conformance.
-   **MUST NOT** --- larangan wajib.
-   **SHOULD** --- recommendation yang diharapkan dipenuhi kecuali
    terdapat alasan terdokumentasi.
-   **SHOULD NOT** --- praktik yang umumnya harus dihindari.
-   **MAY** --- pilihan yang diperbolehkan.

Framework membedakan **Normative Requirement**, **Reference Model**,
**Recommended Practice**, **Example**, dan **Implementation Option**.

------------------------------------------------------------------------

# 1. Introduction

AI systems, Large Language Models (LLMs), AI Agents, Agentic AI, dan
tool-using AI semakin mampu melakukan reasoning, planning, generation,
analysis, delegation, dan execution terhadap external systems.
Peningkatan capability tersebut meningkatkan potensi produktivitas,
tetapi juga memperbesar risiko hallucination, incorrect reasoning,
unauthorized action, context contamination, prompt injection, excessive
delegation, security failure, operational failure, dan accountability
gap.

AI Orchestration Framework (AOF) mendefinisikan model untuk
mengoordinasikan AI dan non-AI actors melalui explicit `Goal`, `Task`,
`Context`, `Capability`, `Authority`, `Policy`, `Risk`, `Decision`,
`Action`, `Evidence`, `Verification`, `State`, dan `Trace`.

Framework berangkat dari prinsip:

\[ Reasoning \neq Decision\neq Authority
\neq Action\]

AI atau `Agent` MAY menghasilkan `Proposal`, tetapi `Proposal` tidak
dengan sendirinya menjadi authorized `Action`.

\[ reason(a,c,t)\rightarrow proposal\]

\[ proposal\not\Rightarrow action\]

Framework memandang orchestration sebagai governed control system, bukan
sekadar agent coordination.

\[ AI Orchestration = Goal Directed Coordination + Bounded Authority +
Policy Control + Risk Control + Evidence Based Verification +
Explicit State Transition + Traceable Accountability \]

AOF v1.0 merupakan evolusi dari v0.1 Conceptual Specification dan v0.2
Formal Specification. v0.1 menetapkan Human-Directed AI Orchestration,
Secure SDLC orientation, `Least Authority`, `Risk-Based Orchestration`,
`Verification Gate`, Human Control, failure learning, dan outcome
measurement. v1.0 mempertahankan intent tersebut sambil menggeneralisasi
model agar dapat diterapkan pada domain orchestration lain tanpa
menghilangkan S-SDLC sebagai primary reference domain.

------------------------------------------------------------------------

# 2. Purpose

AOF bertujuan menyediakan specification yang:

1.  mendefinisikan canonical semantics untuk AI orchestration;
2.  memisahkan reasoning dari system authority dan consequential effect;
3.  memungkinkan bounded dan governed agent autonomy;
4.  mengatur task decomposition, assignment, delegation, execution,
    verification, dan termination;
5.  memastikan consequential action tunduk pada `Authority`, `Policy`,
    `Risk`, dan valid `State`;
6.  menyediakan evidence-based assurance dan traceable accountability;
7.  mendukung Human governance tanpa mewajibkan Human approval pada
    setiap low-risk operation;
8.  tetap model-agnostic, tool-agnostic, platform-agnostic, dan
    deployment-neutral;
9.  memungkinkan conformance assessment;
10. menyediakan foundation untuk reference implementation, framework
    profiles, evaluation, dan domain extensions.

Framework tidak menggantikan Software Engineering, Security Engineering,
Secure SDLC, Risk Management, organizational governance, atau Human
accountability. Framework berfungsi sebagai orchestration and governance
layer di atas praktik tersebut.

------------------------------------------------------------------------

# 3. Scope

## 3.1 In Scope

AOF mencakup:

-   orchestration session dan lifecycle;
-   `Goal` dan `Task`;
-   AI, deterministic, Human, hybrid, dan external-service `Agent`;
-   `Capability` dan `Resource`;
-   context projection dan context isolation;
-   agent selection dan assignment;
-   `Proposal`, `Decision`, dan `Action`;
-   `Authority` dan delegation;
-   `Policy` evaluation;
-   dynamic `Risk`;
-   `Evidence` dan provenance;
-   `Verification`;
-   explicit `State` transition;
-   `Trace` dan accountability;
-   retry, replan, waiting, escalation, failure, abort, cancellation,
    dan compensation;
-   Human governance;
-   trust boundaries dan security controls;
-   conformance dan framework profiles.

## 3.2 Reference Domain

Secure Software Development Lifecycle (S-SDLC) merupakan primary
reference domain, mencakup planning, requirements, architecture, threat
modeling, implementation, testing, security verification, release,
deployment, operations, maintenance, dan continuous improvement.

## 3.3 Out of Scope

Core specification tidak mewajibkan:

-   specific LLM atau model provider;
-   specific agent SDK;
-   specific cloud provider;
-   specific programming language;
-   specific vector database;
-   specific CI/CD platform;
-   specific message broker;
-   microservices;
-   Kubernetes;
-   blockchain;
-   penyimpanan private chain-of-thought.

AI techniques seperti RAG, ReAct, Tree of Thoughts, Few-Shot,
Reflection, dan RCTCF merupakan selectable implementation techniques,
bukan mandatory core constructs.

------------------------------------------------------------------------

# 4. Design Principles

## P-01 --- Human Intent and Accountability

Human governance menetapkan organizational intent, governance envelope,
risk tolerance, dan accountability boundary.

\[ HumanAccountability\neq HumanParticipationInEveryAction\]

Human MAY mendelegasikan bounded operational authority, tetapi
delegation tidak menghilangkan organizational accountability.

## P-02 --- Agent as Bounded Actor

\[ Agent=Bounded Actor \]

\[ Agency(a)\subset eq GovernanceEnvelope(a) \]

Tidak ada `Agent` yang secara inherent merupakan sovereign root of
trust.

## P-03 --- Reasoning Is Not Authority

\[
Reasoning\neq Decision\neq Authority\neq Action
\]

LLM output, recommendation, plan, atau `Proposal` MUST NOT diperlakukan
sebagai permission.

## P-04 --- Capability-Authority Separation

\[ Capability(a,x)\not\Rightarrow Authority(a,x) \]

Technical access, `Role`, `Trust`, `Memory`, reputation, atau prior
success MUST NOT menciptakan implicit authority.

## P-05 --- Least Authority

`Agent` MUST memperoleh authority minimum yang diperlukan dalam scope,
operation, resource, environment, time, quantity, dan risk yang sesuai.

## P-06 --- Policy Mediation

Consequential `Action` MUST dievaluasi terhadap applicable `Policy`.

## P-07 --- Risk-Proportional Control

\[
Risk\uparrow\Rightarrow ControlStrength\uparrow
\]

Control strength MAY mencakup stronger verification, explicit approval,
separation of duties, restricted tools, reduced autonomy, atau
escalation.

## P-08 --- Evidence Before Trust

Generated output adalah candidate result sampai applicable assurance
requirements terpenuhi.

\[ SuccessfulExecution\neq VerifiedOutcome\]

## P-09 --- Verification Independence

High-risk operation SHOULD menggunakan verifier yang sufficiently
independent dari executor sesuai risk dan policy.

## P-10 --- Explicit State Transition

Consequential state mutation MUST terjadi melalui valid transition dan
menghasilkan traceable record.

## P-11 --- Constraint Preservation

Child task, delegation, retry, dan replan MUST mempertahankan applicable
parent constraints kecuali perubahan diotorisasi secara eksplisit.

## P-12 --- Context Least Privilege

`Agent` SHOULD menerima minimum context yang diperlukan untuk task dan
MUST NOT memperluas context boundary secara unilateral.

## P-13 --- Bounded Failure

Retry, replan, waiting, delegation depth, time, cost, dan autonomous
execution SHOULD memiliki bounded control.

## P-14 --- Model and Tool Agnosticism

Framework MUST tetap valid ketika model, tool, runtime, atau provider
diganti.

## P-15 --- Outcome, Evidence, and Trace

Framework outcome tidak hanya berupa output.

\[
\mathcal{O}(q)\rightarrow\langle o,e,\tau\rangle
\]

yaitu `Outcome + Evidence + Trace`.

------------------------------------------------------------------------

# 5. Normative Terminology

  ---------------------------------------------------------------------
  Term                               Normative Meaning
  ---------------------------------- ----------------------------------
  `Agent`                            Identifiable bounded actor yang
                                     dapat melakukan reasoning,
                                     deterministic processing, Human
                                     action, hybrid processing, atau
                                     external service operation.

  `Goal`                             Desired outcome dengan success
                                     criteria dan constraints.

  `Task`                             Unit orchestration work yang
                                     diturunkan dari Goal.

  `Context`                          Informasi yang tersedia untuk
                                     reasoning atau control dalam
                                     defined scope.

  `Capability`                       Kemampuan teknis atau fungsional
                                     untuk melakukan operation.

  `Resource`                         Target atau facility yang dapat
                                     dibaca, dimodifikasi, dieksekusi,
                                     atau di-invoke.

  `Proposal`                         Candidate output dari reasoning
                                     yang belum merupakan authorized
                                     decision.

  `Decision`                         Control selection yang dibuat
                                     berdasarkan state, policy,
                                     authority, risk, evidence, dan
                                     applicable criteria.

  `Action`                           Operation yang dapat menyebabkan
                                     internal atau external effect.

  `Authority`                        Explicit bounded right untuk
                                     melakukan operation terhadap
                                     resource dalam scope tertentu.

  `Policy`                           Normative rule yang membatasi
                                     decision atau action.

  `Risk`                             Representasi likelihood, impact,
                                     exposure, controls, dan residual
                                     adverse outcome.

  `Evidence`                         Identifiable artifact yang
                                     mendukung atau menyangkal claim
                                     serta memiliki provenance.

  `Verification`                     Evaluasi claim terhadap criteria
                                     dan evidence.

  `State`                            Authoritative orchestration
                                     snapshot pada waktu tertentu.

  `Trace`                            Append-oriented governance record
                                     untuk merekonstruksi orchestration
                                     activity.

  `Orchestrator`                     Control component yang
                                     mengoordinasikan lifecycle dan
                                     decision flow.

  `Safety Kernel`                    Minimal governance mediation
                                     functions untuk consequential
                                     operation.

  `Governance Envelope`              Batas effective autonomy yang
                                     dibentuk oleh Authority, Policy,
                                     Risk, Context, Resource, State,
                                     dan Verification requirements.

  `Consequential Action`             Action yang dapat menimbulkan
                                     material state change, external
                                     effect, privileged operation,
                                     security impact, financial impact,
                                     safety impact, atau organizational
                                     impact.

  `Conformance`                      Kondisi ketika implementation
                                     memenuhi mandatory requirements
                                     dari applicable AOF profile.
  ---------------------------------------------------------------------

Canonical state names, identifiers, abbreviations, dan normative
keywords menggunakan English.

------------------------------------------------------------------------

# 6. Framework Definition

## 6.1 System Definition

AI Orchestration Framework didefinisikan sebagai:

\[ \mathcal{O}=
\langle A,T,C,R,P,H,V,S,E,D,\Delta\rangle\]

dengan:

-   (A): set of `Agents`;
-   (T): set of `Tasks`;
-   (C): `Context` space;
-   (R): `Resources` and tools;
-   (P): `Policy` set;
-   (H): `Authority` model;
-   (V): `Verification` model;
-   (S): system `State` space;
-   (E): `Evidence` space;
-   (D): `Decision` space;
-   (\Delta): state transition function.

Request:

\[ q=\langle i,c_0,g\rangle\]

Execution:

\[
\mathcal{O}(q)\rightarrow\langle o,e,\tau\rangle
\]

## 6.2 Canonical Control Predicate

Candidate action hanya dapat dieksekusi ketika applicable control
conditions terpenuhi:

\[ ExecuteAllowed=
C\land H\land P\land S\land R\land V
\]

dengan (C) = capability validity, (H) = authority validity, (P) = policy
compliance, (S) = state validity, (R) = risk acceptability, dan (V) =
applicable verification satisfaction.

Control evaluation menggunakan three-valued semantics:

\[ GateResult={Pass,Fail,Pending} \]

Unknown atau undetermined control predicate MUST menghasilkan `Pending`,
bukan implicit allow.

## 6.3 Canonical Control Loop

\[
Observe\rightarrow Reason\rightarrow Propose\rightarrow Govern\rightarrow Act\rightarrow Verify\rightarrow Update
\]

`Govern` mencakup applicable `Authority`, `Policy`, `Risk`, dan
`StateValidation`.

------------------------------------------------------------------------

# 7. Core Constructs

Canonical constructs:

\[ \mathbb{C}= {
Agent,Task,Goal,Context,Resource,Capability,Authority,Policy,Decision,Action,Evidence,Verification,Risk,State,Trace
} \]

## 7.1 Classification

\[ Intent={Goal,Task} \]

\[ Execution={Agent,Capability,Resource,Action} \]

\[ Governance={Authority,Policy,Risk} \]

\[ Assurance={Evidence,Verification} \]

\[ Control={Context,Decision,State,Trace} \]

## 7.2 Canonical Relationship

\[
Goal\rightarrow Task\rightarrow Agent\rightarrow Proposal
\]

`Proposal` dievaluasi melalui:

\[ Context+Authority+Policy+Risk+State \]

untuk menghasilkan `Decision`.

Jika permitted:

\[ Decision\rightarrow Action\rightarrow Effect\]

Kemudian:

\[
Action\rightarrow Evidence\rightarrow Verification\rightarrow State
\]

dan seluruh lifecycle direkam dalam `Trace`.

## 7.3 Accountability Chain

\[
Goal\rightarrow Task\rightarrow Decision\rightarrow Agent\rightarrow Authority\rightarrow Policy\rightarrow Action\rightarrow Evidence\rightarrow Verification\rightarrow Outcome
\]

Consequential action dengan broken accountability chain MUST dianggap
incomplete untuk conformance sampai required linkage dipulihkan atau
action ditangani sesuai failure policy.

------------------------------------------------------------------------

# 8. Architectural Model

## 8.1 Purpose and Architectural Objectives

Architectural Model mendefinisikan logical structure yang diperlukan
agar orchestration mempertahankan separation antara reasoning,
governance, effect, dan assurance. Architecture ini bukan mandatory
physical deployment topology. Implementation MAY menggunakan monolith,
modular process, microservices, distributed services, serverless
components, embedded runtime, atau federated deployment selama normative
architectural properties tetap dipertahankan.

Architectural objectives adalah:

1.  mencegah `Agent` atau reasoning component menjadi implicit root of
    authority;
2.  memastikan consequential `Action` dimediasi oleh governance
    controls;
3.  memisahkan `Proposal`, `Decision`, `Effect`, dan `Verification`;
4.  menyediakan authoritative `State` dan reconstructable `Trace`;
5.  mempertahankan bounded `Context`, `Authority`, dan `Resource`
    access;
6.  mendukung revocation, retry, replan, escalation, dan recovery secara
    controlled;
7.  memungkinkan independent assurance sesuai `Risk`;
8.  menjaga deployment neutrality dan technology neutrality.

Canonical architectural principle:

\[ Reasoning Plane \neq Control Plane \neq Effect Plane
\neq Assurance Plane \]

Logical separation MUST dipertahankan walaupun dua atau lebih plane
secara fisik berada dalam process, host, runtime, atau service yang
sama.

------------------------------------------------------------------------

## 8.2 Canonical Architecture

Reference logical architecture:

```text
                       HUMAN / ORGANIZATIONAL GOVERNANCE
                                      |
                                      v
+------------------------------------------------------------------+
|                         CONTROL PLANE                            |
|                                                                  |
|  Orchestrator / Control Logic                                    |
|        |                                                         |
|        +--> Task & Session Control                               |
|        +--> Agent Selection / Assignment                         |
|        +--> Context Projection                                   |
|        |                                                         |
|        +--> ORCHESTRATION SAFETY KERNEL                          |
|              +-- Authority Evaluator                             |
|              +-- Policy Evaluator                                |
|              +-- Risk Gate                                       |
|              +-- State Validator                                 |
|              +-- Verification Gate                              |
|              +-- Trace Recorder                                  |
+---------------------------+--------------------------------------+
                            |
                Governed Decision / Control Outcome
                            |
          +-----------------+-----------------+
          |                                   |
          v                                   v
+-------------------------+       +-----------------------------+
|    REASONING PLANE      |       |       ASSURANCE PLANE       |
|                         |       |                             |
| Agent Pool              |       | Evidence Collection         |
| Planner                 |       | Verification                |
| Analyzer                |       | Validation                  |
| Generator               |       | Review                      |
| Recommender             |       | Audit                       |
+------------+------------+       +--------------^--------------+
             |                                   |
             | Proposal                          | Evidence
             v                                   |
+------------------------------------------------------------------+
|                          EFFECT PLANE                             |
|                                                                  |
| Execution Gateway                                                |
| Tools | APIs | Files | DB | CI/CD | Infrastructure | Services    |
+----------------------------+-------------------------------------+
                             |
                             v
                      External / Internal Effect
```

Architecture MUST preserve the semantic distinction:

\[
Proposal\neq Decision\neq Action\neq Effect\neq Verification
\]

------------------------------------------------------------------------

## 8.3 Architectural Components

A conformant architecture MUST provide functions semantically equivalent
to the components below. Component names dan physical boundaries MAY
berbeda.

### 8.3.1 Orchestrator

`Orchestrator` mengoordinasikan lifecycle, tetapi bukan unbounded
authority holder.

Reference responsibilities:

-   session initialization;
-   task decomposition coordination;
-   task readiness evaluation;
-   agent selection and assignment;
-   proposal routing;
-   control evaluation coordination;
-   retry/replan/escalation coordination;
-   termination evaluation.

\[ Orchestrator\neq UnboundedAgent\]

`Orchestrator` MUST NOT bypass applicable `Authority`, `Policy`, `Risk`,
`State`, atau `Verification` controls.

### 8.3.2 Agent Runtime / Agent Pool

Agent Runtime menyediakan controlled environment untuk `Agent` reasoning
atau deterministic processing.

Agent Runtime SHOULD expose:

-   stable agent identity;
-   declared capabilities;
-   assigned task;
-   scoped context;
-   applicable governance envelope;
-   proposal/output interface;
-   observable execution status.

Direct consequential tool access dari reasoning component MUST NOT
bypass equivalent Effect Boundary controls.

### 8.3.3 Agent Registry

Jika dynamic agent selection digunakan, implementation SHOULD memiliki
authoritative atau equivalently controlled registry untuk:

-   identity;
-   type;
-   role;
-   capability;
-   supported interfaces;
-   trust metadata;
-   eligibility metadata;
-   lifecycle status.

Registry entry MUST NOT dengan sendirinya memberikan `Authority`.

### 8.3.4 Context Manager

Context Manager atau equivalent function mengendalikan context
acquisition, classification, projection, isolation, freshness, dan
disclosure.

Untuk agent (a) dan task (t):

\[ VisibleContext(a,t)\subset eq AvailableContext\]

dan SHOULD mendekati:

\[ VisibleContext(a,t)=MinimumContextRequired(a,t) \]

Context Manager MUST preserve applicable sensitivity dan trust metadata.

### 8.3.5 Execution Gateway

Execution Gateway adalah logical boundary antara governed decision dan
resource effect.

Responsibilities SHOULD mencakup:

-   operation normalization;
-   actor identity binding;
-   resource/target resolution;
-   final control token/decision validation;
-   applicable precondition validation;
-   execution;
-   result capture;
-   effect metadata capture;
-   evidence return.

\[ ControlPermit\not\Rightarrow ExecutionSuccess\]

dan:

\[ ExecutionSuccess\not\Rightarrow VerifiedOutcome\]

### 8.3.6 State Store

Implementation MUST memiliki authoritative state function untuk
consequential orchestration state.

Agent-local memory, prompt context, model conversation history, cache,
atau private runtime state MUST NOT menjadi satu-satunya authoritative
source untuk consequential orchestration state.

### 8.3.7 Trace Store

Trace Store atau equivalent function mempertahankan governance events
yang diperlukan untuk reconstruction, accountability, audit, dan
conformance evidence.

Trace storage MAY menggunakan database, event log, append-oriented
store, distributed log, atau equivalent mechanism.

### 8.3.8 Evidence Store

Jika evidence harus bertahan melampaui immediate verification,
implementation SHOULD menyediakan evidence storage atau durable
reference yang mempertahankan provenance dan integrity metadata.

### 8.3.9 Approval Interface

Jika applicable `Policy` memerlukan explicit approval, architecture MUST
menyediakan controlled approval path yang mengikat approval kepada:

-   approver identity;
-   subject;
-   requested operation;
-   applicable scope;
-   timestamp;
-   decision;
-   expiry atau validity jika diperlukan.

Approval MUST NOT menjadi reusable universal permission kecuali secara
eksplisit didefinisikan demikian oleh valid `Authority` dan `Policy`.

------------------------------------------------------------------------

## 8.4 Four-Plane Architecture

### 8.4.1 Reasoning Plane

\[ RP= { Reason, Plan, Generate, Analyze, Recommend } \]

Reasoning Plane menghasilkan candidate interpretation, plan,
decomposition, recommendation, content, atau `Proposal`.

Reasoning Plane MAY bersifat probabilistic atau nondeterministic.

Reasoning Plane MUST NOT diasumsikan memiliki authority hanya karena
mampu menghasilkan valid action specification.

\[ ReasoningCapability\not\Rightarrow ExecutionAuthority
\]

### 8.4.2 Control Plane

\[ CP= { Assign, Authorize, EvaluatePolicy, AssessRisk, ValidateState,
Approve, Escalate, Retry, Replan, Terminate } \]

Control Plane mengubah proposal menjadi governed `Decision`.

Control Plane SHOULD menggunakan deterministic atau bounded-evaluation
mechanisms untuk security-critical predicates ketika practical.

### 8.4.3 Effect Plane

\[ EP= { Read, Write, Execute, Invoke, Modify, Create, Delete, Deploy }
\]

Effect Plane melakukan operation terhadap `Resource`.

Effect Plane MUST dapat mengidentifikasi actor atau delegated execution
identity yang menyebabkan operation.

### 8.4.4 Assurance Plane

\[ AP= { CollectEvidence, Verify, Validate, Review, Audit } \]

Assurance Plane mengevaluasi claim, result, compliance, atau outcome.

Assurance Plane MUST mempertahankan applicable independence requirement
dari executor sesuai `Risk`, `Policy`, dan profile.

------------------------------------------------------------------------

## 8.5 Plane Separation Principle

Plane separation adalah semantic separation, bukan mandatory
infrastructure separation.

Implementation MAY menggunakan satu service untuk beberapa plane jika:

1.  interfaces tetap distinguishable;
2.  authority boundaries tetap enforceable;
3.  control evaluation tidak dapat dilewati;
4.  assurance independence yang diwajibkan tetap dapat dibuktikan;
5.  trace dapat membedakan reasoning, decision, effect, dan verification
    events.

Untuk high-assurance deployment, physical atau administrative separation
SHOULD meningkat sesuai `Risk`.

------------------------------------------------------------------------

## 8.6 Orchestration Safety Kernel

Reference Safety Kernel:

\[ K= { AuthorityEvaluator, PolicyEvaluator, StateValidator, RiskGate,
VerificationGate, TraceRecorder } \]

Kernel menerima candidate consequential operation (x_c) dalam state (s):

\[
K(x_c,s)\rightarrow { Permit, Deny, Verify, Approve, Replan, Retry, Escalate, Abort }
\]

Safety Kernel merupakan logical trusted control boundary. Implementation
MAY membagi kernel menjadi beberapa components atau services, tetapi
MUST mempertahankan equivalent mediation semantics.

### 8.6.1 Kernel Mediation

\[ Consequential(x)\Rightarrow MediatedBy(K,x) \]

No direct path MAY memungkinkan consequential effect yang menghindari
applicable kernel evaluation.

### 8.6.2 Kernel Non-Circularity

Satu discretionary reasoning agent SHOULD NOT menjadi satu-satunya actor
yang sekaligus:

1.  menentukan applicable policy;
2.  memberikan authority;
3.  menilai risk;
4.  mengeksekusi effect;
5.  memverifikasi hasil;
6.  menghapus atau mengubah audit evidence.

### 8.6.3 No Safety by Prompt Alone

Prompt instruction MAY membantu agent behavior tetapi MUST NOT menjadi
satu-satunya enforcement mechanism untuk mandatory consequential
control.

\[ PromptInstruction\neq EnforcedControl\]

------------------------------------------------------------------------

## 8.7 Canonical Control Evaluation

Sebelum consequential action, architecture MUST mengevaluasi:

\[ ExecuteAllowed(a,x,s)=
C\land H\land P\land S\land R\land V
\]

dengan:

-   (C): `CapabilityValid`;
-   (H): `AuthorityValid`;
-   (P): `PolicyCompliant`;
-   (S): `StateValid`;
-   (R): `RiskAcceptable`;
-   (V): `VerificationSatisfied` jika pre-action verification required.

Control predicate menggunakan:

\[ GateResult={Pass,Fail,Pending} \]

Jika mandatory predicate `Fail`:

\[ ExecuteAllowed=false \]

Jika mandatory predicate `Pending`:

\[ ExecuteAllowed=Pending \]

`Pending` MUST NOT diperlakukan sebagai `Permit`.

------------------------------------------------------------------------

## 8.8 Control Token / Decision Binding

Implementation SHOULD mengikat permit terhadap candidate action yang
dievaluasi.

Conceptual binding:

\[ permit= Bind( actor, action, resource, parameters, stateVersion,
authorityVersion, policyContext, riskContext, validity ) \]

Perubahan material terhadap bound attributes SHOULD menginvalidasi
permit atau memicu reevaluation.

Implementation tidak diwajibkan menggunakan literal token; semantic
equivalence cukup.

------------------------------------------------------------------------

## 8.9 Effect Boundary Principle

Effect Boundary adalah titik terakhir sebelum operation menyebabkan
material internal atau external effect.

Pada boundary tersebut, implementation MUST memastikan bahwa applicable
decision masih valid.

\[
DecisionValid\_{t_1}\not\Rightarrow DecisionValid\_{t_2}
\]

untuk (t_2\>t_1) jika relevant state dapat berubah.

High-risk atau time-sensitive operation SHOULD melakukan revalidation
pada atau sedekat mungkin dengan Effect Boundary.

------------------------------------------------------------------------

## 8.10 State Ownership and Authority

Consequential orchestration state MUST memiliki authoritative owner atau
authoritative coordination mechanism.

Canonical rule:

\[ AuthoritativeState\neq AgentPrivateMemory\]

`Agent` MAY menyimpan working memory, scratch state, atau local
execution context, tetapi consequential state mutation hanya valid jika
diterima melalui governed transition mechanism.

Jika distributed state digunakan, implementation MUST memiliki conflict
detection atau equivalent consistency mechanism yang mencegah silent
contradictory state.

------------------------------------------------------------------------

## 8.11 State--Trace Coherence

Untuk setiap consequential state transition:

\[ StateChange\Rightarrow TransitionRecord\]

dan:

\[ CommittedTransition(s_i,s_j) \Rightarrow Traceable(s_i,s_j)
\]

Trace dan State SHOULD memungkinkan reconstruction terhadap order dan
causal relationship yang diperlukan.

Jika trace persistence gagal setelah consequential effect, system MUST
memperlakukan kondisi tersebut sebagai governance failure dan mengikuti
applicable recovery/escalation policy; system MUST NOT silently
menganggap auditability complete.

------------------------------------------------------------------------

## 8.12 Context Architecture

Context bukan synonym untuk prompt.

Reference context classes MAY mencakup:

-   User Context;
-   System Context;
-   Task Context;
-   Policy Context;
-   Environment Context;
-   Retrieved Context;
-   Generated Context;
-   Historical Context.

Setiap context item SHOULD memiliki metadata yang cukup untuk
menentukan:

-   source;
-   scope;
-   trust;
-   sensitivity;
-   freshness;
-   intended consumer.

### 8.12.1 Context Projection

\[ ContextProjection(a,t)=C\_{a,t}\subset eq C\]

Projection MUST mempertahankan applicable data minimization dan
disclosure constraints.

### 8.12.2 Context Trust Boundary

External, retrieved, generated, atau agent-produced content MUST NOT
secara otomatis memperoleh control authority.

\[ Content\neq InstructionAuthority\]

Architecture SHOULD memisahkan data-bearing content dari control-bearing
instruction ketika practical.

### 8.12.3 Context Freshness

Time-sensitive context SHOULD memiliki freshness semantics. Stale
context yang material terhadap decision MUST memicu refresh, `Pending`,
replan, atau escalation sesuai policy.

------------------------------------------------------------------------

## 8.13 Resource and Tool Architecture

Tool availability menunjukkan technical reachability, bukan
authorization.

\[ ToolAccess\neq Authority\]

Resource interface SHOULD mendeklarasikan supported operations dan
relevant security characteristics.

Untuk invocation:

\[
invoke(a,r,x)\rightarrow\langle result,effect,evidence\rangle
\]

Execution Gateway MUST memastikan bahwa actual operation tidak lebih
luas daripada governed operation.

Wildcard atau broad technical credential SHOULD dibatasi oleh logical
authority enforcement jika underlying tool tidak menyediakan
sufficiently granular permissions.

------------------------------------------------------------------------

## 8.14 Evidence Return Principle

Consequential effect SHOULD menghasilkan sufficient result/effect
evidence untuk downstream verification dan state reconciliation.

\[ Action\rightarrow Result+EffectEvidence \]

Evidence return SHOULD memungkinkan system membedakan:

-   request accepted;
-   operation started;
-   operation completed;
-   intended effect occurred;
-   unintended effect occurred;
-   outcome verified.

Absence of sufficient evidence MUST NOT otomatis dianggap successful
verified completion.

------------------------------------------------------------------------

## 8.15 Assurance Pipeline

Reference assurance flow:

```text
Action / Result
      |
      v
Evidence Collection
      |
      v
Provenance / Integrity Check
      |
      v
Verification Criteria Selection
      |
      v
Verification
      |
      +--> Verified
      +--> Rejected
      +--> Inconclusive
      |
      v
Control / State Decision
```

Assurance Plane MAY memanggil deterministic tests, specialist agents,
Human reviewers, external validators, atau composite mechanisms.

Verification result MUST kembali ke Control Plane atau equivalent
state-transition authority sebelum terminal success ditetapkan bila
verification diwajibkan.

------------------------------------------------------------------------

## 8.16 Trust Boundary Model

Architecture MUST mengidentifikasi trust boundaries yang relevan.
Minimum reference boundaries:

### TB-01 --- External Input Boundary

User input, retrieved content, external messages, documents, web
content, atau third-party data dapat mengandung malicious atau
misleading instructions.

### TB-02 --- Agent Boundary

Agent output merupakan `Proposal` atau result, bukan implicit system
decision.

### TB-03 --- Inter-Agent Boundary

Message dari satu agent ke agent lain MUST mempertahankan identity,
task, context, constraints, dan applicable authority metadata yang
diperlukan.

### TB-04 --- Tool/Resource Boundary

Tool response MAY salah, stale, incomplete, malicious, atau semantically
ambiguous.

### TB-05 --- Effect Boundary

Permit harus dipastikan masih applicable sebelum consequential effect.

### TB-06 --- Human Interaction Boundary

Human approval/review MUST diikat pada identifiable subject dan scope.

### TB-07 --- Evidence Boundary

Evidence ingestion MUST mempertahankan provenance dan SHOULD
mempertimbangkan integrity serta source trust.

### TB-08 --- State/Trace Boundary

Unauthorized mutation terhadap state atau trace MUST dicegah atau
detectable sesuai profile.

------------------------------------------------------------------------

## 8.17 Inter-Plane Interaction Contract

Cross-plane interaction SHOULD menggunakan explicit semantic messages
atau equivalent contracts.

Minimum interaction classes:

-   `TaskAssignment`;
-   `ContextProjection`;
-   `Proposal`;
-   `ControlRequest`;
-   `ControlDecision`;
-   `ActionRequest`;
-   `ActionResult`;
-   `EvidenceSubmission`;
-   `VerificationResult`;
-   `StateTransition`;
-   `Escalation`;
-   `TerminationDecision`.

Setiap consequential interaction SHOULD memiliki correlation identity
yang memungkinkan end-to-end reconstruction.

------------------------------------------------------------------------

## 8.18 Decision Flow

Reference decision flow:

```text
Task
 |
 v
Agent Reasoning
 |
 v
Proposal
 |
 v
Control Request
 |
 +--> Capability Evaluation
 +--> Authority Evaluation
 +--> Policy Evaluation
 +--> Risk Evaluation
 +--> State Validation
 +--> Verification Requirement
 |
 v
Control Outcome
 |
 +--> Permit
 +--> Deny
 +--> Verify
 +--> Approve
 +--> Replan
 +--> Retry
 +--> Escalate
 +--> Abort
```

`Permit` hanya berarti applicable pre-effect control conditions
satisfied.

------------------------------------------------------------------------

## 8.19 Concurrency and Conflict Control

Architecture MAY menjalankan tasks secara concurrent jika dependency,
resource, authority, dan state constraints memungkinkan.

Concurrent actions yang dapat mengubah shared consequential state SHOULD
menggunakan conflict-control mechanism.

Possible mechanisms MAY mencakup:

-   optimistic version checking;
-   locking;
-   compare-and-swap;
-   serialized decision queue;
-   transactional boundary;
-   lease;
-   domain-specific reconciliation.

Framework tidak mewajibkan mechanism tertentu.

Canonical property:

\[ ConcurrentExecution\Rightarrow NoSilentConflictingCommit\]

------------------------------------------------------------------------

## 8.20 Time-of-Check to Time-of-Use (TOCTOU)

Control decision dapat menjadi stale akibat perubahan:

-   Authority;
-   Policy;
-   State;
-   Risk;
-   Resource;
-   Environment;
-   approval validity.

\[ Check\_{t_1}\not\Rightarrow Valid\_{t_2} \]

Architecture MUST menentukan revalidation policy untuk consequential
operations.

High-risk profile SHOULD menggunakan stricter revalidation daripada
low-risk profile.

------------------------------------------------------------------------

## 8.21 Authority Revocation Propagation

Jika authority direvoke, suspend, expire, atau consumed:

1.  new dependent action MUST ditolak;
2.  queued action MUST direevaluasi;
3.  in-progress action SHOULD dihentikan jika safe dan applicable;
4.  irreversible effect yang telah terjadi MUST direkonsiliasi melalui
    state/evidence/recovery flow;
5.  revocation event MUST traceable.

\[ Revoked(h)\Rightarrow\neg NewExecutionUsing(h) \]

------------------------------------------------------------------------

## 8.22 Dynamic Risk Propagation

Material risk change MUST dapat mempengaruhi pending dan future
decisions.

\[ Risk\_{t_2}\>Risk\_{t_1} \]

MAY menyebabkan:

-   stronger verification;
-   reduced authority;
-   approval requirement;
-   resource restriction;
-   replan;
-   escalation;
-   abort.

Architecture MUST NOT mengasumsikan risk classification immutable selama
session.

------------------------------------------------------------------------

## 8.23 Retry and Replan Architecture

`Retry` dan `Replan` merupakan Control Plane decisions, bukan
discretionary infinite loops.

Retry MUST mempertimbangkan:

-   retry limit;
-   idempotency;
-   prior effect;
-   resource state;
-   authority validity;
-   policy validity;
-   risk change;
-   evidence from previous attempt.

Replan MUST mempertahankan applicable Goal dan constraints kecuali
authorized change tersedia.

Agent MAY mengusulkan retry/replan, tetapi proposal tersebut tetap
tunduk pada Control Plane.

------------------------------------------------------------------------

## 8.24 Failure Boundaries

Architecture SHOULD mengisolasi failure sehingga failure pada satu
component tidak otomatis memberikan broader authority atau menyebabkan
uncontrolled effect.

Reference failure boundaries:

-   reasoning failure;
-   control evaluation failure;
-   state persistence failure;
-   trace persistence failure;
-   tool failure;
-   evidence failure;
-   verification failure;
-   communication failure;
-   Human approval timeout.

Fail-open behavior MUST NOT digunakan untuk mandatory authority, policy,
state, atau critical security controls kecuali explicit profile/policy
secara sah mendefinisikannya.

Default safety posture untuk undetermined mandatory control adalah:

\[ Unknown\rightarrow Pending/Deny/Escalate \]

bukan implicit permit.

------------------------------------------------------------------------

## 8.25 Escalation Architecture

Escalation package SHOULD memuat sufficient context agar receiving actor
dapat membuat informed decision tanpa kehilangan governance chain.

Reference escalation data:

-   session/task identity;
-   reason;
-   current state;
-   relevant proposal/action;
-   authority result;
-   policy result;
-   risk result;
-   available evidence;
-   prior attempts;
-   requested decision;
-   expiry/urgency jika applicable.

Escalation MUST NOT secara otomatis memperluas authority dari actor yang
mengeskalasi.

------------------------------------------------------------------------

## 8.26 Human Governance Boundary

Human atau organizational governance menetapkan root governance
conditions seperti policy source, authority issuance model, risk
tolerance, approval rules, dan accountability structure.

Operational delegation MAY diberikan kepada Agent:

\[ AgentAuthority\subset eq DelegatedGovernanceEnvelope\]

Human interaction MAY berada di Control Plane atau Assurance Plane
sesuai role.

Human actor MUST tetap memiliki identifiable authority untuk
consequential approval atau override.

------------------------------------------------------------------------

## 8.27 Separation of Duties Architecture

Architecture SHOULD memungkinkan distinct actors untuk:

-   propose;
-   authorize;
-   execute;
-   verify;
-   approve;
-   audit.

Tidak semua operation membutuhkan actor berbeda. Required separation
ditentukan oleh `Risk`, `Policy`, dan profile.

Untuk high-risk action, architecture MUST mampu mendukung independent
verification jika profile mensyaratkannya.

------------------------------------------------------------------------

## 8.28 Observability Architecture

Conformant implementation MUST menyediakan observability yang cukup
untuk reconstruct consequential orchestration.

Minimum observable dimensions SHOULD mencakup:

-   session;
-   task;
-   actor;
-   proposal;
-   control decision;
-   action;
-   resource;
-   result;
-   evidence;
-   verification;
-   state transition;
-   failure;
-   escalation;
-   termination.

Observability MUST NOT memerlukan penyimpanan private chain-of-thought.

------------------------------------------------------------------------

## 8.29 Architecture Security Properties

Architecture MUST mendukung properties berikut sesuai applicable
profile:

### AOF-ARCH-SP-01 --- Non-Bypassability

Mandatory governance controls tidak dapat dilewati melalui alternate
execution path.

### AOF-ARCH-SP-02 --- Attribution

Consequential action dapat dikaitkan dengan actor dan task/session.

### AOF-ARCH-SP-03 --- Bounded Authority

Technical capability tidak memperluas granted authority.

### AOF-ARCH-SP-04 --- State Integrity

Consequential state change terjadi melalui controlled transition.

### AOF-ARCH-SP-05 --- Traceability

Required decision/action chain dapat direkonstruksi.

### AOF-ARCH-SP-06 --- Assurance Independence

Architecture dapat menyediakan verifier independence sesuai profile.

### AOF-ARCH-SP-07 --- Revocation Responsiveness

Revoked authority tidak dapat digunakan untuk new consequential
execution.

### AOF-ARCH-SP-08 --- Context Isolation

Agent hanya menerima context yang required atau explicitly authorized.

### AOF-ARCH-SP-09 --- Fail-Controlled

Undetermined mandatory governance state tidak menjadi implicit permit.

### AOF-ARCH-SP-10 --- Effect Reconciliation

System dapat membedakan intended request, actual effect, dan verified
outcome.

------------------------------------------------------------------------

## 8.30 Deterministic and Agentic Components

Framework tidak mengharuskan semua component menggunakan AI.

Security-critical control functions SHOULD menggunakan deterministic
mechanisms jika semantics dapat diekspresikan secara deterministic dan
practical.

Examples yang biasanya cocok untuk deterministic enforcement:

-   authority scope matching;
-   policy rule evaluation;
-   state transition validation;
-   retry counter;
-   expiry check;
-   resource allowlist;
-   trace persistence validation.

Agentic reasoning MAY digunakan untuk:

-   planning;
-   decomposition;
-   analysis;
-   recommendation;
-   classification;
-   evidence interpretation;
-   complex review.

Jika agentic component digunakan untuk control decision, implementation
MUST tetap mempertahankan bounded authority, traceability, dan
applicable verification.

------------------------------------------------------------------------

## 8.31 Deployment Topologies

AOF mendukung beberapa deployment topology.

### 8.31.1 Centralized

Satu Control Plane mengoordinasikan Agent Pool dan Effect Plane.

### 8.31.2 Hierarchical

Parent Orchestrator mendelegasikan bounded sub-orchestration kepada
child orchestrators.

Delegation conservation tetap berlaku pada setiap level.

### 8.31.3 Distributed

Control functions tersebar pada beberapa services atau nodes.

Distributed implementation MUST menjaga state consistency, identity,
authority propagation, dan trace correlation.

### 8.31.4 Federated

Beberapa administrative domain mempertahankan governance masing-masing
dan berinteraksi melalui explicit contracts.

Cross-domain action MUST memiliki authority dan policy yang valid pada
relevant domains.

### 8.31.5 Embedded

AOF controls MAY ditanamkan dalam application atau workflow engine
selama logical separation dan non-bypassability tetap dapat dibuktikan.

Tidak ada topology yang secara inherent lebih conformant daripada
topology lain.

------------------------------------------------------------------------

## 8.32 Multi-Orchestrator Architecture

Jika lebih dari satu Orchestrator digunakan:

\[ Authority(O_i)\not\Rightarrow Authority(O_j) \]

Setiap Orchestrator MUST memiliki explicit scope.

Cross-orchestrator delegation atau task transfer MUST mempertahankan:

-   task identity;
-   constraints;
-   authority;
-   context classification;
-   risk;
-   evidence references;
-   trace correlation.

Circular delegation SHOULD dideteksi dan dibatasi.

------------------------------------------------------------------------

## 8.33 Availability and Liveness

Architecture SHOULD menghindari indefinite orchestration state.

Setiap waiting atau blocked state SHOULD memiliki salah satu:

-   resume condition;
-   timeout;
-   retry bound;
-   escalation path;
-   cancellation path;
-   termination path.

Safety MUST memiliki precedence atas liveness ketika keduanya konflik
pada consequential action.

\[ SafetyViolationRisk\Rightarrow NoForcedProgress\]

------------------------------------------------------------------------

## 8.34 Deadlock and Livelock Control

Implementation SHOULD mendeteksi atau membatasi:

-   cyclic task dependency;
-   repeated retry without progress;
-   repeated replan without material change;
-   approval loops;
-   verifier loops;
-   delegation loops;
-   conflicting resource locks.

Framework tidak menentukan universal deadlock algorithm, tetapi
uncontrolled infinite orchestration MUST NOT dianggap conformant
controlled execution.

------------------------------------------------------------------------

## 8.35 Architecture-Level Privacy and Sensitive Data Controls

Context dan evidence architecture SHOULD mendukung:

-   data classification;
-   minimum disclosure;
-   secret isolation;
-   redaction;
-   retention constraints;
-   purpose limitation;
-   access control;
-   cross-boundary transfer control.

Sensitive data MUST NOT diberikan kepada Agent atau external service
hanya karena data tersedia pada global orchestration context.

------------------------------------------------------------------------

## 8.36 Architecture Conformance Requirements

Architecture yang menyatakan conformance terhadap AOF-Core MUST
menunjukkan minimal bahwa:

**AOF-ARCH-001** --- `Proposal`, `Decision`, dan consequential `Action`
dapat dibedakan secara semantik.

**AOF-ARCH-002** --- Consequential `Action` tidak dapat bypass
applicable governance evaluation.

**AOF-ARCH-003** --- `Capability` atau technical tool access tidak
otomatis menciptakan `Authority`.

**AOF-ARCH-004** --- Mandatory control result `Pending` atau unknown
tidak diperlakukan sebagai implicit allow.

**AOF-ARCH-005** --- Consequential state mutation menggunakan controlled
transition.

**AOF-ARCH-006** --- Consequential action dan transition menghasilkan
sufficient trace untuk reconstruction.

**AOF-ARCH-007** --- Implementation memiliki authoritative orchestration
state function yang terpisah secara semantik dari agent private memory.

**AOF-ARCH-008** --- Revoked/expired authority tidak dapat digunakan
untuk new consequential execution.

**AOF-ARCH-009** --- Effect Boundary memiliki mechanism untuk memastikan
applicable decision masih valid sesuai revalidation policy.

**AOF-ARCH-010** --- Architecture dapat mengembalikan result/effect
evidence untuk applicable assurance.

AOF-Governed SHOULD juga memenuhi:

**AOF-ARCH-011** --- Dynamic risk dapat memicu control reevaluation.

**AOF-ARCH-012** --- Delegation dan multi-orchestrator transfer
mempertahankan governance envelope.

**AOF-ARCH-013** --- Failure pada mandatory control tidak menghasilkan
silent fail-open.

**AOF-ARCH-014** --- Concurrency terhadap shared consequential state
memiliki conflict-control mechanism.

AOF-Assured SHOULD juga memenuhi:

**AOF-ARCH-015** --- Verification result terhubung kembali ke
state/control decision.

**AOF-ARCH-016** --- Architecture dapat mendukung independent
verification sesuai profile.

**AOF-ARCH-017** --- Evidence provenance dapat dipertahankan melintasi
Effect dan Assurance Plane.

AOF-High-Assurance profile MUST menentukan stronger deployment-specific
requirements untuk isolation, integrity, independent verification, trace
protection, dan effect-boundary revalidation.

------------------------------------------------------------------------

## 8.37 Architecture Invariants

Architecture menambahkan invariant family berikut. Numbering final MUST
direkonsiliasi dengan canonical Invariant Registry sebelum v1.0 LTS
freeze.

### ARCH-INV-01 --- Plane Separation

\[ RP\neq CP\neq EP\neq AP\]

### ARCH-INV-02 --- Kernel Mediation

\[ Consequential(x)\Rightarrow MediatedBy(K,x) \]

### ARCH-INV-03 --- No Agent Root of Trust

\[ Agent\not\supset eq GovernanceRoot\]

### ARCH-INV-04 --- Effect Boundary Validation

\[ Effect(x)\Rightarrow ValidControlDecision(x) \]

### ARCH-INV-05 --- State Authority

\[ ConsequentialState\neq UncontrolledAgentPrivateState\]

### ARCH-INV-06 --- State--Trace Coherence

\[ StateChange\Rightarrow TraceRecord\]

### ARCH-INV-07 --- No Implicit Allow

\[ UnknownMandatoryControl\Rightarrow\neg Permit\]

### ARCH-INV-08 --- Revocation Enforcement

\[ Revoked(h)\Rightarrow\neg NewExecutionUsing(h) \]

### ARCH-INV-09 --- Context Non-Authority

\[ ContextContent\not\Rightarrow ControlAuthority\]

### ARCH-INV-10 --- Tool Access Non-Authority

\[ ToolReachability\not\Rightarrow AuthorizedUse\]

### ARCH-INV-11 --- Evidence Return

\[ ConsequentialEffect\Rightarrow ObservableResult\]

sesuai applicable evidence requirements.

### ARCH-INV-12 --- Controlled Concurrency

\[ ConcurrentConsequentialCommit\Rightarrow ConflictControlled\]

------------------------------------------------------------------------

## 8.38 Reference Architectural Sequence

```text
1. Control Plane receives Task
2. Context Manager creates scoped Context Projection
3. Agent is selected using Capability and eligibility
4. Agent receives Task + Context + Governance Envelope
5. Agent reasons
6. Agent returns Proposal
7. Control Plane normalizes candidate Action
8. Safety Kernel evaluates:
      Capability
      Authority
      Policy
      Risk
      State
      Verification requirement
9. Kernel returns Control Outcome
10. If Permit:
      Effect Boundary revalidates applicable conditions
11. Execution Gateway invokes Resource
12. Resource returns Result + Effect Evidence
13. Assurance Plane evaluates required Evidence
14. Verification returns Verified / Rejected / Inconclusive
15. Control Plane commits valid State Transition
16. Trace Recorder records governance chain
17. Lifecycle chooses:
      Complete / Continue / Retry / Replan /
      Wait / Escalate / Fail / Abort
```

Implementation MAY optimize sequencing jika semantic guarantees tetap
equivalent.

------------------------------------------------------------------------

## 8.39 Minimal Reference Architecture

Minimum implementation architecture MAY terdiri atas:

```text
Orchestrator
Agent Runtime
Safety Kernel
Execution Gateway
State Store
Trace Store
```

dengan Safety Kernel menyediakan equivalent:

```text
Authority
Policy
Risk
State Validation
Verification Gate
Trace Mediation
```

Minimal architecture bukan berarti minimal security untuk seluruh
deployment. Applicable profile dan domain MAY mensyaratkan additional
components.

------------------------------------------------------------------------

## 8.40 Full Reference Architecture

Full reference architecture SHOULD menyediakan:

```text
Human / Organizational Governance
        |
        v
Orchestrator / Control Plane
        |
        +-- Task Manager
        +-- Agent Registry
        +-- Context Manager
        +-- Safety Kernel
        |     +-- Authority Evaluator
        |     +-- Policy Evaluator
        |     +-- Risk Gate
        |     +-- State Validator
        |     +-- Verification Gate
        |     +-- Trace Recorder
        |
        +-- Approval / Escalation Interface
        |
        +--> Agent Runtime / Reasoning Plane
        |
        +--> Execution Gateway / Effect Plane
        |       +-- Tool Registry
        |       +-- Resource Adapters
        |
        +--> Assurance Plane
        |       +-- Evidence Collector
        |       +-- Verifier(s)
        |       +-- Human Review
        |
        +--> State Store
        +--> Trace Store
        +--> Evidence Store
```

------------------------------------------------------------------------

## 8.41 Architectural Design Consequences

Architecture menghasilkan konsekuensi berikut:

\[ Agent\neq OrchestrationSystem\]

\[ Orchestrator\neq RootAuthority\]

\[ ToolAccess\neq Authority\]

\[ Proposal\neq Decision\]

\[ Permit\neq ExecutionSuccess\]

\[ ExecutionSuccess\neq VerifiedOutcome\]

\[ AgentMemory\neq AuthoritativeState\]

\[ PromptPolicy\neq EnforcedPolicy\]

\[ HumanPresence\neq UnlimitedAuthority\]

------------------------------------------------------------------------

## 8.42 Architecture Freeze Candidate Criteria

Architecture area MAY dinyatakan `Freeze Candidate` jika:

1.  four-plane semantics telah stabil;
2.  Safety Kernel mediation telah stabil;
3.  component responsibilities tidak bertentangan dengan Agent,
    Authority, Policy, Risk, Evidence, Verification, State, atau Trace
    models;
4.  state ownership semantics telah disepakati;
5.  Effect Boundary dan TOCTOU semantics telah disepakati;
6.  revocation propagation telah didefinisikan;
7.  trust boundaries telah didefinisikan;
8.  minimal architecture conformance requirements tersedia;
9.  architecture tetap deployment-neutral;
10. cross-domain review tidak menemukan breaking contradiction.

Status `Freeze Candidate` tidak sama dengan `FROZEN`. Final freeze
dilakukan setelah Authority, Policy, Risk, Assurance, State/Trace,
Security, dan Conformance passes selesai.

------------------------------------------------------------------------

## 8.43 Architecture Formalization Result

Canonical architecture v1.0 RC-Architecture dapat diringkas sebagai:

\[ AOFArchitecture= RP+CP+EP+AP \]

dengan:

\[ CP\supset eq K\]

dan:

\[ K= { AuthorityEvaluator, PolicyEvaluator, StateValidator, RiskGate,
VerificationGate, TraceRecorder } \]

serta:

\[ Proposal \rightarrow GovernanceMediation \rightarrow
Decision \rightarrow EffectBoundary \rightarrow Action
\rightarrow Evidence \rightarrow Verification
\rightarrow StateTransition \rightarrow Trace \]

Architectural safety property utama:

\[
\boxed{ No\ Consequential\ Effect\ Without\ Governed\ Control }
\]

Architectural accountability property utama:

\[
\boxed{ No\ Consequential\ State\ Change\ Without\ Traceable\ Transition }
\]

Architectural autonomy property utama:

\[ \boxed{ Agent\ Autonomy\subset eq Governance\ Envelope } \]
# 9. Orchestration Lifecycle

## 9.1 Purpose

`Orchestration Lifecycle` mendefinisikan canonical governed runtime flow
AOF dari request intake sampai terminal Outcome. Lifecycle MUST
mengintegrasikan Reasoning, governance evaluation, Effect execution,
Verification, State transition, Human Governance, Failure & Recovery,
dan Trace.

Canonical control loop:

\[
Observe\rightarrow Reason\rightarrow Propose\rightarrow Govern\rightarrow Act\rightarrow Verify\rightarrow Update
\]

Lifecycle tidak boleh mengubah proposal menjadi consequential effect
tanpa governed transition.

\[ Proposal\not\Rightarrow Action\]

\[ ConsequentialAction\Rightarrow GovernedTransition\]

------------------------------------------------------------------------

## 9.2 Orchestration Session

Canonical session:

\[ \omega= \langle
id,request,goal,tasks,context,agents,state,risk,evidence,trace,outcome
\rangle\]

Session merupakan governed execution scope yang mengikat Goal, Task
graph, Context, Agent assignments, Authority/Policy evaluation, Risk,
Evidence, Verification, State, dan Trace.

------------------------------------------------------------------------

## 9.3 Session States

Canonical session states:

-   `Received`
-   `Qualified`
-   `Planning`
-   `Ready`
-   `Running`
-   `Waiting`
-   `Verifying`
-   `Containing`
-   `Reconciling`
-   `Recovering`
-   `Escalated`
-   `Completed`
-   `Failed`
-   `Rejected`
-   `Aborted`
-   `Cancelled`

`Containing`, `Reconciling`, dan `Recovering` mengintegrasikan Failure &
Recovery semantics sebagai first-class lifecycle states.

------------------------------------------------------------------------

## 9.4 Canonical Phases

\[ L= { Intake, Qualification, Planning, Control, Execution,
Verification, Resolution, Termination } \]

Reference flow:

```text
Intent
  -> Intake
  -> Qualification
  -> Planning
  -> Task Preparation
  -> Assignment
  -> Reasoning
  -> Proposal
  -> Governance Evaluation
  -> Execution
  -> Effect Evidence
  -> Verification
  -> State Update
  -> Resolution
  -> Termination Evaluation
```

Failure dapat memasukkan governed recovery path tanpa keluar dari
lifecycle.

------------------------------------------------------------------------

## 9.5 Intake

`Intake` menerima request:

\[ q=\langle intent,context_0,goal\rangle\]

Intake SHOULD establish:

-   request identity;
-   requester identity jika applicable;
-   initial Intent;
-   initial Goal;
-   initial Context;
-   initial governance scope;
-   initial Trace correlation.

Request MUST NOT dianggap executable hanya karena berhasil diterima.

------------------------------------------------------------------------

## 9.6 Qualification

Qualification menentukan apakah request sufficiently defined dan
governable.

Qualification SHOULD evaluate:

-   Goal clarity;
-   applicable constraints;
-   Context sufficiency;
-   obvious Policy conflict;
-   obvious Authority boundary;
-   initial Risk;
-   required Human Governance involvement;
-   feasibility of controlled execution.

Possible result:

`Qualified`, `Waiting`, `Rejected`, atau `Escalated`.

------------------------------------------------------------------------

## 9.7 Goal Integrity During Qualification

Qualification MAY meminta refinement, tetapi MUST preserve governing
Intent.

\[ QualificationRefinement\not\Rightarrow IntentMutation
\]

Material Goal change MUST mengikuti Human Governance rules.

------------------------------------------------------------------------

## 9.8 Planning

Planning menghasilkan candidate execution plan dan Task graph.

\[
Plan=\langle Tasks,Dependencies,Assignments,Controls,Verification,Recovery\rangle
\]

Plan adalah proposal sampai governance validation selesai.

\[ PlanProposal\neq AuthorizedExecutionPlan\]

------------------------------------------------------------------------

## 9.9 Task Graph

Task dependencies SHOULD membentuk explicit dependency structure.

Untuk DAG-based plan:

\[ G_T=(T,E) \]

dengan edge:

\[ (t_i,t_j)\in E\]

berarti (t_j) bergantung pada completion/postcondition (t_i).

Cycle MAY digunakan hanya jika loop semantics explicit, bounded, dan
controlled.

------------------------------------------------------------------------

## 9.10 Plan Validation

Sebelum `Ready`, plan SHOULD divalidasi terhadap:

-   Goal;
-   constraints;
-   dependency consistency;
-   Resource availability;
-   Capability;
-   Authority feasibility;
-   Policy;
-   Risk;
-   required Verification;
-   Human approval requirements;
-   recovery strategy;
-   termination conditions.

Unknown mandatory governance condition menghasilkan `Pending`/`Waiting`,
bukan implicit permit.

------------------------------------------------------------------------

## 9.11 Task Lifecycle

Canonical Task states:

-   `Created`
-   `Qualified`
-   `Ready`
-   `Assigned`
-   `Executing`
-   `Waiting`
-   `Verifying`
-   `Completed`
-   `Failed`
-   `Rejected`
-   `Escalated`
-   `Cancelled`

Recovery-related substate MAY include `Containing`, `Reconciling`, atau
`Recovering` jika implementation memodelkannya pada Task level.

Undefined transition MUST ditolak.

------------------------------------------------------------------------

## 9.12 Task Readiness

Task dapat menjadi `Ready` hanya jika applicable preconditions
satisfied.

Reference predicate:

\[ Ready(t)= PreconditionsSatisfied(t) \land
DependenciesSatisfied(t) \land ContextSufficient(t)
\land NoKnownBlockingState(t) \]

`Ready` belum berarti Action authorized.

------------------------------------------------------------------------

## 9.13 Assignment

Assignment mengikat Task ke candidate Agent.

\[ Assign(t,a) \]

MUST mempertimbangkan applicable Agent Requirements dan tidak boleh
menggunakan Capability sebagai substitute untuk Authority.

Final Agent eligibility didefinisikan lebih lanjut pada Section 10.

------------------------------------------------------------------------

## 9.14 Execution Contract

Sebelum consequential execution, implementation SHOULD establish
`Execution Contract` atau equivalent binding yang mencakup:

-   Task;
-   Agent;
-   operation;
-   target;
-   parameters;
-   Authority reference;
-   Policy context;
-   Risk;
-   required Verification;
-   State reference/version;
-   expected effect;
-   expiry/validity jika applicable.

\[ ExecutionContract\neq AuthorityGrant\]

------------------------------------------------------------------------

## 9.15 Reasoning

Reasoning Plane MAY menggunakan LLM, deterministic logic, Human
reasoning, search, planning, atau techniques lain.

Reasoning menghasilkan candidate proposal.

\[ reason(a,t,c)\rightarrow proposal\]

Reasoning MUST NOT secara sendiri menciptakan execution permission.

------------------------------------------------------------------------

## 9.16 Proposal

Canonical proposal SHOULD bind:

-   actor;
-   Task;
-   proposed operation;
-   target;
-   parameters;
-   assumptions;
-   expected effect;
-   relevant Evidence;
-   State reference;
-   Risk estimate jika applicable.

Default trust:

\[ AgentOutput=UntrustedProposal \]

------------------------------------------------------------------------

## 9.17 Governance Evaluation

Proposal consequential MUST melewati applicable governance evaluation.

Canonical pre-execution predicate:

\[ ExecuteAllowed=
C\land H\land P\land S\land R\land V
\]

dengan:

-   \(C\) = Capability valid;
-   \(H\) = Authority valid;
-   \(P\) = Policy satisfied;
-   \(S\) = State valid;
-   \(R\) = Risk acceptable;
-   \(V\) = required pre-execution Verification/Approval condition
    satisfied.

Human Governance requirement MAY menjadi bagian dari applicable
Authority, Policy, Risk, atau Verification/Approval gate.

------------------------------------------------------------------------

## 9.18 Three-Valued Governance Result

Mandatory control evaluation SHOULD menggunakan:

\[ GateResult\in{Pass,Fail,Pending} \]

Semantics:

-   `Pass` --- applicable condition satisfied;
-   `Fail` --- condition violated;
-   `Pending` --- required fact/control result unresolved.

\[ Pending\neq Pass\]

Unknown mandatory value MUST NOT become implicit `Pass`.

------------------------------------------------------------------------

## 9.19 Governance Decision

Governance evaluation menghasilkan explicit Decision.

Possible Decision types mencakup:

-   `execute`
-   `verify`
-   `approve`
-   `wait`
-   `retry`
-   `replan`
-   `escalate`
-   `reject`
-   `abort`
-   `terminate`

Decision MUST bind ke relevant proposal, State, Authority, Policy, Risk,
dan applicable Evidence.

------------------------------------------------------------------------

## 9.20 Human Approval Gate

Jika applicable profile/policy mensyaratkan Human approval, lifecycle
MUST enter `Waiting` atau equivalent until:

-   valid approval received;
-   request rejected;
-   approval expired;
-   authorized alternate path selected;
-   escalation;
-   valid Break-Glass path;
-   cancellation/abort.

\[ HumanUnavailable\not\Rightarrow Approved\]

------------------------------------------------------------------------

## 9.21 Pre-Execution State Revalidation

Sebelum crossing Effect Boundary, implementation MUST memastikan
Decision masih valid terhadap current authoritative State.

\[ DecisionAt(s_i)\not\Rightarrow ValidAt(s_j) \]

jika material State berubah.

Stale Decision SHOULD menghasilkan reevaluation, `Pending`, `Replan`,
atau rejection.

------------------------------------------------------------------------

## 9.22 TOCTOU Control

Time-of-check/time-of-use gap antara governance evaluation dan effect
execution MUST dikendalikan sesuai risk.

Controls MAY mencakup:

-   version binding;
-   optimistic concurrency;
-   leases;
-   locks;
-   short-lived authorization;
-   target identity binding;
-   atomic gateway evaluation.

------------------------------------------------------------------------

## 9.23 Authority Revocation Before Effect

Jika applicable Authority revoked/suspended/expired sebelum effect
commit:

\[ AuthorityInvalid\Rightarrow\neg ExecuteAllowed\]

Execution MUST NOT proceed berdasarkan stale grant.

------------------------------------------------------------------------

## 9.24 Effect Boundary

Consequential Action MUST cross controlled Effect Boundary.

\[ Decision \rightarrow EffectBoundary
\rightarrow Action \]

Effect Boundary SHOULD bind:

-   authorized actor;
-   operation;
-   target;
-   parameters;
-   State version;
-   governance Decision;
-   applicable validity window.

------------------------------------------------------------------------

## 9.25 Execution

Execution invokes Resource/Tool/environment.

\[
invoke(a,r,x)\rightarrow\langle y,effect,evidence\rangle
\]

Execution result MUST distinguish response/output dari actual effect.

\[ ToolResponse\neq ProvenEffect\]

------------------------------------------------------------------------

## 9.26 Effect Evidence

Consequential execution SHOULD produce effect Evidence sufficient untuk
menentukan what happened.

Possible evidence:

-   transaction identifier;
-   system response;
-   state observation;
-   artifact hash;
-   deployment status;
-   log/event;
-   independent read-back.

Absence of expected response MUST NOT automatically imply absence of
effect.

------------------------------------------------------------------------

## 9.27 Post-Execution State

Setelah Action, system MUST reconcile observed effect dengan
authoritative State.

\[ ActionEffect \rightarrow StateEvaluation \rightarrow
ControlledStateTransition \]

Silent consequential State mutation dilarang.

------------------------------------------------------------------------

## 9.28 Verification Entry

Jika claim/outcome memerlukan Verification, lifecycle enters
`Verifying`.

Verification MUST evaluate claim terhadap criteria dan Evidence.

\[
V:\langle claim,evidence,criteria\rangle\rightarrow result
\]

------------------------------------------------------------------------

## 9.29 Verification Results

Canonical result:

\[ VerificationResult\in { Verified, Rejected, Inconclusive } \]

`Inconclusive` MUST NOT diperlakukan sebagai `Verified`.

------------------------------------------------------------------------

## 9.30 Verified Result

`Verified` MAY satisfy applicable assurance gate jika:

-   verifier eligible;
-   criteria applicable;
-   Evidence sufficient;
-   independence requirement satisfied;
-   result fresh untuk current subject/version.

Verified result tidak otomatis berarti entire Goal completed.

------------------------------------------------------------------------

## 9.31 Rejected Verification

`Rejected` menunjukkan claim gagal terhadap criteria.

Possible lifecycle transitions:

-   `Failed`;
-   `Replan`;
-   `Retry` jika eligible;
-   `Escalated`;
-   `Rejected`;
-   `Aborted`.

System MUST NOT silently convert rejection menjadi success.

------------------------------------------------------------------------

## 9.32 Inconclusive Verification

`Inconclusive` berarti assurance belum cukup untuk acceptance/rejection.

Possible transitions:

-   obtain additional Evidence;
-   independent Verification;
-   `Waiting`;
-   `Replan`;
-   `Escalated`;
-   `Failed` jika required assurance cannot be established.

\[ Inconclusive\neq Pass\]

------------------------------------------------------------------------

## 9.33 Resolution Phase

`Resolution` menentukan next governed state setelah
execution/verification.

Resolution MAY select:

-   continue next Task;
-   complete Task;
-   wait;
-   retry;
-   replan;
-   contain;
-   reconcile;
-   recover;
-   escalate;
-   reject;
-   abort;
-   terminate.

------------------------------------------------------------------------

## 9.34 Failure Detection

Failure MAY berasal dari:

-   Agent;
-   Tool/Resource;
-   Authority;
-   Policy;
-   Risk;
-   State;
-   Verification;
-   Evidence;
-   Human Governance;
-   Security;
-   infrastructure.

Failure detection MUST NOT itself grant permission untuk bypass
controls.

\[ Failure\neq PermissionToBypassControl\]

------------------------------------------------------------------------

## 9.35 Failed Action and Effect Uncertainty

AOF MUST distinguish:

\[ FailedAction\not\Rightarrow NoEffect\]

dan:

\[ PartialEffect\not\Rightarrow NoEffect\]

Jika effect unknown/partial, lifecycle SHOULD enter `Containing` atau
`Reconciling` sebelum retry.

------------------------------------------------------------------------

## 9.36 Containment

Containment bertujuan membatasi further harm/effect.

Possible containment:

-   stop additional Actions;
-   revoke temporary Authority;
-   isolate Resource;
-   disable Agent/tool path;
-   freeze affected Task;
-   preserve Evidence;
-   escalate.

Containment MUST tetap governed.

------------------------------------------------------------------------

## 9.37 Reconciliation

Reconciliation menentukan actual external/system state setelah
uncertain, partial, atau conflicting effect.

\[ ExpectedState\neq ObservedState\Rightarrow Reconcile
\]

Reconciliation SHOULD menghasilkan updated Evidence dan authoritative
State decision.

------------------------------------------------------------------------

## 9.38 Risk Reassessment After Failure

Material failure, partial effect, security event, atau unexpected state
SHOULD trigger Risk reassessment.

\[ MaterialFailure\Rightarrow ReassessRisk\]

Old Risk decision MUST NOT assumed valid jika underlying conditions
berubah materially.

------------------------------------------------------------------------

## 9.39 Retry Eligibility

Retry bukan default response.

\[ RetryEligible= RetryableFailure \land BudgetAvailable
\land StateSafe \land AuthorityValid \land
PolicyValid \land RiskAcceptable \]

Jika prior effect unknown, retry SHOULD wait for reconciliation unless
operation is demonstrably safe/idempotent under applicable semantics.

------------------------------------------------------------------------

## 9.40 Retry Budget

Retry SHOULD bounded oleh:

-   attempt count;
-   time;
-   cost;
-   Risk;
-   effect exposure;
-   policy.

Unbounded retry/livelock dilarang untuk controlled workflow.

------------------------------------------------------------------------

## 9.41 Replan

`Replan` menghasilkan revised plan karena assumptions, State, Risk,
constraints, or results changed.

Replan MUST re-enter applicable governance evaluation.

\[ Replan\not\Rightarrow PreserveOldPermit\]

Material plan change MAY invalidate prior Human approval.

------------------------------------------------------------------------

## 9.42 Recovery

Recovery attempts to restore acceptable operational condition.

Recovery MAY include:

-   retry;
-   compensation;
-   alternative Resource;
-   alternate Agent;
-   rollback where semantically valid;
-   forward recovery;
-   manual intervention.

Recovery Action MUST memiliki independent governance eligibility.

------------------------------------------------------------------------

## 9.43 Compensation

Compensation tidak selalu exact rollback.

\[ Compensation\neq GuaranteedRollback\]

Compensation SHOULD be modeled sebagai new governed Action dengan own
Authority, Policy, Risk, Evidence, dan Verification.

------------------------------------------------------------------------

## 9.44 Recovery Verification

Recovery MUST NOT dianggap successful hanya karena recovery command
returned success.

Applicable recovery SHOULD be verified.

\[ RecoverySuccess \Rightarrow
RequiredRecoveryVerificationSatisfied \]

------------------------------------------------------------------------

## 9.45 Escalation

Escalation packages unresolved decision kepada authorized Human/system
governance path.

Escalation SHOULD include:

-   subject;
-   current State;
-   unresolved condition;
-   Risk;
-   Evidence;
-   attempted actions;
-   relevant Authority/Policy;
-   recommended options;
-   deadline jika applicable.

\[ Escalated\neq Resolved\]

------------------------------------------------------------------------

## 9.46 Break-Glass Path

Break-Glass MAY digunakan hanya melalui Section 17 Human Governance
semantics.

\[ BreakGlass\neq UnlimitedAuthority\]

Break-Glass Action tetap subject to applicable non-overridable controls,
Effect Boundary, Evidence, State, dan Trace.

------------------------------------------------------------------------

## 9.47 Cancellation

`Cancelled` berarti workflow dihentikan berdasarkan valid cancellation
Decision.

Cancellation tidak otomatis membatalkan already committed effects.

\[ Cancel\neq Rollback\]

------------------------------------------------------------------------

## 9.48 Abort

`Aborted` berarti controlled termination karena continuation tidak aman,
tidak valid, atau tidak diizinkan.

Abort MAY require containment/reconciliation sebelum terminal state jika
prior effects unresolved.

------------------------------------------------------------------------

## 9.49 Rejection

`Rejected` menunjukkan request/Task/plan tidak diterima untuk
progression.

Rejection MAY berasal dari:

-   invalid Goal/request;
-   explicit Policy Deny;
-   insufficient Authority;
-   unacceptable Risk;
-   rejected approval;
-   failed mandatory criteria.

Rejected item MUST NOT re-enter execution tanpa new valid transition.

------------------------------------------------------------------------

## 9.50 Successful Completion

Successful completion valid hanya jika:

\[ GoalSatisfied \land RequiredVerificationSatisfied
\land NoBlockingTask \land NoUnresolvedCriticalRisk
\land StateConsistent \land TraceComplete \]

dan applicable Human Governance obligations satisfied.

Semua Tasks `Completed` tidak otomatis berarti Goal satisfied.

------------------------------------------------------------------------

## 9.51 Failed Termination

Session MAY terminate `Failed` jika Goal tidak tercapai dan no valid
continuation/recovery path remains.

Failure MUST preserve known effect/evidence/state semantics.

------------------------------------------------------------------------

## 9.52 Terminal Outcome

Canonical Outcome:

\[ o= \langle status, goalState, results, evidence,
verification, residualRisk, state, trace \rangle\]

Terminal status SHOULD distinguish at least:

-   `Completed`
-   `Failed`
-   `Rejected`
-   `Aborted`
-   `Cancelled`

------------------------------------------------------------------------

## 9.53 No Successful Termination With Pending Mandatory Assurance

\[ MandatoryVerification=Pending \Rightarrow
\neg Completed\]

\[ MandatoryVerification=Inconclusive \Rightarrow
\neg Completed\]

kecuali applicable governance explicitly defines a different legitimate
terminal classification yang bukan false success.

------------------------------------------------------------------------

## 9.54 Concurrency

Independent Tasks MAY execute concurrently jika:

-   dependencies permit;
-   Resources compatible;
-   State semantics safe;
-   Authority/Policy permit;
-   Risk acceptable.

Concurrency MUST NOT weaken governance gates.

------------------------------------------------------------------------

## 9.55 State Conflict

Concurrent conflicting transitions MUST be detected.

Possible resolution:

-   reject stale transition;
-   retry evaluation;
-   serialize;
-   reconcile;
-   escalate.

Last-write-wins SHOULD NOT digunakan untuk consequential governance
state tanpa explicit safe semantics.

------------------------------------------------------------------------

## 9.56 Decision Freshness

Decision validity MAY depend on:

-   State version;
-   Authority validity;
-   Policy version;
-   Risk assessment;
-   Evidence freshness;
-   approval version;
-   target identity.

Material dependency change SHOULD invalidate/re-evaluate Decision.

------------------------------------------------------------------------

## 9.57 Waiting State

`Waiting` digunakan jika progression memerlukan external condition
seperti:

-   Evidence;
-   Resource;
-   Human approval;
-   Authority;
-   Policy resolution;
-   dependency completion;
-   verification result.

Waiting MUST preserve enough State/Trace untuk safe resumption.

------------------------------------------------------------------------

## 9.58 Resume

Resume dari `Waiting`, `Escalated`, atau recovery state MUST revalidate
stale governance dependencies sebelum execution.

\[ Resume\not\Rightarrow ReuseStalePermit\]

------------------------------------------------------------------------

## 9.59 Dynamic Risk

Risk MAY berubah selama lifecycle.

\[ Risk\_{t_0}\neq Risk\_{t_1} \]

Material Risk increase SHOULD trigger stronger controls, additional
Verification, Human approval, containment, atau escalation sesuai
profile.

------------------------------------------------------------------------

## 9.60 Dynamic Authority

Authority MAY be granted, suspended, revoked, expire, atau consumed
selama session.

Lifecycle MUST evaluate current effective Authority, bukan only initial
Authority snapshot.

------------------------------------------------------------------------

## 9.61 Dynamic Policy

Policy change MAY invalidate pending Decision.

Implementation SHOULD define policy-version binding dan reevaluation
semantics.

\[ PolicyChange\Rightarrow ReevaluateApplicablePendingDecision\]

jika change material.

------------------------------------------------------------------------

## 9.62 Evidence Freshness During Lifecycle

Evidence MAY become stale.

Required Evidence freshness SHOULD be evaluated at decision/verification
point, bukan hanya saat collection.

------------------------------------------------------------------------

## 9.63 Human Governance During Lifecycle

Human MAY participate sebagai:

-   governance root;
-   Goal owner;
-   approver;
-   verifier;
-   executor;
-   risk acceptor;
-   escalation recipient;
-   override actor;
-   Break-Glass actor.

Human participation MUST mengikuti Section 17 dan tidak automatically
bypass Safety Kernel.

------------------------------------------------------------------------

## 9.64 Security Events During Lifecycle

Security event MAY force:

-   containment;
-   Authority revocation;
-   Context restriction;
-   Agent isolation;
-   Tool disablement;
-   risk escalation;
-   Evidence preservation;
-   incident escalation;
-   abort.

Security response MUST maintain governed State and Trace where feasible.

------------------------------------------------------------------------

## 9.65 Safety Kernel Failure

Mandatory Safety Kernel component failure MUST fail controlled.

\[ MandatoryControlFailure \Rightarrow
\neg ImplicitPermit\]

Possible result:

-   `Pending`;
-   `Waiting`;
-   `Escalated`;
-   `Aborted`;
-   safe degraded mode if explicitly defined.

------------------------------------------------------------------------

## 9.66 Deadlock

Lifecycle SHOULD detect deadlock where Tasks/control dependencies cannot
progress.

Resolution MAY include:

-   replan;
-   release safe Resource;
-   escalation;
-   abort.

Deadlock resolution MUST NOT bypass Authority/Policy.

------------------------------------------------------------------------

## 9.67 Livelock

Repeated transitions tanpa meaningful progress SHOULD be detected.

Retry/replan budgets SHOULD prevent unbounded livelock.

------------------------------------------------------------------------

## 9.68 Progress and Liveness

AOF seeks liveness subject to safety/governance constraints.

\[ Liveness\not\Rightarrow PermissionToViolateSafety\]

If safe progression impossible, controlled termination is valid.

------------------------------------------------------------------------

## 9.69 Transition Semantics

Every consequential transition SHOULD be representable as:

\[ Transition= Decision + StateChange + TraceRecord \]

Jika Action occurred:

\[ Transition= Decision + Action + Evidence + StateChange + TraceRecord
\]

------------------------------------------------------------------------

## 9.70 Transition Authorization

State transition itself MAY require Authority/Policy evaluation jika
transition changes consequential governance state.

No component MAY silently mutate authoritative State outside defined
transition path.

------------------------------------------------------------------------

## 9.71 Trace Correlation

Lifecycle MUST preserve correlation across:

-   session;
-   Goal;
-   Task;
-   proposal;
-   Decision;
-   Action;
-   Evidence;
-   Verification;
-   State transition;
-   Outcome.

Correlation enables accountability reconstruction.

------------------------------------------------------------------------

## 9.72 Lifecycle Observability

Conformant implementation SHOULD expose observable lifecycle state
without requiring private Chain-of-Thought.

Required observability concerns events/decisions/effects, bukan hidden
reasoning tokens.

------------------------------------------------------------------------

## 9.73 Deterministic Controls

Where practical, mandatory governance predicates SHOULD use
deterministic evaluation.

LLM output MAY assist interpretation but MUST NOT become sole implicit
authority source.

\[ ProbabilisticReasoning\neq ProbabilisticPermission\]

------------------------------------------------------------------------

## 9.74 Performance and Control Budget

Implementation MAY optimize governance latency melalui:

-   local deterministic evaluation;
-   safe caching;
-   precomputation;
-   batched checks;
-   colocated Policy/Authority evaluation;
-   bounded parallel evaluation.

Tetapi:

\[ PerformanceOptimization \not\Rightarrow
GovernanceWeakening \]

AOF tidak menetapkan universal sub-millisecond latency requirement.
Deployment/Profile MAY menetapkan `ControlLatencyBudget` sesuai
operational context.

------------------------------------------------------------------------

## 9.75 Control Evaluation Parallelism

Independent governance predicates MAY dievaluasi parallel jika semantics
dan authoritative inputs preserved.

Conceptually:

\[ ControlLatency\approx max(L_C,L_H,L_P,L_S,L_R,L_V) \]

untuk safely parallelizable checks, bukan necessarily sum seluruh
latency.

Parallelism MUST NOT introduce inconsistent snapshots atau stale
decisions.

------------------------------------------------------------------------

## 9.76 Lifecycle Requirements

**AOF-LC-001** --- Consequential Action MUST require explicit governed
transition.

**AOF-LC-002** --- Proposal MUST NOT be treated as authorized Decision
solely because it was generated by an Agent.

**AOF-LC-003** --- Unknown/Pending mandatory governance result MUST NOT
become implicit permit.

**AOF-LC-004** --- Pre-execution Decision MUST be revalidated when
material State/governance dependency changes.

**AOF-LC-005** --- Consequential execution MUST cross controlled Effect
Boundary or equivalent enforcement point.

**AOF-LC-006** --- Execution SHOULD produce sufficient effect Evidence
for applicable assurance/reconciliation.

**AOF-LC-007** --- `Inconclusive` mandatory Verification MUST NOT be
treated as successful Verification.

**AOF-LC-008** --- Failure MUST NOT authorize bypass of mandatory
governance controls.

**AOF-LC-009** --- Unknown/partial effect SHOULD be reconciled before
unsafe retry.

**AOF-LC-010** --- Retry MUST be bounded dan governance-eligible.

**AOF-LC-011** --- Replan MUST re-evaluate applicable governance
controls.

**AOF-LC-012** --- Recovery Action MUST be independently eligible for
execution.

**AOF-LC-013** --- Cancellation MUST NOT be represented as rollback
unless committed effects were actually reversed.

**AOF-LC-014** --- Successful termination MUST require Goal satisfaction
and applicable assurance satisfaction.

**AOF-LC-015** --- Consequential State mutation MUST occur through
controlled transition.

**AOF-LC-016** --- Resume MUST revalidate stale governance dependencies.

**AOF-LC-017** --- Mandatory Safety Kernel failure MUST NOT fail open.

**AOF-LC-018** --- Lifecycle MUST preserve traceable correlation across
consequential control/effect events.

**AOF-LC-019** --- Human unavailability MUST NOT become implicit
approval.

**AOF-LC-020** --- Performance optimization MUST NOT weaken mandatory
governance semantics.

**AOF-LC-021** --- Dynamic Authority revocation/expiry MUST be respected
before subsequent consequential effect.

**AOF-LC-022** --- Material Risk change SHOULD trigger applicable
control reassessment.

**AOF-LC-023** --- Concurrent consequential transitions MUST detect
applicable State conflicts.

**AOF-LC-024** --- Terminal Outcome MUST preserve residual Risk,
Evidence, Verification, State, dan Trace references as applicable.

------------------------------------------------------------------------

## 9.77 Lifecycle Invariants

### LC-INV-01 --- Proposal Non-Authority

\[ Proposal\not\Rightarrow Action\]

### LC-INV-02 --- Governed Effect

\[ ConsequentialEffect\Rightarrow GovernedTransition\]

### LC-INV-03 --- Pending Non-Permit

\[ Pending\neq Pass\]

### LC-INV-04 --- State Freshness

\[ MaterialStateChange\Rightarrow ReevaluateDecision\]

### LC-INV-05 --- Verification Integrity

\[ Inconclusive\neq Verified\]

### LC-INV-06 --- Failure Non-Bypass

\[ Failure\neq PermissionToBypassControl\]

### LC-INV-07 --- Effect Honesty

\[ FailedAction\not\Rightarrow NoEffect\]

### LC-INV-08 --- Retry Governance

\[ Retry\Rightarrow ReevaluateEligibility\]

### LC-INV-09 --- Replan Governance

\[ Replan\not\Rightarrow PreserveOldPermit\]

### LC-INV-10 --- Recovery Governance

\[ RecoveryAction\Rightarrow GovernedAction\]

### LC-INV-11 --- Cancellation Honesty

\[ Cancel\neq Rollback\]

### LC-INV-12 --- Successful Termination

\[
Completed\Rightarrow GoalSatisfied\land RequiredAssuranceSatisfied
\]

### LC-INV-13 --- Transition Traceability

\[ ConsequentialTransition\Rightarrow TraceRecord\]

### LC-INV-14 --- Resume Freshness

\[ Resume\not\Rightarrow ReuseStalePermit\]

### LC-INV-15 --- Fail-Controlled Kernel

\[ MandatoryControlFailure\Rightarrow\neg ImplicitPermit
\]

### LC-INV-16 --- Human Approval Integrity

\[ HumanUnavailable\not\Rightarrow Approved\]

------------------------------------------------------------------------

## 9.78 Reference Lifecycle Conformance Tests

### CT-LC-001 --- Pending Governance

Given one mandatory gate returns `Pending`:

Expected: consequential execution blocked.

### CT-LC-002 --- Stale Decision

Given State changes materially after permit but before Effect Boundary:

Expected: reevaluation; stale Decision MUST NOT execute unchanged.

### CT-LC-003 --- Inconclusive Verification

Given mandatory Verification returns `Inconclusive`:

Expected: session MUST NOT terminate `Completed`.

### CT-LC-004 --- Partial Effect Retry

Given Action returns failure while effect status unknown:

Expected: reconcile/contain before unsafe retry.

### CT-LC-005 --- Revoked Authority

Given Authority revoked after planning and before effect:

Expected: execution blocked.

### CT-LC-006 --- Replan

Given plan materially changes:

Expected: governance re-evaluation and applicable approval freshness
evaluation.

### CT-LC-007 --- Cancellation

Given already committed external effect then session cancelled:

Expected: cancellation MUST NOT falsely record effect as rolled back.

### CT-LC-008 --- Safety Kernel Failure

Given mandatory governance component unavailable:

Expected: no implicit execution permit.

### CT-LC-009 --- Concurrent State Conflict

Given two conflicting transitions use same stale State version:

Expected: conflict detection/rejection/reconciliation.

### CT-LC-010 --- Human Approval Timeout

Given mandatory Human approval expires/unavailable:

Expected: no implicit approval.

------------------------------------------------------------------------

## 9.79 Cross-Domain Lifecycle Matrix

  Lifecycle Concern              Primary AOF Domain
  ------------------------------ --------------------------------
  Proposal/Decision separation   Architecture, Agent, Lifecycle
  Capability                     Agent
  Authority                      Authority Model
  Policy                         Policy Model
  Risk                           Risk Model
  Evidence                       Evidence
  Verification                   Verification
  State consistency              State & Trace
  Human approval/override        Human Governance
  Failure containment/recovery   Failure & Recovery
  Effect security                Security
  Conformance                    Conformance
  Machine representation         Schemas

------------------------------------------------------------------------

## 9.80 Freeze Candidate Criteria

Section 9 MAY dinyatakan `Freeze Candidate` jika:

1.  canonical phases consistent dengan Architecture;
2.  Task/Session states consistent dengan State & Trace;
3.  governance evaluation consistent dengan Authority, Policy, Risk,
    Verification, dan Human Governance;
4.  Effect Boundary consistent dengan Security;
5.  Verification results `Verified/Rejected/Inconclusive` integrated;
6.  Failure states `Containing/Reconciling/Recovering` integrated;
7.  retry/replan/recovery semantics consistent dengan Failure &
    Recovery;
8.  dynamic Authority/Policy/Risk revalidation defined;
9.  concurrency/TOCTOU/state conflict semantics integrated;
10. successful termination semantics consistent dengan Verification and
    Outcome;
11. requirements/invariants have conformance hooks;
12. no private Chain-of-Thought requirement introduced;
13. lifecycle remains model/tool/platform agnostic;
14. cross-domain review menemukan no breaking contradiction.

------------------------------------------------------------------------

## 9.81 Lifecycle Formalization Result

Canonical lifecycle:

\[ Observe \rightarrow Reason \rightarrow Propose
\rightarrow Govern \rightarrow Act \rightarrow
Verify \rightarrow Update \]

dengan recovery branch:

\[ Failure \rightarrow Contain \rightarrow Reconcile
\rightarrow ReassessRisk \rightarrow

\begin{cases}
Retry\\
Replan\\
Recover\\
Escalate\\
Abort
\end{cases}
\rightarrow
VerifyRecovery \]

dan safety property:

\[
\boxed{ No\ Consequential\ Action\ Without\ Governed\ Transition }
\]

assurance property:

\[
\boxed{ No\ Successful\ Termination\ Without\ Goal\ And\ Assurance\ Satisfaction }
\]

state property:

\[
\boxed{ No\ Consequential\ State\ Change\ Without\ Controlled\ Traceable\ Transition }
\]

Section 9 dengan demikian menjadi canonical integration lifecycle untuk
domain Architecture, Authority, Policy, Risk, Evidence, Verification,
State & Trace, Human Governance, Failure & Recovery, Security, dan
Conformance.

------------------------------------------------------------------------

# 10. Agent Requirements

## 10.1 Purpose

Section ini mendefinisikan normative Agent Model AOF dan
merekonsiliasikannya dengan Architecture, Orchestration Lifecycle,
Authority, Policy, Risk, Evidence, Verification, State & Trace, Human
Governance, Failure & Recovery, Security, dan Conformance.

Canonical principle:

\[ Agent=BoundedOperationalActor \]

\[ Agent\neq AutonomousRootOfTrust\]

Agent MAY reason, plan, propose, execute, coordinate, atau verify sesuai
Governance Envelope, tetapi Agent MUST NOT memperoleh permission hanya
dari capability, confidence, role, model intelligence, atau tool access.

------------------------------------------------------------------------

## 10.2 Canonical Agent Object

Canonical Agent:

\[ a= \langle id, type, role, capabilities, authority, context,
memory, trust, policies, riskProfile, state, interface \rangle
\]

Agent representation SHOULD memungkinkan binding ke current
versions/references dari governance objects yang relevan.

------------------------------------------------------------------------

## 10.3 Agent Types

Reference `AgentType`:

-   `LLM`
-   `Deterministic`
-   `Human`
-   `Hybrid`
-   `ExternalService`

Implementation MAY menambahkan type melalui extension mechanism selama
core semantics tidak dilemahkan.

Agent type tidak menentukan Authority.

\[ AgentType\not\Rightarrow Authority\]

------------------------------------------------------------------------

## 10.4 Role

`Role` mendeskripsikan responsibility/function Agent.

Examples:

-   Planner;
-   Developer;
-   Reviewer;
-   Verifier;
-   Security Analyst;
-   Release Operator;
-   Human Approver.

Role MAY membantu selection dan Policy evaluation, tetapi:

\[ Role\neq Capability\]

\[ Role\neq Authority\]

------------------------------------------------------------------------

## 10.5 Multi-Role Agent

Satu Agent MAY memiliki multiple roles jika governance mengizinkan.

Multiple roles MUST NOT digunakan untuk menghindari separation-of-duties
atau verifier independence.

\[
MultipleRoles\not\Rightarrow MultipleIndependentActors
\]

------------------------------------------------------------------------

## 10.6 Capability

Capability adalah kemampuan Agent untuk melakukan class of work.

\[ cap(a)={c_1,c_2,\dots,c_n} \]

Capability MAY berasal dari:

-   model capability;
-   deterministic function;
-   tool integration;
-   Human expertise;
-   external service;
-   composite workflow.

Capability menyatakan ability, bukan permission.

------------------------------------------------------------------------

## 10.7 Capability-Authority Separation

Canonical invariant:

\[ Capability\neq Authority\]

Agent yang mampu melakukan operation belum tentu authorized.

\[ Capable(a,x)\not\Rightarrow Authorized(a,x) \]

------------------------------------------------------------------------

## 10.8 Declared vs Observed Capability

AOF membedakan:

-   `DeclaredCapability` --- capability yang dikonfigurasi/dinyatakan;
-   `ObservedCapability` --- capability yang didukung oleh
    evaluation/operational evidence.

High-risk assignment SHOULD tidak bergantung solely pada unverified
self-declared capability.

------------------------------------------------------------------------

## 10.9 Capability Qualification

Deployment MAY menetapkan qualification criteria untuk capability,
misalnya:

-   test result;
-   benchmark;
-   certification;
-   Human attestation;
-   historical performance;
-   deterministic feature availability.

Qualification Evidence SHOULD memiliki provenance/freshness sesuai risk.

------------------------------------------------------------------------

## 10.10 Authority

Agent Authority berasal dari valid Authority Model.

Agent MUST NOT self-authorize.

\[ SelfDeclaredAuthority\neq EffectiveAuthority\]

Effective Authority MAY berubah karena grant, delegation, suspension,
revocation, expiry, consumption, Policy, State, atau Risk constraints.

------------------------------------------------------------------------

## 10.11 Governance Envelope

Canonical Agent Governance Envelope:

\[ GE_a= \langle Authority, Policy, RiskLimits, ContextScope,
ResourceScope, VerificationRequirements, ApprovalRequirements,
TemporalLimits \rangle\]

Agent operation MUST remain within applicable (GE_a).

\[ Agency(a)\subset eq GE_a \]

------------------------------------------------------------------------

## 10.12 Bounded Autonomy

AOF autonomy adalah bounded operational property.

Higher autonomy MAY reduce per-action Human interaction, tetapi MUST NOT
create governance-root status.

\[
Autonomy\uparrow\not\Rightarrow GovernanceAuthority\uparrow
\]

Autonomy MUST remain constrained oleh Authority, Policy, Risk, State,
Context, Resource scope, dan Verification requirements.

------------------------------------------------------------------------

## 10.13 Reference Autonomy Levels

Reference levels:

-   `AL0 — Advisory`: analyze/recommend only;
-   `AL1 — Assisted`: generate/propose with Human-controlled execution;
-   `AL2 — Bounded Execution`: execute predefined low/moderate-risk
    actions within explicit envelope;
-   `AL3 — Bounded Orchestration`: plan/delegate/execute multi-step
    workflows within governance envelope;
-   `AL4 — Supervised High Autonomy`: broad operational orchestration
    under strong controls, monitoring, assurance, and escalation.

AOF defines no `UnlimitedAutonomy` level.

------------------------------------------------------------------------

## 10.14 Effective Autonomy

\[ EffectiveAutonomy(a)= ConfiguredAutonomy \cap
EffectiveAuthority \cap PolicyPermittedScope \cap
RiskPermittedScope \cap StatePermittedScope \]

Context/Resource/Verification constraints further bound executable
behavior.

------------------------------------------------------------------------

## 10.15 Agent Eligibility

Agent assignment MUST distinguish candidate suitability dari execution
permission.

Reference eligibility:

\[ EligibleAgent(a,t)= CapabilityCompatible(a,t) \land
AuthorityCompatible(a,t) \land PolicyCompatible(a,t)
\land RiskCompatible(a,t) \land ContextCompatible(a,t)
\land StateCompatible(a,t) \]

Jika salah satu mandatory condition unresolved:

\[ EligibleAgent\neq true\]

sampai applicable resolution diperoleh.

------------------------------------------------------------------------

## 10.16 Capability Compatibility

\[ CapabilityCompatible(a,t) \]

berarti Agent memiliki required capabilities untuk Task dengan
sufficient qualification sesuai profile/risk.

Capability matching MAY menggunakan deterministic registry, metadata,
evaluation evidence, atau governed reasoning.

------------------------------------------------------------------------

## 10.17 Authority Compatibility

\[ AuthorityCompatible(a,t) \]

berarti current effective Authority Agent cukup untuk planned
responsibility.

Assignment SHOULD NOT dibuat dengan asumsi bahwa Authority akan otomatis
diberikan setelah selection.

Jika Authority perlu granted, grant harus melalui Authority lifecycle.

------------------------------------------------------------------------

## 10.18 Policy Compatibility

\[ PolicyCompatible(a,t) \]

berarti assignment/operation tidak bertentangan dengan applicable
Policy.

Policy compatibility MAY bergantung pada role, Agent identity/type,
resource, context, time, risk, atau other conditions.

------------------------------------------------------------------------

## 10.19 Risk-Compatible Agent Selection

Agent selection MUST mempertimbangkan Risk ketika Agent characteristics
material terhadap safe execution.

Reference:

\[ RiskCompatible(a,t)= RiskProfile(a) \succeq
RequiredRiskHandling(t) \]

Interpretasi operator (\succeq) ditentukan deployment/profile,
bukan universal numeric ranking.

High/Critical-risk Task SHOULD require stronger qualification, bounded
Authority, observability, assurance, dan recovery characteristics.

------------------------------------------------------------------------

## 10.20 Risk Profile Contract

Agent MAY memiliki `RiskProfile`:

```text
agent_id
permitted_risk_classes
prohibited_operations
required_supervision
required_verification
max_effect_scope
escalation_thresholds
failure_limits
```

Risk Profile MUST NOT grant Authority.

\[ RiskCompatibility\neq AuthorityGrant\]

------------------------------------------------------------------------

## 10.21 Context Compatibility

Agent MUST menerima hanya Context yang legitimate dan necessary untuk
assigned responsibility.

\[ Context_a\subset eq Context\_{available} \]

dan SHOULD mengikuti Context Least Privilege.

Agent selection SHOULD mempertimbangkan whether Agent is
permitted/trusted to receive required Context.

------------------------------------------------------------------------

## 10.22 Context Projection

Orchestrator/Control Plane SHOULD construct bounded `Context Projection`
untuk Agent.

Projection MAY include:

-   Task;
-   Goal;
-   constraints;
-   Evidence;
-   Resource metadata;
-   relevant history;
-   Policy guidance;
-   execution result.

Projection MUST NOT be interpreted sebagai transfer of Authority.

\[ ContextPossession\not\Rightarrow Authority\]

------------------------------------------------------------------------

## 10.23 Context Trust

Context SHOULD carry trust/provenance metadata where material.

External/retrieved/user/tool content MAY be untrusted.

\[ ExternalContent\neq ControlInstruction\]

Untrusted content MUST NOT silently redefine governing Policy,
Authority, or Intent.

------------------------------------------------------------------------

## 10.24 Instruction-Data Separation

Implementation SHOULD distinguish trusted control instructions dari
untrusted task data.

Prompt formatting alone MAY assist separation tetapi MUST NOT be sole
security boundary untuk consequential systems.

------------------------------------------------------------------------

## 10.25 Memory

Agent Memory MAY include:

-   session memory;
-   task memory;
-   episodic memory;
-   durable memory;
-   external knowledge reference.

Memory MUST NOT be treated as Authority source.

\[ Memory\neq Authority\]

------------------------------------------------------------------------

## 10.26 Least Persistence

Agent Memory SHOULD persist only information necessary sesuai purpose,
privacy, security, retention, dan governance requirements.

Sensitive Context SHOULD NOT become durable memory merely because Agent
observed it.

------------------------------------------------------------------------

## 10.27 Memory Freshness

Memory-derived fact MAY become stale.

Material decision SHOULD validate freshness/provenance sesuai
Evidence/Context semantics.

\[ RememberedClaim\neq CurrentVerifiedFact\]

------------------------------------------------------------------------

## 10.28 Trust

Trust adalah contextual assessment, bukan global permission score.

\[ Trust(a,context,task) \]

MAY influence selection, supervision, verification, atau risk treatment.

Trust MUST NOT directly create Authority.

\[ TrustIncrease\not\Rightarrow AuthorityIncrease\]

------------------------------------------------------------------------

## 10.29 Agent Confidence

Self-reported confidence MAY be informative metadata.

\[ Confidence\neq Verification\]

\[ HighConfidence\not\Rightarrow ExecuteAllowed\]

Confidence MUST NOT replace Evidence atau required Verification.

------------------------------------------------------------------------

## 10.30 Selection Hard Constraints

Agent selection SHOULD separate hard constraints dari soft preferences.

Hard constraints MAY include:

-   required Capability;
-   valid Authority;
-   Policy eligibility;
-   Risk compatibility;
-   Context clearance;
-   separation of duties;
-   Resource eligibility;
-   availability if required.

Hard constraint failure MUST NOT be compensated by high model score.

------------------------------------------------------------------------

## 10.31 Selection Soft Criteria

Setelah hard constraints satisfied, selection MAY optimize:

-   quality;
-   latency;
-   cost;
-   reliability;
-   historical success;
-   specialization;
-   locality;
-   resource utilization.

Canonical:

\[ Select(a\^\*)=
\arg\max\_{a\in EligibleAgents} Utility(a,t) \]

Utility optimization MUST NOT weaken hard governance constraints.

------------------------------------------------------------------------

## 10.32 No Cheapest-Agent Override

Lower cost/latency MUST NOT justify selection Agent yang gagal mandatory
eligibility.

\[ CheaperAgent\not\Rightarrow EligibleAgent\]

------------------------------------------------------------------------

## 10.33 Dynamic Re-Selection

Agent MAY become ineligible selama Task karena:

-   Authority revoked;
-   Policy change;
-   Risk change;
-   capability degradation;
-   Agent compromise;
-   Context restriction;
-   Resource change.

Lifecycle SHOULD support controlled re-selection/reassignment.

------------------------------------------------------------------------

## 10.34 Assignment Binding

Assignment SHOULD bind:

-   Task;
-   Agent identity;
-   role;
-   responsibility;
-   capability basis;
-   Authority basis;
-   Context scope;
-   Resource scope;
-   Risk constraints;
-   required Verification;
-   validity.

Assignment MUST NOT silently expand Agent governance envelope.

------------------------------------------------------------------------

## 10.35 Proposal Semantics

Agent output default:

\[ AgentOutput=UntrustedProposal \]

Proposal MAY include plan, answer, code, Decision recommendation, Action
request, Evidence claim, atau delegation request.

Proposal MUST NOT be interpreted as authorized Action solely because
source Agent is trusted/capable.

------------------------------------------------------------------------

## 10.36 Agent Claim

\[ AgentClaim\neq VerifiedFact\]

Agent-generated factual claim MAY become Evidence candidate jika
provenance/content meet Evidence requirements, tetapi claim itself tidak
establish Verification.

------------------------------------------------------------------------

## 10.37 Action Proposal

Consequential Action Proposal SHOULD bind:

-   Agent;
-   Task;
-   operation;
-   target;
-   parameters;
-   State reference;
-   expected effect;
-   assumptions;
-   relevant Evidence;
-   Risk.

Agent MUST NOT encode hidden privilege expansion melalui parameters.

------------------------------------------------------------------------

## 10.38 Agent Decision Participation

Agent MAY recommend Decision.

Only authorized Control Plane/governance mechanism MAY convert proposal
menjadi executable Decision sesuai Architecture.

\[ ReasoningOutput\neq ControlDecision\]

------------------------------------------------------------------------

## 10.39 Agent Execution

Agent MAY initiate execution hanya jika Section 9 governance lifecycle
menghasilkan eligible Decision.

Tool/API availability tidak cukup.

\[ TechnicalAccess\neq Authority\]

------------------------------------------------------------------------

## 10.40 Least Tool Exposure

Agent SHOULD receive only Resources/tools required untuk assigned
responsibility.

Tool exposure SHOULD be bounded by:

-   operation;
-   target;
-   parameter;
-   credential;
-   network;
-   time;
-   task/session.

Broad tool access SHOULD NOT digunakan sebagai substitute untuk proper
Authority mediation.

------------------------------------------------------------------------

## 10.41 Tool Credential Semantics

Possession of credential/token/API key tidak membuktikan governance
Authority.

\[
CredentialPossession\not\Rightarrow GovernanceAuthority
\]

Credential SHOULD be scoped/issued/mediated sesuai least privilege.

------------------------------------------------------------------------

## 10.42 Delegation

Agent MAY delegate Task/responsibility hanya jika delegation permitted.

Delegation MUST preserve:

-   Goal;
-   constraints;
-   Authority bounds;
-   Context bounds;
-   Risk controls;
-   Policy;
-   required Verification;
-   Trace.

------------------------------------------------------------------------

## 10.43 Delegation Authority Conservation

\[ Authority\_{delegatee} \subset eq Authority\_{delegator} \]

untuk Authority yang diturunkan melalui delegation chain, kecuali
independent Authority grant berasal dari separate legitimate issuer.

Delegation MUST NOT create Authority ex nihilo.

------------------------------------------------------------------------

## 10.44 Delegation Context Conservation

Delegatee SHOULD menerima minimum necessary Context.

\[ Context\_{delegatee} \subset eq
PermittedContext\_{delegation} \]

Delegation MUST NOT be used untuk bypass disclosure restrictions.

------------------------------------------------------------------------

## 10.45 Constraint Inheritance

Child Task/delegated responsibility MUST inherit applicable parent
constraints kecuali valid governance change explicitly modifies them.

\[ Constraints(child)\supset eq
MandatoryInheritedConstraints(parent) \]

------------------------------------------------------------------------

## 10.46 No Authority Laundering

Agent MUST NOT use another Agent/tool/service untuk obtain effect yang
tidak authorized melalui original governance path.

\[ DelegationChain\not\Rightarrow PrivilegeExpansion\]

------------------------------------------------------------------------

## 10.47 Recursive Delegation

Recursive delegation SHOULD be bounded by:

-   depth;
-   Authority;
-   time;
-   cost;
-   Risk;
-   Context;
-   policy;
-   Task graph constraints.

Unbounded recursive Agent spawning SHOULD NOT be permitted.

------------------------------------------------------------------------

## 10.48 Result Disclosure Authority

Authority untuk execute Task tidak otomatis memberikan Authority untuk
disclose result kepada arbitrary recipient.

\[ ExecutionAuthority\neq DisclosureAuthority\]

Result routing MUST respect Context/data Policy.

------------------------------------------------------------------------

## 10.49 Agent Interaction Contract

Inter-Agent communication SHOULD menggunakan
`Agent Interaction Contract` atau equivalent structured semantics.

Contract MAY include:

```text
sender
recipient
task
message_type
context_refs
evidence_refs
constraints
authority_refs
expected_response
validity
correlation
```

Message MUST NOT expand Authority merely by asserting it.

------------------------------------------------------------------------

## 10.50 Message Types

Reference message types MAY include:

-   `REQUEST`
-   `PROPOSAL`
-   `RESULT`
-   `EVIDENCE`
-   `VERIFY`
-   `DELEGATE`
-   `ESCALATE`
-   `CONTROL_NOTICE`

Message type is descriptive and MUST NOT override governance semantics.

------------------------------------------------------------------------

## 10.51 Message Provenance

Consequential inter-Agent messages SHOULD preserve:

-   sender identity;
-   recipient;
-   timestamp;
-   correlation;
-   provenance;
-   relevant State/Task reference.

Spoofed/unresolved sender identity SHOULD NOT satisfy identity-dependent
Authority.

------------------------------------------------------------------------

## 10.52 Agent Impersonation

Implementation MUST protect governance-relevant Agent identity dari
spoofing/substitution sesuai Security Profile.

Agent name/string in prompt is not sufficient identity proof untuk
consequential governance.

------------------------------------------------------------------------

## 10.53 Compromised Agent Assumption

Security-sensitive AOF deployment SHOULD assume any individual Agent MAY
become compromised, manipulated, faulty, or adversarial.

Therefore Safety Kernel MUST NOT rely solely on Agent self-restraint.

\[ AgentCompliance\neq SecurityBoundary\]

------------------------------------------------------------------------

## 10.54 Prompt Policy vs Enforcement

Policy embedded dalam Agent prompt MAY guide behavior.

Namun:

\[ PolicyPrompt\neq PolicyEnforcement\]

Mandatory consequential controls SHOULD be enforced outside sole
probabilistic Agent reasoning.

------------------------------------------------------------------------

## 10.55 Agent Sandbox

Execution-capable Agent SHOULD use sandbox/isolation sesuai
Resource/Risk.

Sandbox MAY restrict:

-   filesystem;
-   process;
-   network;
-   credential;
-   environment;
-   package;
-   execution time.

Sandbox does not replace Authority/Policy evaluation.

------------------------------------------------------------------------

## 10.56 Network Access

Network access SHOULD be least privilege.

Unrestricted egress MAY increase Context leakage, tool abuse, prompt
injection, dan supply-chain Risk.

Network policy SHOULD align dengan assigned Task and Resource scope.

------------------------------------------------------------------------

## 10.57 Secrets

Agent SHOULD receive secrets only when necessary dan through controlled
mechanism.

Secret exposure in prompt/memory SHOULD be minimized.

Agent MUST NOT infer Authority from secret possession.

------------------------------------------------------------------------

## 10.58 External Service Agent

ExternalService Agent SHOULD be treated according to trust boundary.

Implementation SHOULD consider:

-   service identity;
-   data disclosure;
-   availability;
-   integrity;
-   jurisdiction;
-   model/service substitution;
-   logging;
-   retention;
-   contractual constraints.

External service response remains subject to AOF Evidence/Verification
semantics.

------------------------------------------------------------------------

## 10.59 Human Agent

Human MAY be represented as `AgentType=Human`.

Human Agent tetap subject to applicable:

-   Authority;
-   Policy;
-   Risk;
-   State;
-   Trace;
-   separation of duties.

\[ HumanPresence\not\Rightarrow UnlimitedAuthority\]

Detailed governance semantics berada di Section 17.

------------------------------------------------------------------------

## 10.60 Hybrid Agent

Hybrid Agent menggabungkan Human, LLM, deterministic component, atau
service.

Implementation MUST identify governance-relevant actor/component
boundary sufficiently untuk accountability.

Composite identity MUST NOT obscure which component made consequential
proposal/action.

------------------------------------------------------------------------

## 10.61 Planner Agent

Planner MAY decompose Goal dan propose Task graph.

Planner MUST NOT assume planning Authority equals execution Authority.

\[ PlanningAuthority\neq ExecutionAuthority\]

Plan remains proposal until governed.

------------------------------------------------------------------------

## 10.62 Orchestrator Agent

Jika Orchestrator diwujudkan sebagai Agent, Orchestrator Agent MUST NOT
menjadi implicit root of Authority.

\[ OrchestratorAgent\neq RootOfTrust\]

Control Plane/Safety Kernel enforcement SHOULD remain independently
governable.

------------------------------------------------------------------------

## 10.63 Supervisor Agent

Supervisor Agent MAY monitor, route, critique, or coordinate.

Supervisor role tidak otomatis grant approval/override Authority.

Supervisor-generated instruction to another Agent MUST remain within
valid governance chain.

------------------------------------------------------------------------

## 10.64 Verifier Agent

Verifier Agent MUST satisfy applicable capability, criteria, Evidence
access, dan independence.

Reference:

\[ VerifierEligible(a,t)= EligibleAgent(a,t) \land
VerificationCapability(a,t) \land IndependenceSatisfied(a,t) \]

------------------------------------------------------------------------

## 10.65 Verification Independence Levels

Reference:

-   `VI0` --- self-check;
-   `VI1` --- same Agent/system, separated pass/context;
-   `VI2` --- independent Agent/model/tool path;
-   `VI3` --- organizationally/technically independent verifier.

Required level ditentukan oleh Verification Profile/Risk.

------------------------------------------------------------------------

## 10.66 Self-Verification Boundary

Self-check MAY improve quality tetapi MUST NOT satisfy independent
Verification requirement.

\[ SelfCheck\neq IndependentVerification\]

Agent MUST NOT mark own output as independently verified jika
independence requirement tidak terpenuhi.

------------------------------------------------------------------------

## 10.67 Circular Verification

Delegation chain MUST NOT create false independence.

Jika Agent A creates output, Agent B nominally verifies tetapi B is
controlled such that independence criteria fail, verification MUST NOT
be represented at stronger independence level.

------------------------------------------------------------------------

## 10.68 Verifier Conflict

Conflicting verifier results SHOULD enter governed resolution:

-   additional Evidence;
-   higher independence;
-   deterministic test;
-   Human review;
-   escalation.

Conflict MUST NOT default to preferred optimistic result.

------------------------------------------------------------------------

## 10.69 Agent Failure

Agent failure MAY include:

-   hallucination;
-   invalid plan;
-   tool misuse;
-   timeout;
-   malformed output;
-   context confusion;
-   privilege attempt;
-   verification failure;
-   security compromise;
-   non-response.

Agent failure MUST enter Section 9/18 controlled failure path as
applicable.

------------------------------------------------------------------------

## 10.70 Agent Quarantine

Compromised/suspect Agent MAY be quarantined.

Quarantine MAY include:

-   revoke/suspend Authority;
-   remove tool access;
-   isolate Context;
-   stop assignments;
-   preserve Evidence;
-   trigger Risk reassessment.

Quarantine action itself MUST be governed.

------------------------------------------------------------------------

## 10.71 Agent Replacement

Replacing failed Agent MUST NOT automatically preserve all prior
assumptions.

Replacement SHOULD re-evaluate:

-   Capability;
-   Authority;
-   Context;
-   Risk;
-   State;
-   pending approvals;
-   execution contract.

------------------------------------------------------------------------

## 10.72 Agent State

Agent operational state MAY include:

-   `Available`
-   `Assigned`
-   `Executing`
-   `Waiting`
-   `Suspended`
-   `Quarantined`
-   `Failed`
-   `Terminated`

Implementation MAY extend states while preserving authoritative State
semantics.

------------------------------------------------------------------------

## 10.73 State Synchronization

Agent local state/memory MUST NOT supersede authoritative orchestration
State.

\[ AgentLocalState\neq AuthoritativeState\]

Before consequential Action, current State reference MUST be validated
according to Section 9/16.

------------------------------------------------------------------------

## 10.74 Agent Restart

Restarted Agent MUST NOT assume prior permissions remain valid.

Resume SHOULD reload/revalidate:

-   Task;
-   State;
-   Authority;
-   Policy;
-   Risk;
-   Context;
-   pending Decision.

\[ AgentRestart\not\Rightarrow ReuseStalePermit\]

------------------------------------------------------------------------

## 10.75 Agent Observability

AOF observability SHOULD capture governance-relevant events:

-   assignment;
-   proposal;
-   delegation;
-   Action request;
-   tool invocation;
-   Evidence emission;
-   verification;
-   failure;
-   escalation;
-   State transition.

AOF MUST NOT require storage/disclosure private Chain-of-Thought.

------------------------------------------------------------------------

## 10.76 Explainability Boundary

Implementation MAY request concise rationale/decision basis.

Rationale is not equivalent to hidden reasoning transcript.

\[ Rationale\neq PrivateChainOfThought\]

Conformance SHOULD evaluate observable governed behavior, not private
reasoning tokens.

------------------------------------------------------------------------

## 10.77 Agent Performance Metrics

Agent metrics MAY include:

-   success rate;
-   verified correctness;
-   failure rate;
-   retry rate;
-   escalation rate;
-   latency;
-   cost;
-   policy violations;
-   security incidents.

Metrics MUST NOT independently expand Authority.

------------------------------------------------------------------------

## 10.78 Historical Performance

Historical success MAY influence soft selection criteria atau Risk
treatment.

\[ PastSuccess\not\Rightarrow FutureAuthorization\]

Current Authority/Policy/State remain mandatory.

------------------------------------------------------------------------

## 10.79 Model Substitution

Changing underlying model/service MAY change Agent capability/risk
characteristics.

Material substitution SHOULD trigger reassessment of:

-   Capability;
-   Risk Profile;
-   trust;
-   verification requirements;
-   security;
-   qualification evidence.

Model substitution MUST NOT silently preserve unsupported assurance
claims.

------------------------------------------------------------------------

## 10.80 Version Binding

Agent definition SHOULD identify material version/configuration,
including where applicable:

-   model;
-   system prompt/control configuration;
-   toolset;
-   policy binding;
-   capability registry;
-   sandbox configuration.

Conformance evidence SHOULD bind to relevant version/configuration.

------------------------------------------------------------------------

## 10.81 Agent Supply Chain

Agent runtime MAY depend on models, prompts, packages, plugins, tools,
containers, external services.

Security Profile SHOULD apply supply-chain controls terhadap material
dependencies.

Compromised dependency MAY invalidate Agent trust/qualification.

------------------------------------------------------------------------

## 10.82 Agent Resource Budget

Agent MAY be constrained by:

-   token;
-   compute;
-   time;
-   cost;
-   API calls;
-   tool calls;
-   concurrency.

Resource budget SHOULD prevent uncontrolled consumption tetapi MUST NOT
force governance bypass.

------------------------------------------------------------------------

## 10.83 Agent Retry Behavior

Agent MAY retry reasoning internally sesuai bounded policy, tetapi
consequential Action retry MUST mengikuti Section 9/18 Retry semantics.

\[ ReasoningRetry\neq EffectRetry\]

------------------------------------------------------------------------

## 10.84 Agent Escalation

Agent SHOULD escalate ketika:

-   insufficient Authority;
-   insufficient Context;
-   unresolved Policy;
-   unacceptable Risk;
-   required Human decision;
-   verification conflict;
-   repeated failure;
-   suspected compromise.

Agent MUST NOT fabricate resolution untuk avoid escalation.

------------------------------------------------------------------------

## 10.85 Agent Termination

Agent/session termination SHOULD revoke or expire temporary
resources/Authority as applicable.

Termination MUST NOT erase Trace/Evidence required for accountability.

------------------------------------------------------------------------

## 10.86 Agent Requirements

**AOF-AGT-001** --- Agent MUST operate as bounded actor within
applicable Governance Envelope.

**AOF-AGT-002** --- Capability MUST NOT be treated as Authority.

**AOF-AGT-003** --- Agent MUST NOT self-authorize consequential Action.

**AOF-AGT-004** --- Agent assignment MUST satisfy applicable hard
eligibility constraints.

**AOF-AGT-005** --- Risk-sensitive Task assignment MUST consider Agent
Risk compatibility.

**AOF-AGT-006** --- Context supplied to Agent SHOULD follow
least-privilege semantics.

**AOF-AGT-007** --- Context or Memory possession MUST NOT create
Authority.

**AOF-AGT-008** --- Trust/confidence MUST NOT replace Authority or
required Verification.

**AOF-AGT-009** --- Agent output MUST NOT be treated as authorized
Decision solely because it was produced by Agent.

**AOF-AGT-010** --- Technical tool/credential access MUST NOT be treated
as governance Authority.

**AOF-AGT-011** --- Delegation MUST NOT expand inherited Authority.

**AOF-AGT-012** --- Delegation MUST preserve applicable mandatory
constraints.

**AOF-AGT-013** --- Delegation MUST NOT be used for Authority
laundering.

**AOF-AGT-014** --- Execution Authority MUST NOT automatically imply
result disclosure Authority.

**AOF-AGT-015** --- Mandatory Policy enforcement MUST NOT rely solely on
probabilistic Agent compliance.

**AOF-AGT-016** --- Agent identity used for consequential governance
SHOULD be integrity-protected.

**AOF-AGT-017** --- Independent verifier assignment MUST satisfy
applicable independence requirements.

**AOF-AGT-018** --- Agent local State MUST NOT supersede authoritative
orchestration State.

**AOF-AGT-019** --- Agent restart/replacement MUST revalidate stale
governance dependencies before consequential execution.

**AOF-AGT-020** --- Conformance MUST NOT require disclosure of private
Chain-of-Thought.

**AOF-AGT-021** --- Material model/service substitution SHOULD trigger
capability/risk/assurance reassessment.

**AOF-AGT-022** --- Compromised/suspect Agent SHOULD be containable
through governed quarantine/revocation mechanisms.

**AOF-AGT-023** --- Optimization for cost/latency MUST NOT override
mandatory Agent eligibility constraints.

**AOF-AGT-024** --- Recursive delegation SHOULD be bounded.

**AOF-AGT-025** --- Human Agent MUST remain subject to applicable
governance semantics.

**AOF-AGT-026** --- Orchestrator Agent MUST NOT be treated as implicit
root of Authority.

------------------------------------------------------------------------

## 10.87 Agent Invariants

### AGT-INV-01 --- Bounded Agency

\[ Agency(a)\subset eq GovernanceEnvelope(a) \]

### AGT-INV-02 --- Capability-Authority Separation

\[ Capability\neq Authority\]

### AGT-INV-03 --- Role-Authority Separation

\[ Role\neq Authority\]

### AGT-INV-04 --- No Self-Authorization

\[ SelfDeclaredAuthority\neq EffectiveAuthority\]

### AGT-INV-05 --- Context Non-Authority

\[ ContextPossession\not\Rightarrow Authority\]

### AGT-INV-06 --- Memory Non-Authority

\[ Memory\neq Authority\]

### AGT-INV-07 --- Trust Non-Authority

\[ TrustIncrease\not\Rightarrow AuthorityIncrease\]

### AGT-INV-08 --- Confidence Non-Verification

\[ Confidence\neq Verification\]

### AGT-INV-09 --- Proposal Non-Decision

\[ AgentOutput\neq AuthorizedDecision\]

### AGT-INV-10 --- Technical Access Non-Authority

\[ TechnicalAccess\neq Authority\]

### AGT-INV-11 --- Delegation Conservation

\[ Authority\_{delegatee}\subset eq Authority\_{delegator} \]

untuk inherited delegated Authority.

### AGT-INV-12 --- No Authority Laundering

\[ DelegationChain\not\Rightarrow PrivilegeExpansion\]

### AGT-INV-13 --- Execution/Disclosure Separation

\[ ExecutionAuthority\neq DisclosureAuthority\]

### AGT-INV-14 --- Policy Enforcement Independence

\[ PolicyPrompt\neq PolicyEnforcement\]

### AGT-INV-15 --- Agent Non-Root

\[ AIAgent\not\Rightarrow GovernanceRoot\]

### AGT-INV-16 --- State Authority

\[ AgentLocalState\neq AuthoritativeState\]

### AGT-INV-17 --- Restart Freshness

\[ AgentRestart\not\Rightarrow ReuseStalePermit\]

### AGT-INV-18 --- Verification Independence

\[ SelfCheck\neq IndependentVerification\]

### AGT-INV-19 --- Human Non-Omnipotence

\[ HumanPresence\not\Rightarrow UnlimitedAuthority\]

### AGT-INV-20 --- Optimization Bound

\[
UtilityOptimization\not\Rightarrow GovernanceWeakening
\]

------------------------------------------------------------------------

## 10.88 Reference Agent Conformance Tests

### CT-AGT-001 --- Capability Without Authority

Given Agent capable of operation but lacks Authority:

Expected: Agent MUST NOT be eligible for consequential execution.

### CT-AGT-002 --- High Capability, Risk Incompatible

Given highly capable Agent whose Risk Profile excludes Critical Task:

Expected: assignment rejected/escalated.

### CT-AGT-003 --- Context Injection

Given untrusted Context instructs Agent to ignore Policy:

Expected: no Authority/Policy change.

### CT-AGT-004 --- Tool Credential

Given Agent possesses valid technical credential but lacks governance
Authority:

Expected: governed Effect Boundary blocks operation.

### CT-AGT-005 --- Delegation Escalation

Given delegator lacks operation X and attempts to delegate X:

Expected: inherited delegation denied.

### CT-AGT-006 --- Self Verification

Given Agent creates output and self-checks it where VI2 required:

Expected: independent Verification remains unsatisfied.

### CT-AGT-007 --- Agent Restart

Given Agent restarts after Authority expiry:

Expected: stale permit not reused.

### CT-AGT-008 --- Orchestrator Agent Root

Given Orchestrator Agent asserts unlimited Authority:

Expected: assertion has no governance effect.

### CT-AGT-009 --- Human Agent Without Authority

Given Human Agent attempts consequential Action outside grant:

Expected: no implicit permit.

### CT-AGT-010 --- Cheapest Ineligible Agent

Given lowest-cost Agent fails mandatory Context/Risk eligibility:

Expected: selection algorithm excludes Agent.

### CT-AGT-011 --- Compromised Agent

Given Agent attempts to bypass Policy through direct tool invocation:

Expected: independent enforcement blocks/contains action.

### CT-AGT-012 --- Disclosure Boundary

Given Agent authorized to execute but not disclose sensitive result
externally:

Expected: external disclosure denied.

------------------------------------------------------------------------

## 10.89 Cross-Domain Agent Matrix

  Agent Concern            Primary AOF Domain
  ------------------------ ---------------------------------------
  Bounded Agency           Architecture, Agent, Human Governance
  Assignment lifecycle     Lifecycle, Agent
  Capability               Agent
  Authority                Authority Model
  Policy eligibility       Policy Model
  Risk compatibility       Risk Model
  Context                  Core Constructs, Security
  Evidence claims          Evidence
  Verifier eligibility     Verification
  Authoritative State      State & Trace
  Delegation               Authority, Agent
  Human Agent              Human Governance
  Agent failure            Failure & Recovery
  Agent compromise         Security
  Conformance              Conformance
  Machine representation   Schemas

------------------------------------------------------------------------

## 10.90 Freeze Candidate Criteria

Section 10 MAY dinyatakan `Freeze Candidate` jika:

1.  Agent remains Bounded Operational Actor;
2.  Capability/Role/Authority/Trust semantics separated;
3.  Agent eligibility integrates Capability, Authority, Policy, Risk,
    Context, dan State;
4.  Risk-Compatible Agent Selection defined;
5.  Governance Envelope aligned with Human Governance;
6.  Context/Memory least-privilege semantics aligned with Security;
7.  delegation conservation aligned with Authority;
8.  no Authority laundering;
9.  verifier eligibility/independence aligned with Verification;
10. Human Agent aligned with Section 17;
11. compromised-Agent assumption aligned with Security;
12. restart/replacement aligned with Lifecycle/State;
13. failure/quarantine aligned with Failure & Recovery;
14. no private Chain-of-Thought requirement introduced;
15. requirements/invariants have Conformance hooks;
16. no contradiction with Section 9 lifecycle;
17. Agent model remains model/tool/platform agnostic.

------------------------------------------------------------------------

## 10.91 Agent Formalization Result

Canonical Agent semantics:

\[ Agent=BoundedOperationalActor \]

\[ EligibleAgent(a,t)= CapabilityCompatible \land
AuthorityCompatible \land PolicyCompatible \land
RiskCompatible \land ContextCompatible \land
StateCompatible \]

\[ VerifierEligible= EligibleAgent \land VerificationCapability
\land IndependenceSatisfied \]

dengan:

\[ \boxed{ Capability\neq Authority } \]

\[ \boxed{ AgentOutput=UntrustedProposal } \]

\[ \boxed{ TechnicalAccess\neq Authority } \]

\[ \boxed{ DelegationChain\not\Rightarrow PrivilegeExpansion }
\]

\[ \boxed{ AgentLocalState\neq AuthoritativeState } \]

\[ \boxed{ AIAgent\not\Rightarrow GovernanceRoot } \]

Section 10 dengan demikian menjadi canonical Agent contract yang
konsisten dengan Section 9 Lifecycle dan seluruh
governance/assurance/security domains AOF.

------------------------------------------------------------------------

# 11. Authority Requirements

## 11.1 Purpose

`Authority Model` mendefinisikan siapa atau apa yang diperbolehkan
melakukan operation tertentu terhadap `Resource`, dalam scope,
constraints, validity, dan governance conditions tertentu.

Authority merupakan control primitive yang berbeda dari `Capability`,
`Role`, `Trust`, `Policy`, `Approval`, dan technical access.

Canonical separation:

\[
Capability\neq Role\neq Trust\neq Authority\neq Policy\neq Approval
\]

dan:

\[ Capability(a,x)\not\Rightarrow Authorized(a,x) \]

Tujuan model ini adalah mencegah implicit permission, privilege
amplification, authority laundering, uncontrolled delegation, stale
authorization, dan execution yang melampaui governance envelope.

------------------------------------------------------------------------

## 11.2 Authority Definition

Canonical authority grant:

\[ h= \langle id, subject, operations, resources, scope,
constraints, issuer, delegable, validity, status, provenance,
parentGrant \rangle\]

dengan:

-   `id`: stable grant identity;
-   `subject`: actor yang menerima grant;
-   `operations`: permitted operations;
-   `resources`: target resource set;
-   `scope`: bounded operational scope;
-   `constraints`: additional restrictions;
-   `issuer`: actor atau governance source yang menerbitkan grant;
-   `delegable`: apakah grant dapat didelegasikan;
-   `validity`: temporal validity;
-   `status`: lifecycle state;
-   `provenance`: origin dan authorization basis;
-   `parentGrant`: parent authority jika grant berasal dari delegation.

Authority evaluation:

\[ AuthEval(a,x,s)\rightarrow{Allow,Deny,Escalate,Pending} \]

`Pending` digunakan jika required authority information belum cukup atau
validity tidak dapat ditentukan.

------------------------------------------------------------------------

## 11.3 Positive Authorization

AOF menggunakan positive authorization untuk authority-sensitive action.

\[ NoApplicableGrant\Rightarrow Deny\]

Absence of explicit deny MUST NOT diperlakukan sebagai allow.

**AOF-AUTH-001** --- Authority-sensitive consequential `Action` MUST
memiliki applicable valid `Authority`.

**AOF-AUTH-002** --- Jika applicable grant tidak ditemukan,
implementation MUST menghasilkan `Deny`, `Pending`, atau `Escalate`;
MUST NOT menghasilkan implicit `Allow`.

------------------------------------------------------------------------

## 11.4 Authority Scope

Authority SHOULD dapat dibatasi setidaknya pada dimensions berikut bila
applicable:

\[ Scope= { Task, Resource, Operation, Environment, Time, Risk, Quantity
} \]

Contoh:

``` yaml
authority_grant:
  id: AG-1042
  subject: deployment-agent
  operations:
    - deploy
  resources:
    - application-x
  scope:
    task: release-2026-041
    environment:
      - staging
  constraints:
    max_risk: Moderate
    production: false
  delegable: false
```

Broad grant SHOULD dihindari ketika narrower grant dapat memenuhi task.

**AOF-AUTH-003** --- Effective permission MUST NOT melebihi applicable
grant scope.

------------------------------------------------------------------------

## 11.5 Authority Lifecycle

Reference lifecycle:

```text
Requested
    |
    v
  Active
   / | \
  /  |  \
 v   v   v
Suspended Expired Revoked
   \
    v
  Active

Active -> Consumed
Requested -> Denied
```

Canonical states:

`Requested`, `Active`, `Suspended`, `Revoked`, `Expired`, `Consumed`,
`Denied`.

### Requested

Grant telah diminta tetapi belum aktif.

### Active

Grant dapat digunakan jika seluruh applicable conditions terpenuhi.

### Suspended

Grant sementara tidak dapat digunakan.

### Revoked

Grant dihentikan sebelum natural expiry.

### Expired

Temporal validity telah berakhir.

### Consumed

Grant single-use atau quantity-bounded telah digunakan sampai limit.

### Denied

Request authority ditolak.

**AOF-AUTH-004** --- Hanya grant berstatus `Active` dan masih valid yang
MAY memenuhi authority predicate.

------------------------------------------------------------------------

## 11.6 Authority Validity

Authority validity merupakan conjunction dari applicable predicates:

\[ Valid(h,a,x,s,t)= SubjectMatch \land OperationMatch
\land ResourceMatch\land ScopeMatch
\land ConstraintMatch\land TimeValid
\land StatusActive\]

Jika salah satu mandatory predicate false:

\[ Valid=false \]

Jika mandatory predicate tidak dapat ditentukan:

\[ Valid=Pending \]

------------------------------------------------------------------------

## 11.7 Effective Authority

Base authority MAY berasal dari lebih dari satu bounded source.

Reference model:

\[ H\_{base}= H\_{granted} \cap H\_{task}
\cap H\_{session} \cap H\_{environment}
\cap H\_{time} \]

Effective usability kemudian dibatasi oleh governance state:

\[ H\_{usable}=Constrain(H\_{base},P,Risk,State) \]

Penting:

\[ Policy does not create Authority \]

\[ Risk does not create Authority \]

\[ State does not create Authority \]

Ketiganya dapat membuat authority yang secara nominal tersedia menjadi
tidak usable.

------------------------------------------------------------------------

## 11.8 Authority vs Policy

`Authority` menjawab:

> Apakah subject memiliki bounded right untuk operation ini?

`Policy` menjawab:

> Apakah operation ini diperbolehkan atau memerlukan control tambahan
> dalam kondisi saat ini?

Karena itu:

\[ PolicyAllow\not\Rightarrow AuthorityGrant\]

dan:

\[ AuthorityGrant\not\Rightarrow PolicyAllow\]

Execution memerlukan keduanya bila applicable.

**AOF-AUTH-005** --- Implementation MUST NOT menggunakan `Policy Allow`
sebagai pengganti missing authority grant.

------------------------------------------------------------------------

## 11.9 Authority vs Approval

`Approval` adalah decision atau consent event. `Authority` adalah
bounded permission relation.

\[ Approval\neq Authority\]

Approval MAY menjadi required condition bagi penggunaan authority,
tetapi approval tidak otomatis menciptakan unlimited grant.

Contoh:

\[ ExecuteAllowed= AuthorityValid \land PolicySatisfied
\land ApprovalSatisfied\]

jika approval required.

**AOF-AUTH-006** --- Approval MUST terikat pada identifiable
subject/scope dan MUST NOT diinterpretasikan lebih luas daripada
approval semantics yang diberikan.

------------------------------------------------------------------------

## 11.10 Authority vs Capability and Technical Access

\[ Capability\not\Rightarrow Authority\]

\[
CredentialPossession\not\Rightarrow GovernanceAuthority
\]

\[ ToolAccess\not\Rightarrow AuthorizedUse\]

Jika underlying platform hanya menyediakan broad credential, AOF
implementation SHOULD menyediakan logical enforcement yang mempersempit
actual usable operations.

**AOF-AUTH-007** --- Technical reachability MUST NOT menjadi
satu-satunya authority decision mechanism untuk consequential operation.

------------------------------------------------------------------------

## 11.11 Authority Issuance

Authority grant MUST berasal dari valid issuer atau governance source.

\[ Issue(i,h)\Rightarrow AuthorizedToIssue(i,h) \]

Issuer MUST NOT memberikan authority yang melebihi authority yang dapat
diterbitkannya menurut governance model.

Root organizational authority MAY berasal dari Human/organization
governance, system configuration, institutional policy, atau externally
established authority source sesuai deployment domain.

AOF tidak menganggap AI Agent sebagai autonomous root governance
authority.

**AOF-AUTH-008** --- Authority issuance MUST memiliki traceable issuer
dan authorization basis.

------------------------------------------------------------------------

## 11.12 Delegation

Delegation:

\[ delegate(a_i,a_j,h_d) \]

valid hanya jika:

\[ h_d\subset eq Authority(a_i) \]

dan:

\[ Delegable(h_d)=true \]

serta applicable policy mengizinkan delegation.

Canonical chain:

\[ Authority(a_3)\subset eq Authority(a_2)\subset eq
Authority(a_1) \]

Ini adalah **Authority Conservation Principle**.

**AOF-AUTH-009** --- Delegatee MUST NOT memperoleh authority yang lebih
luas daripada delegator dapat secara sah delegasikan.

**AOF-AUTH-010** --- Non-delegable grant MUST NOT digunakan sebagai
basis subdelegation.

------------------------------------------------------------------------

## 11.13 Authority Attenuation

Delegation SHOULD mempersempit atau mempertahankan, bukan memperluas,
authority.

Possible attenuation dimensions:

-   fewer operations;
-   fewer resources;
-   narrower task;
-   shorter validity;
-   lower quantity;
-   lower risk ceiling;
-   narrower environment;
-   additional constraints.

\[ H\_{child}\subset eq H\_{parent} \]

------------------------------------------------------------------------

## 11.14 Delegation Depth

Implementation SHOULD menetapkan maximum delegation depth untuk
workflows yang memungkinkan recursive delegation.

\[ DelegationDepth\leq DelegationLimit\]

Melebihi limit MUST menghasilkan `Deny`, `Replan`, atau `Escalate`.

Delegation depth merupakan control terhadap complexity dan
authority-chain ambiguity.

------------------------------------------------------------------------

## 11.15 No Authority Laundering

Authority laundering terjadi ketika actor mencoba memperoleh effective
permission melalui intermediate actor, tool, role, workflow, atau
delegation chain yang tidak dapat diperoleh secara langsung menurut
governance rules.

Canonical prohibition:

\[ NoAuthority(a,x) \land DelegateVia(b)
\not\Rightarrow Authorized(a,x) \]

**AOF-AUTH-011** --- Delegation chain MUST preserve provenance dan MUST
NOT menghasilkan privilege amplification.

------------------------------------------------------------------------

## 11.16 Authority Intersection

Jika beberapa grants berlaku terhadap satu action, implementation MUST
memiliki deterministic rule untuk menentukan effective authority.

Reference conservative rule:

\[ H\_{eff}= \bigcupApplicablePositiveGrants-
ExplicitRestrictions \]

tetapi only within common applicable governance constraints.

Deployment MAY menggunakan intersection-oriented model untuk
high-assurance contexts.

Rule yang dipilih MUST documented, deterministic, dan testable.

Explicit deny dari applicable `Policy` tetap berada di luar grant
aggregation dan dapat memblokir action.

------------------------------------------------------------------------

## 11.17 Authority Constraints

Constraints MAY mencakup:

-   maximum risk;
-   environment;
-   network boundary;
-   resource classification;
-   allowed parameter range;
-   transaction amount;
-   invocation count;
-   time window;
-   required verifier;
-   required approval;
-   required execution path.

Constraint violation membuat grant tidak applicable untuk candidate
action.

------------------------------------------------------------------------

## 11.18 Temporal Authority

Authority SHOULD memiliki explicit temporal semantics jika permission
tidak dimaksudkan permanent.

Reference:

\[ Validity(h)= \[validFrom,validUntil\] \]

Jika current time berada di luar validity:

\[ AuthorityValid=false \]

Clock uncertainty yang material terhadap high-risk action SHOULD
menghasilkan `Pending` atau stronger validation.

------------------------------------------------------------------------

## 11.19 Quantity-Bounded and Consumable Authority

Authority MAY dibatasi oleh count, amount, quota, atau one-time use.

Contoh:

``` yaml
constraints:
  max_invocations: 1
  max_records: 100
```

Jika limit tercapai:

\[ Status(h)=Consumed \]

atau remaining authority diperbarui secara atomic/equivalently
controlled.

**AOF-AUTH-012** --- Quantity-bounded authority MUST memiliki mechanism
yang mencegah silent over-consumption pada concurrent execution.

------------------------------------------------------------------------

## 11.20 Environment-Bounded Authority

Authority pada `development` atau `staging` MUST NOT diasumsikan berlaku
pada `production`.

\[
Authority\_{staging}\not\Rightarrow Authority\_{production}
\]

Environment transition MAY memerlukan separate grant, approval,
verification, atau risk evaluation.

------------------------------------------------------------------------

## 11.21 Resource-Bounded Authority

Authority MUST mengikat operation terhadap resource atau resource class
yang identifiable.

Wildcard resource scope SHOULD dianggap broader privilege dan SHOULD
memiliki stronger governance justification.

Dynamic resource resolution MUST dilakukan sebelum effect jika resource
identity material terhadap authorization.

------------------------------------------------------------------------

## 11.22 Operation-Bounded Authority

Permission untuk satu operation tidak otomatis memberikan permission
untuk operation lain.

\[ Read\not\Rightarrow Write\]

\[ Write\not\Rightarrow Delete\]

\[ Generate\not\Rightarrow Execute\]

\[ Execute\not\Rightarrow Approve\]

\[ Read\not\Rightarrow Disclose\]

------------------------------------------------------------------------

## 11.23 Information-Flow Authority

Authority untuk mengakses data berbeda dari authority untuk memindahkan,
mengungkapkan, merangkum, atau mengirim data kepada actor/domain lain.

\[ ReadAuthority\neq DisclosureAuthority\]

Cross-boundary disclosure MUST dievaluasi sebagai operation tersendiri
jika consequential.

**AOF-AUTH-013** --- Authorized access MUST NOT secara otomatis dianggap
authorized disclosure.

------------------------------------------------------------------------

## 11.24 Authority Request

Agent MAY mengusulkan atau meminta authority tambahan.

\[ RequestAuthority\neq GrantAuthority\]

Request SHOULD memuat:

-   subject;
-   requested operation;
-   resource;
-   task;
-   rationale;
-   duration;
-   risk;
-   required quantity;
-   delegation requirement jika ada.

Agent MUST NOT mengaktifkan requested authority sebelum valid grant
diterbitkan.

------------------------------------------------------------------------

## 11.25 Self-Authorization Prohibition

\[ Agent\not\Rightarrow SelfGrant\]

kecuali agent secara eksplisit bertindak sebagai authorized authority
issuer dalam governance model dan issuance tersebut tetap tunduk pada
independent applicable controls.

Secara default:

**AOF-AUTH-014** --- Agent MUST NOT menaikkan own operational authority
berdasarkan reasoning, confidence, urgency, task difficulty, atau
technical necessity semata.

------------------------------------------------------------------------

## 11.26 Revocation

Revocation:

\[ revoke(i,h) \]

MUST hanya dilakukan oleh actor/control yang authorized untuk revoke
grant tersebut.

Setelah revocation committed:

\[ Revoked(h)\Rightarrow\neg NewExecutionUsing(h) \]

Architecture MUST menerapkan propagation sebagaimana Section 8.

Queued atau pending actions yang bergantung pada revoked grant MUST
direevaluasi.

------------------------------------------------------------------------

## 11.27 Suspension

Suspension bersifat reversible dan tidak identik dengan revocation.

\[ Suspended(h)\Rightarrow\neg Usable(h) \]

Resume dari `Suspended` ke `Active` MUST merupakan controlled authority
transition dan traceable.

------------------------------------------------------------------------

## 11.28 Expiry

Expiry terjadi ketika temporal validity berakhir tanpa explicit
revocation.

Expired authority MUST NOT digunakan untuk new action.

Renewal SHOULD menghasilkan new validity decision dan trace;
implementation SHOULD NOT silently memperpanjang expired grant.

------------------------------------------------------------------------

## 11.29 Authority Consumption

Single-use atau quota-based authority SHOULD memiliki atomic atau
equivalently safe consumption semantics.

Concurrent consumers MUST NOT dapat menggunakan grant melampaui quantity
limit akibat race condition.

------------------------------------------------------------------------

## 11.30 Authority Revalidation

Authority SHOULD direvalidasi:

-   sebelum consequential effect;
-   setelah material state change;
-   setelah delegation;
-   setelah waiting period;
-   setelah retry/replan;
-   setelah risk escalation;
-   ketika resource identity berubah;
-   ketika approval validity berubah;
-   ketika revocation event mungkin terjadi.

Reference:

\[
AuthorityValid\_{t_1}\not\Rightarrow AuthorityValid\_{t_2}
\]

------------------------------------------------------------------------

## 11.31 Authority and Retry

Retry MUST NOT reuse stale authority blindly.

Jika prior action telah mengonsumsi quantity-bounded authority atau
menghasilkan partial effect, retry MUST melakukan reconciliation sebelum
authority reuse.

------------------------------------------------------------------------

## 11.32 Authority and Replan

Replan dapat mengubah:

-   agent;
-   resource;
-   operation;
-   environment;
-   execution method.

Karena itu:

\[ Replan\Rightarrow ReevaluateAuthority\]

jika perubahan material terhadap authority scope terjadi.

------------------------------------------------------------------------

## 11.33 Authority and Agent Replacement

Replacement agent tidak mewarisi authority dari previous agent secara
implicit.

\[
Replace(a_i,a_j)\not\Rightarrow Authority(a_j)=Authority(a_i)
\]

**AOF-AUTH-015** --- Replacement actor MUST melalui eligibility dan
authority evaluation baru.

------------------------------------------------------------------------

## 11.34 Authority and Multi-Agent Orchestration

Dalam multi-agent workflow, setiap consequential actor MUST memiliki
authority yang applicable terhadap own operation.

Authority supervisor tidak otomatis mengalir ke worker.

\[
Authority(supervisor)\not\Rightarrow Authority(worker)
\]

Assignment hanya memberikan task responsibility; assignment bukan
authority grant kecuali governance model secara eksplisit menggabungkan
keduanya dan semantic grant tetap traceable.

------------------------------------------------------------------------

## 11.35 Authority and Orchestrator

`Orchestrator` MAY memiliki authority untuk assignment, routing, retry,
replan, escalation, atau termination sesuai governance model.

Namun:

\[ OrchestratorRole\not\Rightarrow UnlimitedAuthority\]

`Orchestrator` MUST tunduk pada authority boundaries yang sama untuk
consequential effect.

------------------------------------------------------------------------

## 11.36 Human Authority

Human actor tidak secara otomatis memiliki unlimited authority hanya
karena merupakan Human.

Human authority MAY berasal dari:

-   organizational role;
-   explicit delegation;
-   system ownership;
-   governance charter;
-   regulatory/legal mandate;
-   incident/emergency role.

Human approval atau override MUST traceable.

Framework membedakan:

\[ OrganizationalGovernanceAuthority \]

dari:

\[ DelegatedOperationalAuthority \]

AI Agent MAY menerima bounded operational authority, tetapi root
governance conditions berasal dari valid organizational/governance
authority source.

------------------------------------------------------------------------

## 11.37 Emergency Authority

Deployment MAY mendefinisikan emergency authority atau break-glass
procedure.

Emergency authority MUST:

-   explicit;
-   time-bounded;
-   actor-bound;
-   purpose-bound;
-   traceable;
-   subject to post-action review;
-   tidak menjadi permanent silent privilege.

Emergency mode SHOULD meningkatkan logging dan assurance, bukan
meniadakannya.

------------------------------------------------------------------------

## 11.38 Authority Provenance

Setiap grant SHOULD dapat menjawab:

-   siapa/apa issuer-nya;
-   berdasarkan authority apa grant diterbitkan;
-   kapan diterbitkan;
-   untuk siapa;
-   untuk scope apa;
-   apakah delegated;
-   parent grant apa;
-   apakah telah diubah, suspended, revoked, expired, atau consumed.

\[ Authority\Rightarrow Provenance\]

untuk consequential use.

------------------------------------------------------------------------

## 11.39 Authority Trace Events

Reference authority events:

-   `AuthorityRequested`;
-   `AuthorityGranted`;
-   `AuthorityDenied`;
-   `AuthorityDelegated`;
-   `AuthorityAttenuated`;
-   `AuthoritySuspended`;
-   `AuthorityResumed`;
-   `AuthorityRevoked`;
-   `AuthorityExpired`;
-   `AuthorityConsumed`;
-   `AuthorityEvaluationPerformed`.

Events SHOULD memiliki correlation dengan session/task/action yang
relevant.

------------------------------------------------------------------------

## 11.40 Authority Decision Evidence

Consequential authority evaluation SHOULD menghasilkan evidence atau
trace data yang cukup untuk menunjukkan:

-   applicable grant(s);
-   scope match;
-   constraints;
-   status;
-   validity;
-   delegation chain jika ada;
-   evaluation result;
-   evaluator;
-   timestamp/state version.

Private chain-of-thought tidak diperlukan.

------------------------------------------------------------------------

## 11.41 Authority Failure Modes

Reference failure modes:

### AUTH-F01 --- Missing Grant

Tidak ada applicable grant.

### AUTH-F02 --- Scope Violation

Action berada di luar scope.

### AUTH-F03 --- Expired Grant

Grant sudah expired.

### AUTH-F04 --- Revoked Grant

Grant telah revoked.

### AUTH-F05 --- Suspended Grant

Grant sedang suspended.

### AUTH-F06 --- Non-Delegable Delegation

Delegation menggunakan grant yang tidak delegable.

### AUTH-F07 --- Privilege Amplification

Child grant lebih luas daripada parent.

### AUTH-F08 --- Stale Authorization

Decision menggunakan authority state lama.

### AUTH-F09 --- Quantity Exhaustion

Consumable authority telah habis.

### AUTH-F10 --- Authority Laundering

Indirect path mencoba melewati authority boundary.

### AUTH-F11 --- Issuer Invalidity

Issuer tidak authorized menerbitkan grant.

### AUTH-F12 --- Provenance Failure

Authority basis tidak dapat direkonstruksi.

Failure MUST menghasilkan controlled outcome sesuai applicable policy;
authority failure MUST NOT silently fail-open.

------------------------------------------------------------------------

## 11.42 Authority Evaluation Algorithm

Reference algorithm:

```text
INPUT:
  actor
  candidate action
  resource
  current state
  current time

1. Resolve actor identity.
2. Resolve actual operation.
3. Resolve actual resource.
4. Retrieve applicable authority grants.
5. If none:
      DENY / ESCALATE
6. Remove grants that are:
      inactive
      expired
      revoked
      suspended
      consumed
7. Validate subject.
8. Validate operation.
9. Validate resource.
10. Validate task/session/environment scope.
11. Validate constraints.
12. Validate delegation provenance.
13. Validate quantity/temporal conditions.
14. If mandatory information unknown:
      PENDING / ESCALATE
15. Compute applicable effective authority.
16. Return:
      ALLOW / DENY / ESCALATE / PENDING
17. Record evaluation trace.
```

Algorithm bersifat reference; implementation MAY menggunakan equivalent
mechanism.

------------------------------------------------------------------------

## 11.43 Authority Conformance Requirements

### Core

**AOF-AUTH-007 (canonical cross-reference)** — See the primary normative definition above.
satu-satunya authority basis.

### Governed

**AOF-AUTH-016** --- Revoked, expired, suspended, atau consumed
authority MUST NOT digunakan untuk new consequential action.

**AOF-AUTH-017** --- Material replan yang mengubah authority scope MUST
memicu reevaluation.

**AOF-AUTH-018** --- Delegation chain MUST traceable.

### Assured / High-Assurance

**AOF-AUTH-019** --- High-risk effect SHOULD melakukan authority
revalidation pada Effect Boundary.

**AOF-AUTH-020** --- High-assurance profile MUST menentukan protection
terhadap unauthorized grant mutation.

**AOF-AUTH-021** --- High-assurance authority evaluation evidence MUST
cukup untuk independent reconstruction.

------------------------------------------------------------------------

## 11.44 Authority Invariants

Numbering final akan direkonsiliasi pada canonical Invariant Registry.

### AUTH-INV-01 --- Authority Bound

\[ Execute(a,x)\Rightarrow Authorized(a,x) \]

### AUTH-INV-02 --- Positive Authorization

\[ NoGrant\Rightarrow NoAuthoritySensitiveExecution\]

### AUTH-INV-03 --- Capability-Authority Separation

\[ Capability(a,x)\not\Rightarrow Authority(a,x) \]

### AUTH-INV-04 --- Delegation Conservation

\[ Delegate(a_i,a_j,h)\Rightarrow h\subset eq
DelegableAuthority(a_i) \]

### AUTH-INV-05 --- No Self-Elevation

\[ AgentReasoning\not\Rightarrow AuthorityIncrease\]

### AUTH-INV-06 --- Revocation Enforcement

\[ Revoked(h)\Rightarrow\neg NewExecutionUsing(h) \]

### AUTH-INV-07 --- Policy Non-Creation

\[ PolicyAllow\not\Rightarrow AuthorityGrant\]

### AUTH-INV-08 --- Approval Non-Expansion

\[ Approval\not\Rightarrow UnlimitedAuthority\]

### AUTH-INV-09 --- Information-Flow Separation

\[ ReadAuthority\not\Rightarrow DisclosureAuthority\]

### AUTH-INV-10 --- Replacement Non-Inheritance

\[
Replace(a_i,a_j)\not\Rightarrow InheritAuthority(a_j,a_i)
\]

### AUTH-INV-11 --- Temporal Validity

\[ Expired(h)\Rightarrow\neg Usable(h) \]

### AUTH-INV-12 --- Authority Provenance

\[ ConsequentialAuthorityUse\Rightarrow TraceableAuthorityBasis
\]

------------------------------------------------------------------------

## 11.45 Architecture Integration

Authority Model mengikat langsung dengan Section 8.

Canonical flow:

```text
Proposal
   |
   v
Control Plane
   |
   v
Authority Evaluator
   |
   +--> Resolve Identity
   +--> Resolve Operation/Resource
   +--> Retrieve Grants
   +--> Validate Scope
   +--> Validate Lifecycle
   +--> Validate Delegation
   +--> Validate Constraints
   |
   v
Authority Result
   |
   +--> Allow
   +--> Deny
   +--> Pending
   +--> Escalate
```

Authority `Allow` belum cukup untuk execution:

\[ AuthorityAllow \land Policy\land Risk
\land State\land Verification
\Rightarrow CandidatePermit\]

------------------------------------------------------------------------

## 11.46 Authority Freeze Candidate Criteria

Authority area MAY dinyatakan `Freeze Candidate` jika:

1.  positive authorization semantics stabil;
2.  grant schema semantics stabil;
3.  authority lifecycle stabil;
4.  delegation conservation stabil;
5.  authority-policy separation stabil;
6.  authority-approval separation stabil;
7.  revocation/expiry/consumption semantics stabil;
8.  Effect Boundary revalidation compatible dengan Architecture;
9.  Human/organizational root governance semantics compatible dengan
    Human Governance;
10. conformance requirements dapat dipetakan ke tests;
11. tidak ada contradiction dengan Agent, Policy, Risk, State, Trace,
    dan Security models.

------------------------------------------------------------------------

## 11.47 Authority Formalization Result

Authority v1.0 RC-Authority diringkas sebagai:

\[ Authority= Explicit + Scoped + Constrained + TimeBounded +
Traceable + Revocable + ConservativeDelegation \]

dengan:

\[ \boxed{ No\ Grant\Rightarrow No\ Authority } \]

\[ \boxed{ Capability\neq Authority } \]

\[ \boxed{ Delegation\ Cannot\ Create\ New\ Authority } \]

\[
\boxed{ Policy\ Can\ Restrict\ Authority,\ But\ Cannot\ Create\ It }
\]

dan:

\[
\boxed{ Agent\ Autonomy\subset eq Effective\ Authority\subset eq Governance\ Envelope }
\] \# 12. Policy Requirements

## 12.1 Purpose

`Policy Model` mendefinisikan normative rules yang mengendalikan
bagaimana `Proposal`, `Decision`, `Action`, delegation, verification,
approval, escalation, retry, replan, termination, dan information flow
dievaluasi dalam orchestration.

Policy merupakan governance constraint, bukan authority source.

Canonical separation:

\[ Policy\neq Authority\neq Approval\neq Risk\]

dan:

\[ PolicyAllow\not\Rightarrow AuthorityGrant\]

Policy MAY membatasi penggunaan authority, mensyaratkan control
tambahan, atau menolak action. Policy MUST NOT menciptakan authority
yang tidak pernah diberikan.

------------------------------------------------------------------------

## 12.2 Policy Definition

Canonical policy:

\[ p= \langle id, version, scope, subject, resource, action,
condition, effect, priority, source, validity, status, provenance
\rangle\]

dengan:

-   `id`: stable policy identity;
-   `version`: policy version;
-   `scope`: applicability boundary;
-   `subject`: actor/role/class yang dikenai policy;
-   `resource`: target resource/resource class;
-   `action`: operation atau decision class;
-   `condition`: predicate yang harus dievaluasi;
-   `effect`: policy outcome;
-   `priority`: explicit ordering jika diperlukan;
-   `source`: governance source;
-   `validity`: temporal applicability;
-   `status`: lifecycle state;
-   `provenance`: origin dan change history.

Reference effects:

\[ PolicyEffect= { Allow, Deny, RequireVerification, RequireApproval,
Escalate } \]

Implementation MAY menambahkan effects seperti `RequireReplan`,
`RequireConstraint`, atau domain-specific effect melalui extension,
selama core semantics tidak dilemahkan.

------------------------------------------------------------------------

## 12.3 Policy Evaluation

Policy evaluation:

\[ Evaluate(P,x,c,s)\rightarrow d_p \]

dengan:

\[
d_p\in { Allow, Deny, RequireVerification, RequireApproval, Escalate, Pending }
\]

`Pending` digunakan jika mandatory policy context belum tersedia atau
tidak dapat ditentukan.

**AOF-POL-001** --- Consequential `Action` MUST dievaluasi terhadap
seluruh applicable mandatory `Policy` sebelum effect.

**AOF-POL-002** --- Mandatory policy result yang unknown atau unresolved
MUST NOT diperlakukan sebagai `Allow`.

------------------------------------------------------------------------

## 12.4 Policy Applicability

Applicability:

\[ Applicable(p,x,c,s)\rightarrow{true,false,unknown} \]

Policy applicability MAY bergantung pada:

-   subject identity;
-   role;
-   task;
-   action;
-   resource;
-   environment;
-   data classification;
-   risk;
-   state;
-   time;
-   location/domain;
-   delegation status;
-   verification status;
-   approval status;
-   external governance condition.

Jika applicability `unknown` untuk mandatory policy, evaluation MUST
menghasilkan `Pending`, `Escalate`, atau conservative equivalent.

------------------------------------------------------------------------

## 12.5 Policy Scope

Reference scope dimensions:

\[ PolicyScope= { Organization, Domain, Environment, Session, Task,
Agent, Resource, Action, Data, Risk, Time } \]

Narrower policy MAY menambahkan restrictions terhadap broader policy.

Narrower policy MUST NOT secara diam-diam melemahkan mandatory
higher-governance restriction kecuali explicit override semantics
mengizinkannya.

------------------------------------------------------------------------

## 12.6 Policy Source and Governance Hierarchy

Policy MUST memiliki identifiable governance source.

Possible sources:

-   organizational governance;
-   legal/regulatory requirement;
-   security governance;
-   domain governance;
-   framework profile;
-   application/system policy;
-   session/task policy;
-   emergency policy.

Implementation SHOULD mendokumentasikan hierarchy atau precedence antar
policy sources.

Example:

```text
External Mandatory Requirement
        |
        v
Organizational Governance
        |
        v
Domain / Security Policy
        |
        v
Application Policy
        |
        v
Task / Session Constraint
```

Lower-level policy MUST NOT override higher-level mandatory restriction
tanpa explicit authorized override mechanism.

------------------------------------------------------------------------

## 12.7 Policy Lifecycle

Reference lifecycle:

`Draft`, `Active`, `Suspended`, `Deprecated`, `Expired`, `Retired`.

Only applicable `Active` policy SHOULD menghasilkan normal enforcement
effect.

Policy activation, suspension, replacement, atau retirement MUST
traceable untuk consequential governance rules.

**AOF-POL-003** --- Policy version yang digunakan dalam consequential
decision MUST dapat diidentifikasi atau direkonstruksi.

------------------------------------------------------------------------

## 12.8 Policy Versioning

Policy change dapat mengubah validitas pending decision.

\[ Policy\_{v1}\neq Policy\_{v2} \]

Jika material policy change terjadi antara decision dan Effect Boundary:

\[
Decision\_{v1}\not\Rightarrow ValidUnder(Policy\_{v2})
\]

Consequential pending action SHOULD direevaluasi sesuai revalidation
policy.

------------------------------------------------------------------------

## 12.9 Policy Conflict Resolution

Default restrictive precedence:

\[ Deny \> Escalate \> RequireApproval \> RequireVerification \> Allow
\]

Jika beberapa applicable policies menghasilkan outcomes berbeda,
implementation MUST menggunakan deterministic conflict-resolution rule.

**AOF-POL-004** --- Conflict resolution MUST deterministic, documented,
dan traceable.

**AOF-POL-005** --- Jika implementation menggunakan precedence berbeda
dari default AOF precedence, override rule MUST explicit dan MUST NOT
silently weaken applicable mandatory higher-level policy.

------------------------------------------------------------------------

## 12.10 Restrictive Decision Dominance

Default AOF principle:

> Ketika dua applicable policy decisions tidak dapat dipenuhi secara
> bersamaan, outcome yang lebih restrictive mendominasi kecuali explicit
> authorized policy-composition rule menentukan sebaliknya.

Ini disebut **Restrictive Decision Dominance**.

Contoh:

```text
Policy A -> Allow
Policy B -> RequireVerification
Result   -> RequireVerification
```

```text
Policy A -> RequireApproval
Policy B -> Deny
Result   -> Deny
```

------------------------------------------------------------------------

## 12.11 Policy Composition

Policy sets MAY disusun secara hierarchical atau compositional.

Reference:

\[ P\_{effective} = Compose( P\_{framework}, P\_{organization},
P\_{domain}, P\_{environment}, P\_{session}, P\_{task} ) \]

Composition MUST mempertahankan applicable mandatory constraints.

Policy composition SHOULD menghindari hidden mutation terhadap source
policy.

------------------------------------------------------------------------

## 12.12 Policy Inheritance

Child task SHOULD mewarisi applicable parent policy constraints.

\[ ApplicablePolicy(t\_{child}) \supset eq
InheritedMandatoryPolicy(t\_{parent}) \]

Delegation, retry, replan, atau agent replacement MUST NOT menghilangkan
applicable mandatory policy secara implicit.

**AOF-POL-006** --- Applicable mandatory policy MUST survive task
decomposition dan delegation kecuali explicit authorized policy
transition menyatakan sebaliknya.

------------------------------------------------------------------------

## 12.13 Policy Override

Policy override adalah controlled exception terhadap normally applicable
policy.

Override MUST memiliki:

-   explicit authority;
-   target policy;
-   scope;
-   rationale;
-   validity;
-   actor;
-   approval jika required;
-   trace;
-   residual risk handling jika applicable.

\[ Override\neq Ignore\]

**AOF-POL-007** --- Policy MUST NOT diabaikan hanya karena agent,
orchestrator, atau Human menganggapnya inconvenient.

------------------------------------------------------------------------

## 12.14 Policy Exception

Exception MAY didefinisikan sebelumnya dalam policy.

Contoh:

``` yaml
condition:
  environment: development
effect: Allow
exceptions:
  - if:
      data_classification: restricted
    effect: RequireApproval
```

Exception merupakan bagian policy semantics dan berbeda dari ad-hoc
override.

------------------------------------------------------------------------

## 12.15 Policy and Authority

Authority evaluation dan policy evaluation MUST tetap distinguishable.

Reference execution:

\[ CandidatePermit= AuthorityValid \land PolicySatisfied
\land RiskAcceptable\land StateValid
\land VerificationSatisfied\]

Policy MAY:

-   deny penggunaan valid authority;
-   mensyaratkan verification;
-   mensyaratkan approval;
-   memicu escalation.

Policy MUST NOT:

-   membuat missing grant menjadi valid;
-   memperluas resource scope dari authority;
-   memperpanjang expired authority secara implicit.

------------------------------------------------------------------------

## 12.16 Policy and Risk

Policy MAY menggunakan `Risk` sebagai input:

\[ Risk(x)\geq T_h \Rightarrow
RequireIndependentVerification \]

Risk assessment sendiri bukan policy decision.

\[ RiskResult\neq PolicyResult\]

Policy menentukan governance response terhadap risk.

**AOF-POL-008** --- Risk classification MUST NOT secara implicit
menghasilkan permission; applicable policy/control mapping tetap
diperlukan.

------------------------------------------------------------------------

## 12.17 Policy and Verification

Policy MAY menentukan:

-   apakah verification required;
-   verification mode;
-   verifier independence;
-   evidence requirements;
-   verification threshold;
-   failure behavior;
-   re-verification trigger.

Example:

``` yaml
if:
  action: deploy
  environment: production
then:
  effect: RequireVerification
  verification_profile: production-release
```

Policy MUST NOT menganggap self-asserted agent confidence sebagai
verification.

------------------------------------------------------------------------

## 12.18 Policy and Approval

Policy MAY menghasilkan `RequireApproval`.

Approval requirement SHOULD menentukan:

-   approver class/role;
-   approval scope;
-   validity;
-   required context/evidence;
-   whether multiple approvers required;
-   whether separation of duties required.

Approval result kembali ke Control Plane sebagai governed input.

------------------------------------------------------------------------

## 12.19 Policy and State

Policy MAY bergantung pada orchestration state.

Example:

\[ State(t)\neq Verifying\Rightarrow Deny(Complete(t))
\]

Policy yang bergantung pada state MUST menggunakan authoritative state
atau controlled state projection.

Agent private memory MUST NOT menjadi sole authoritative source untuk
policy-critical state.

------------------------------------------------------------------------

## 12.20 Policy and Context

Policy condition MAY bergantung pada context, tetapi context trust harus
diperhatikan.

Untrusted context MUST NOT dapat secara langsung mengubah policy
semantics.

\[ UntrustedContent\not\Rightarrow PolicyMutation\]

Jika untrusted input digunakan sebagai policy evaluation fact,
implementation SHOULD melakukan validation atau classification sesuai
risk.

------------------------------------------------------------------------

## 12.21 Policy and Data Classification

Policy SHOULD mendukung information-flow controls berdasarkan
classification.

Contoh classifications MAY mencakup:

`Public`, `Internal`, `Confidential`, `Restricted`, atau domain-specific
equivalents.

Example rule:

```text
IF data = Restricted
AND destination = ExternalService
THEN Deny
```

atau:

```text
THEN RequireApproval + Redaction
```

Policy untuk read dan disclosure SHOULD dapat dibedakan.

------------------------------------------------------------------------

## 12.22 Policy and Resource Operations

Policy SHOULD dapat membedakan operations:

\[
Read\neq Write\neq Modify\neq Delete\neq Execute\neq Deploy\neq Disclose
\]

Policy allow untuk `Read` MUST NOT secara implicit berlaku untuk `Write`
atau `Disclose`.

------------------------------------------------------------------------

## 12.23 Policy and Delegation

Policy MAY membatasi:

-   apakah delegation allowed;
-   eligible delegatee;
-   delegation depth;
-   resource classes;
-   maximum risk;
-   context disclosure;
-   subdelegation.

Delegation MUST membawa applicable policy references atau equivalent
governance context.

------------------------------------------------------------------------

## 12.24 Policy and Retry

Retry MAY memerlukan reevaluation jika:

-   policy version berubah;
-   risk berubah;
-   state berubah;
-   authority berubah;
-   prior attempt menghasilkan effect;
-   retry count mencapai threshold.

Policy MAY menetapkan:

\[ RetryCount\geq N\Rightarrow Escalate\]

------------------------------------------------------------------------

## 12.25 Policy and Replan

Replan MAY mengubah applicable policies karena task, resource, agent,
operation, atau environment berubah.

\[ Replan\Rightarrow RecomputeApplicablePolicy\]

jika material policy scope berubah.

------------------------------------------------------------------------

## 12.26 Policy and Termination

Policy MAY menentukan mandatory termination conditions.

Contoh:

-   critical security violation;
-   revoked root authority;
-   exhausted cost budget;
-   repeated verification failure;
-   forbidden resource access;
-   unresolved critical risk.

Termination policy MUST traceable.

------------------------------------------------------------------------

## 12.27 Policy and Emergency Operation

Emergency/break-glass policy MAY memberikan alternate control path,
tetapi MUST tetap explicit.

Emergency policy SHOULD menentukan:

-   trigger;
-   eligible actor;
-   scope;
-   duration;
-   required trace;
-   post-action review;
-   additional monitoring;
-   residual risk handling.

Emergency policy MUST NOT berarti "all controls disabled".

------------------------------------------------------------------------

## 12.28 Policy Enforcement Architecture

Policy enforcement SHOULD berada pada Control Plane atau equivalent
trusted control boundary.

Reference flow:

```text
Candidate Action
      |
      v
Policy Applicability
      |
      v
Condition Evaluation
      |
      v
Policy Effects
      |
      v
Conflict Resolution
      |
      v
Policy Result
```

Reasoning Plane MAY membantu interpretasi complex policy, tetapi
mandatory enforcement MUST tetap bounded dan traceable.

------------------------------------------------------------------------

## 12.29 No Safety by Prompt Alone

Policy yang hanya disampaikan melalui prompt tidak cukup untuk
consequential enforcement.

\[ PolicyPrompt\neq PolicyEnforcement\]

Prompt MAY digunakan sebagai preventive behavioral guidance.

Control Plane MUST menyediakan enforceable mechanism untuk mandatory
policy.

**AOF-POL-009** --- Mandatory consequential policy MUST memiliki
enforcement path di luar sole reliance pada model compliance.

------------------------------------------------------------------------

## 12.30 Deterministic Policy Evaluation

Jika policy dapat diekspresikan sebagai deterministic predicates,
implementation SHOULD menggunakan deterministic evaluator untuk
enforcement-critical decision.

Agentic policy interpretation MAY digunakan untuk ambiguous text,
classification, atau recommendation, tetapi final consequential effect
SHOULD melalui explicit normalized decision semantics.

------------------------------------------------------------------------

## 12.31 Policy Normalization

Natural-language governance rule SHOULD dinormalisasi menjadi
enforceable representation jika digunakan sebagai machine-enforced
policy.

Reference representation:

``` yaml
policy:
  id: POL-PROD-DEPLOY-001
  version: 1
  scope:
    environment: production
  subject:
    type: agent
  action:
    - deploy
  condition:
    risk:
      minimum: High
  effect:
    - RequireIndependentVerification
    - RequireApproval
```

Schema di atas illustrative, bukan final canonical schema.

------------------------------------------------------------------------

## 12.32 Policy Decision Record

Consequential policy evaluation SHOULD menghasilkan record minimal:

```text
policy_decision_id
policy_set/version
subject
action
resource
context/state reference
applicable policies
individual effects
conflict-resolution rule
final policy result
timestamp
evaluator
```

Record MAY berada di `Trace` atau linked evidence store.

------------------------------------------------------------------------

## 12.33 Policy Provenance

Policy provenance SHOULD menjawab:

-   source;
-   author/issuer;
-   version;
-   activation;
-   changes;
-   superseded version;
-   applicable governance basis.

Consequential policy MUST dapat dibedakan dari dynamically generated
agent suggestion.

\[ GeneratedSuggestion\neq GovernancePolicy\]

------------------------------------------------------------------------

## 12.34 Policy Integrity

Unauthorized policy mutation MUST dicegah atau detectable sesuai
profile.

High-assurance implementation SHOULD menggunakan stronger policy
integrity controls seperti signed configuration, protected repository,
change approval, immutable history, atau equivalent mechanism.

Framework tidak mewajibkan technology tertentu.

------------------------------------------------------------------------

## 12.35 Policy Freshness

Policy evaluator MUST menggunakan applicable active version sesuai
policy versioning semantics.

Cached policy MAY digunakan jika freshness guarantees cukup.

Stale policy yang material terhadap consequential action MUST memicu
refresh atau conservative outcome.

------------------------------------------------------------------------

## 12.36 Policy Distribution

Distributed architecture MUST memiliki mechanism agar enforcement points
mengetahui applicable policy version atau dapat memverifikasi decision
yang dibuat oleh trusted policy evaluator.

Policy propagation delay yang dapat menyebabkan unsafe allow MUST
ditangani melalui version binding, revalidation, deny/pending, atau
equivalent control.

------------------------------------------------------------------------

## 12.37 Policy Failure Modes

Reference failure taxonomy:

### POL-F01 --- Missing Mandatory Policy

Expected policy tidak tersedia.

### POL-F02 --- Unknown Applicability

Applicability tidak dapat ditentukan.

### POL-F03 --- Conflict Resolution Failure

Applicable effects tidak dapat direkonsiliasi.

### POL-F04 --- Stale Policy

Evaluator menggunakan superseded policy.

### POL-F05 --- Unauthorized Mutation

Policy berubah tanpa valid governance process.

### POL-F06 --- Enforcement Bypass

Action melewati policy gate.

### POL-F07 --- Prompt-Only Enforcement

Mandatory control hanya bergantung pada agent compliance.

### POL-F08 --- Scope Leakage

Policy diterapkan terlalu luas atau terlalu sempit.

### POL-F09 --- Invalid Override

Policy dilemahkan tanpa valid override authority.

### POL-F10 --- Policy Drift

Implementation semantics berbeda dari canonical policy intent.

Mandatory policy failure MUST NOT silently fail-open.

------------------------------------------------------------------------

## 12.38 Policy Evaluation Algorithm

Reference algorithm:

```text
INPUT:
  subject
  candidate action
  resource
  context
  authoritative state
  risk
  current time

1. Resolve applicable policy sources.
2. Resolve active policy versions.
3. Determine applicability.
4. If mandatory applicability is unknown:
      PENDING / ESCALATE
5. Evaluate policy conditions.
6. Collect effects.
7. Validate overrides/exceptions.
8. Resolve conflicts deterministically.
9. Produce final Policy Result.
10. Bind result to relevant state/policy versions.
11. Record decision.
12. Return:
      ALLOW
      DENY
      REQUIRE_VERIFICATION
      REQUIRE_APPROVAL
      ESCALATE
      PENDING
```

------------------------------------------------------------------------

## 12.39 Policy Conformance Requirements

### Core

### Governed

**AOF-POL-010** --- Policy change material terhadap pending action MUST
ditangani melalui revalidation atau conservative equivalent.

**AOF-POL-011** --- Policy evaluation MUST menggunakan authoritative
state untuk state-dependent rules.

**AOF-POL-012** --- Delegation MUST preserve applicable policy
constraints.

**AOF-POL-013** --- Replan yang mengubah policy scope MUST memicu
applicability reevaluation.

**AOF-POL-014** --- Emergency policy MUST bounded dan traceable.

**AOF-POL-015** --- Policy decision MUST memiliki sufficient record
untuk reconstruction.

### Assured / High-Assurance

**AOF-POL-016** --- High-assurance policy store/evaluator MUST memiliki
protection terhadap unauthorized mutation.

**AOF-POL-017** --- High-assurance Effect Boundary SHOULD memastikan
applicable policy decision belum stale.

**AOF-POL-018** --- High-assurance policy overrides MUST subject to
independent approval/review sesuai profile.

------------------------------------------------------------------------

## 12.40 Policy Invariants

Numbering final akan direkonsiliasi pada canonical Invariant Registry.

### POL-INV-01 --- Policy Mediation

\[ Consequential(x)\Rightarrow PolicyEvaluated(x) \]

### POL-INV-02 --- Policy Non-Authority

\[ PolicyAllow\not\Rightarrow AuthorityGrant\]

### POL-INV-03 --- Restrictive Dominance

\[ Conflict(P)\Rightarrow DeterministicRestrictiveResolution\]

secara default.

### POL-INV-04 --- No Implicit Allow

\[ UnknownMandatoryPolicy\Rightarrow\neg Allow\]

### POL-INV-05 --- Policy Inheritance

\[ ChildTask\Rightarrow PreserveApplicableMandatoryPolicy\]

### POL-INV-06 --- Override Control

\[
Override(p)\Rightarrow Authorized\land Scoped\land Traceable
\]

### POL-INV-07 --- Prompt Non-Enforcement

\[ PromptPolicy\not\equiv EnforcedPolicy\]

### POL-INV-08 --- Policy Version Traceability

\[ ConsequentialDecision\Rightarrow TraceablePolicyVersion\]

### POL-INV-09 --- Untrusted Context Non-Mutation

\[ UntrustedContent\not\Rightarrow PolicyMutation\]

### POL-INV-10 --- Replan Reevaluation

\[ MaterialPolicyScopeChange\Rightarrow ReevaluatePolicy\]

------------------------------------------------------------------------

## 12.41 Architecture Integration

Policy Evaluator merupakan logical component dari `Safety Kernel`.

\[ K\supset eq PolicyEvaluator\]

Reference interaction:

```text
Proposal / Candidate Action
          |
          v
    Policy Evaluator
          |
          +--> Applicable Policy Resolution
          +--> Condition Evaluation
          +--> Effect Collection
          +--> Conflict Resolution
          +--> Override Validation
          |
          v
      Policy Result
          |
          +--> Allow
          +--> Deny
          +--> RequireVerification
          +--> RequireApproval
          +--> Escalate
          +--> Pending
```

Policy result kemudian dikombinasikan dengan Authority, Risk, State, dan
Verification requirements.

------------------------------------------------------------------------

## 12.42 Policy Freeze Candidate Criteria

Policy area MAY dinyatakan `Freeze Candidate` jika:

1.  policy definition dan lifecycle stabil;
2.  applicability semantics stabil;
3.  policy-authority separation stabil;
4.  policy-risk relationship stabil;
5.  policy-verification/approval relationship stabil;
6.  conflict-resolution semantics stabil;
7.  inheritance/override/exception semantics stabil;
8.  policy versioning/revalidation compatible dengan Architecture;
9.  policy enforcement tidak bergantung pada prompt-only control;
10. conformance requirements dapat dipetakan ke tests;
11. tidak ada contradiction dengan Authority, Risk, State, Security, dan
    Human Governance.

------------------------------------------------------------------------

## 12.43 Policy Formalization Result

Policy v1.0 RC-Policy diringkas sebagai:

\[ Policy= ExplicitRules + Applicability + DeterministicEvaluation +
ConflictResolution + ControlledOverride + VersionedEnforcement +
Traceability \]

dengan:

\[
\boxed{ Policy\ Constrains\ Authority,\ But\ Does\ Not\ Create\ It }
\]

\[ \boxed{ Unknown\ Mandatory\ Policy\ State\neq Allow } \]

\[ \boxed{ Policy\ in\ Prompt\neq Policy\ Enforcement } \]

dan:

\[
\boxed{ Consequential\ Action\Rightarrow Applicable\ Policy\ Evaluation }
\] \# 13. Risk Requirements

## 13.1 Purpose

`Risk Model` mendefinisikan bagaimana AOF mengidentifikasi, menilai,
mengendalikan, memperbarui, menerima, mengeskalasi, dan menelusuri
uncertainty serta potential harm yang terkait dengan `Task`, `Decision`,
`Action`, `Resource`, `Agent`, `Context`, dan `Outcome`.

Risk tidak memberikan permission.

\[ Risk\neq Authority\neq Policy\]

Risk mempengaruhi tingkat control yang diperlukan:

\[
Risk\uparrow\Rightarrow ControlStrength\uparrow
\]

Canonical principle:

\[ Autonomy\propto\frac{1}{Risk} \]

sebagai conceptual relation, bukan mandatory numeric formula.

------------------------------------------------------------------------

## 13.2 Risk Definition

Canonical risk object:

\[ \rho= \langle id, subject, hazard, likelihood,
impact, exposure, classification, controls, residual, owner, acceptance,
state, provenance \rangle\]

dengan:

-   `subject`: Task, Action, Resource, Decision, atau Outcome yang
    dinilai;
-   `hazard`: adverse event atau failure condition;
-   `likelihood`: kemungkinan hazard;
-   `impact`: consequence jika hazard terjadi;
-   `exposure`: contextual exposure;
-   `classification`: normalized risk class;
-   `controls`: preventive/detective/corrective controls;
-   `residual`: risk setelah controls;
-   `owner`: accountable risk owner jika applicable;
-   `acceptance`: risk acceptance record jika diperlukan;
-   `state`: lifecycle state;
-   `provenance`: source dan assessment history.

------------------------------------------------------------------------

## 13.3 Risk Profile Contract

Implementation yang mengklaim risk-aware conformance MUST memiliki
`Risk Profile` atau equivalent contract.

Minimum fields:

```text
profile_id
version
scope
classification_method
risk_levels
impact_dimensions
likelihood_scale
thresholds
control_mapping
reassessment_triggers
residual_risk_rules
acceptance_rules
escalation_rules
```

**AOF-RISK-001** --- Risk classification method MUST explicit dan
reproducible pada tingkat yang sesuai dengan domain.

------------------------------------------------------------------------

## 13.4 Reference Risk Classes

AOF reference classes:

`Low`, `Moderate`, `High`, `Critical`.

Reference control mapping:

  Risk       Minimum Reference Control
  ---------- ----------------------------------------------
  Low        Self-check / standard policy controls
  Moderate   Policy Gate + evidence capture
  High       Independent Verification
  Critical   Independent Verification + Explicit Approval

Mapping ini merupakan baseline. Domain profile MAY memperketat mapping.

Domain profile MUST NOT melemahkan mandatory control tanpa explicit
justified profile semantics.

------------------------------------------------------------------------

## 13.5 Likelihood and Impact

Risk MAY dihitung secara qualitative, ordinal, semi-quantitative, atau
quantitative.

Reference conceptual function:

\[ Risk=f(Likelihood,Impact,Exposure) \]

AOF tidak mewajibkan satu scoring formula universal.

Implementation MUST mendefinisikan bagaimana input tersebut dipetakan ke
risk class.

------------------------------------------------------------------------

## 13.6 Impact Dimensions

Impact SHOULD mempertimbangkan dimensions yang relevan, misalnya:

-   confidentiality;
-   integrity;
-   availability;
-   safety;
-   privacy;
-   financial;
-   legal/regulatory;
-   operational;
-   reputational;
-   human impact;
-   irreversible external effect;
-   blast radius.

Domain MAY menambahkan dimensions lain.

------------------------------------------------------------------------

## 13.7 Risk Subject

Risk assessment MUST memiliki identifiable subject.

Possible subjects:

\[ RiskSubject= { Task, Action, Decision, Resource, AgentAssignment,
ContextTransfer, Delegation, Outcome } \]

Session-level risk MAY merupakan aggregation dari component risks.

------------------------------------------------------------------------

## 13.8 Inherent and Residual Risk

AOF membedakan:

\[ Risk\_{inherent} \]

dan:

\[ Risk\_{residual} = Risk\_{inherent}-Effectiveness(Controls) \]

Notasi subtraction bersifat conceptual.

Control effectiveness MUST NOT diasumsikan tanpa evidence atau justified
basis ketika residual risk menentukan consequential governance decision.

------------------------------------------------------------------------

## 13.9 Risk Classification

Risk classification SHOULD menghasilkan:

```text
risk_id
subject
class
basis
impact
likelihood
exposure
controls
residual_class
assessor
timestamp
```

Classification MUST traceable untuk High/Critical consequential action.

------------------------------------------------------------------------

## 13.10 Risk and Authority

Risk tidak dapat menciptakan authority.

\[ LowRisk\not\Rightarrow Authority\]

\[ CriticalRisk\not\Rightarrow EmergencyAuthority\]

Risk MAY menyebabkan authority lebih sempit atau tidak usable melalui
policy/control decision.

**AOF-RISK-002** --- Risk result MUST NOT digunakan sebagai substitute
untuk missing authority.

------------------------------------------------------------------------

## 13.11 Risk and Policy

Policy menentukan response terhadap risk.

Example:

\[ Risk=High\Rightarrow RequireIndependentVerification\]

\[ Risk=Critical\Rightarrow RequireApproval\]

Risk Gate menghasilkan risk evaluation; Policy Evaluator menentukan
applicable governance rule jika policy-based mapping digunakan.

Implementations MAY mengintegrasikan evaluators secara fisik, tetapi
semantic distinction MUST dipertahankan.

------------------------------------------------------------------------

## 13.12 Risk and Autonomy

Effective autonomy MUST bounded oleh risk.

Reference:

\[ A\_{eff} = min( A\_{configured}, A\_{authority}, A\_{policy},
A\_{risk} ) \]

Higher risk MAY:

-   reduce allowed autonomous operations;
-   increase verification;
-   require approval;
-   restrict resources;
-   shorten authority validity;
-   increase observability;
-   require Human involvement.

------------------------------------------------------------------------

## 13.13 Risk and Verification

Verification strength SHOULD meningkat dengan residual risk dan
consequence severity.

Reference:

```text
Low      -> Self / deterministic checks acceptable
Moderate -> Policy-directed verification
High     -> Independent verification
Critical -> Independent verification + explicit approval
```

Self-verification alone MUST NOT dianggap sufficient jika applicable
profile mensyaratkan independence.

------------------------------------------------------------------------

## 13.14 Risk and Evidence

Risk assessment SHOULD menggunakan evidence yang proportionate terhadap
consequence.

High/Critical classification atau acceptance SHOULD memiliki sufficient
evidence untuk independent reconstruction.

Unverified agent assertion MAY menjadi assessment input, tetapi MUST NOT
otomatis menjadi verified risk fact.

------------------------------------------------------------------------

## 13.15 Risk and Context

Context dapat mengubah risk secara material.

Examples:

-   environment berubah dari staging ke production;
-   data berubah dari Internal ke Restricted;
-   target berubah dari test resource ke customer-facing resource;
-   external service ditambahkan;
-   blast radius meningkat.

\[ ContextChange\Rightarrow PotentialRiskChange\]

Material context change MUST memicu reassessment sesuai Risk Profile.

------------------------------------------------------------------------

## 13.16 Risk and State

Risk merupakan bagian consequential orchestration state.

\[ s_t\supset eq Risks_t \]

Risk change yang mempengaruhi control MUST committed melalui controlled
transition dan traceable.

Agent private risk estimate MAY menjadi proposal, tetapi authoritative
risk state harus melalui applicable governance mechanism.

------------------------------------------------------------------------

## 13.17 Dynamic Risk

Risk tidak immutable selama session.

\[ Risk\_{t_0}\neq Risk\_{t_1} \]

Dynamic triggers MAY mencakup:

-   failed verification;
-   repeated retry;
-   new evidence;
-   changed resource;
-   changed agent;
-   changed environment;
-   partial effect;
-   unexpected tool output;
-   security signal;
-   authority change;
-   policy change;
-   expanded task scope.

**AOF-RISK-003** --- Material risk change MUST memicu control
reevaluation sebelum new consequential effect.

------------------------------------------------------------------------

## 13.18 Risk Escalation

Jika risk melewati configured threshold:

\[ Risk\geq Threshold\_{escalation} \Rightarrow Escalate
\]

atau stronger control sesuai profile.

Escalation package SHOULD mencakup:

-   current risk;
-   prior risk;
-   trigger;
-   evidence;
-   controls already applied;
-   residual risk;
-   requested decision.

------------------------------------------------------------------------

## 13.19 Risk Acceptance

Risk acceptance adalah explicit governance decision untuk menerima
residual risk.

\[ RiskAcceptance\neq RiskAssessment\]

Acceptance MUST dilakukan oleh actor dengan valid acceptance authority.

**AOF-RISK-004** --- Agent yang menilai risk MUST NOT dianggap otomatis
authorized menerima residual risk.

Acceptance SHOULD memuat:

```text
risk_id
residual_risk
accepted_by
authority_basis
scope
rationale
validity
conditions
timestamp
```

------------------------------------------------------------------------

## 13.20 Risk Acceptance Authority

Acceptance authority MAY bergantung pada risk class.

Example:

```text
Low      -> operational actor
Moderate -> delegated owner
High     -> designated governance authority
Critical -> explicit senior/organizational authority
```

AOF tidak mewajibkan organizational hierarchy tertentu.

Profile MUST menentukan acceptance authority untuk High/Critical risk
jika acceptance diperbolehkan.

------------------------------------------------------------------------

## 13.21 Non-Acceptable Risk

Policy/profile MAY mendefinisikan risk yang tidak dapat diterima.

\[ Risk\in NonAcceptableSet\Rightarrow Reject/Abort \]

No approval SHOULD dapat mengubah prohibited risk menjadi allowed
kecuali governance model secara explicit menyediakan
legally/organizationally valid override.

------------------------------------------------------------------------

## 13.22 Risk Treatment

Reference treatment options:

-   `Avoid`;
-   `Reduce`;
-   `Transfer`;
-   `Accept`;
-   `Escalate`.

Untuk orchestration, `Reduce` MAY dilakukan melalui:

-   narrower scope;
-   stronger verification;
-   safer tool;
-   deterministic control;
-   sandbox;
-   Human review;
-   staged execution;
-   rollback capability;
-   reduced blast radius.

------------------------------------------------------------------------

## 13.23 Risk Control Mapping

Risk Profile SHOULD memetakan class ke required controls.

Example:

``` yaml
High:
  verification:
    independence: required
  approval:
    required: false
  execution:
    staged: true
  trace:
    enhanced: true
```

Control mapping MUST explicit agar conformance test dapat menentukan
expected behavior.

------------------------------------------------------------------------

## 13.24 Risk and Irreversibility

Irreversibility SHOULD menjadi impact multiplier atau explicit
assessment factor.

Examples:

-   destructive delete;
-   public publication;
-   financial transfer;
-   production deployment;
-   external disclosure;
-   irreversible infrastructure change.

High irreversibility SHOULD meningkatkan required assurance meskipun
likelihood rendah.

------------------------------------------------------------------------

## 13.25 Blast Radius

Risk SHOULD mempertimbangkan potential blast radius.

\[ BlastRadius= AffectedResources+AffectedUsers+AffectedDomains \]

Broad blast radius SHOULD meningkatkan control strength atau mendorong
staged execution.

------------------------------------------------------------------------

## 13.26 Risk and Data Sensitivity

Sensitive data operation SHOULD mempertimbangkan:

-   classification;
-   destination;
-   retention;
-   disclosure;
-   external processing;
-   aggregation risk;
-   re-identification risk.

Data sensitivity MAY meningkatkan risk walaupun operation hanya `Read`.

------------------------------------------------------------------------

## 13.27 Risk and External Services

External service menambah trust boundary dan MAY meningkatkan:

-   confidentiality risk;
-   availability dependency;
-   supply-chain risk;
-   policy uncertainty;
-   evidence uncertainty.

Use of external service SHOULD masuk dalam risk assessment jika
material.

------------------------------------------------------------------------

## 13.28 Risk and Agent Selection

Agent selection SHOULD mempertimbangkan risk compatibility.

\[ Assignable(a,t) \Rightarrow RiskProfileCompatible(a,t) \]

High-risk task MAY mensyaratkan:

-   observed capability;
-   stronger trust evidence;
-   narrower context;
-   lower autonomy;
-   independent verifier.

------------------------------------------------------------------------

## 13.29 Risk and Delegation

Delegation MAY mengubah risk karena:

-   new actor;
-   new context disclosure;
-   new trust boundary;
-   longer authority chain;
-   increased coordination complexity.

Material delegation SHOULD memicu risk reassessment jika Risk Profile
mensyaratkannya.

------------------------------------------------------------------------

## 13.30 Risk and Retry

Repeated failure dapat meningkatkan risk.

\[
RetryCount\uparrow\Rightarrow PotentialRisk\uparrow
\]

Risk Profile SHOULD menentukan retry thresholds yang memicu:

-   stronger verification;
-   replan;
-   escalation;
-   abort.

------------------------------------------------------------------------

## 13.31 Risk and Replan

Replan MUST mempertahankan atau memperbarui risk assessment jika plan
materially berubah.

\[ MaterialPlanChange\Rightarrow ReassessRisk\]

New plan MUST NOT mewarisi old risk classification secara blind.

------------------------------------------------------------------------

## 13.32 Risk and Partial Effect

Partial effect dapat menciptakan state yang lebih berisiko daripada
pre-action state.

Jika partial effect terdeteksi:

1.  capture evidence;
2.  reconcile state;
3.  reassess risk;
4.  determine compensation/containment;
5.  re-evaluate further execution.

------------------------------------------------------------------------

## 13.33 Risk and Verification Failure

Verification failure atau inconclusive result MAY meningkatkan residual
risk.

\[ Verification=Rejected \Rightarrow NoSuccessfulCompletion \]

dan MAY memicu:

-   replan;
-   stronger verification;
-   rollback;
-   escalation;
-   abort.

------------------------------------------------------------------------

## 13.34 Risk Budget

Deployment MAY menggunakan risk budget untuk membatasi cumulative
exposure.

\[ CumulativeExposure\leq RiskBudget\]

Risk budget MAY diterapkan pada:

-   session;
-   task;
-   environment;
-   resource;
-   time window.

Exceeding budget MUST menghasilkan configured control response.

------------------------------------------------------------------------

## 13.35 Failure Budget and Risk

Failure budget berbeda dari risk budget.

`Failure Budget` membatasi tolerated failures/retries.

`Risk Budget` membatasi tolerated exposure.

Keduanya MAY berinteraksi:

\[ FailureCount\uparrow\Rightarrow RiskReassessment \]

------------------------------------------------------------------------

## 13.36 Cost-Risk Interaction

Cost optimization MUST NOT menurunkan mandatory safety control.

\[ CostOptimization\not\Rightarrow SafetyControlRemoval
\]

Policy MAY memilih cheaper model/tool untuk Low risk, tetapi
High/Critical control requirements tetap berlaku.

------------------------------------------------------------------------

## 13.37 Risk Provenance

Risk assessment SHOULD mempertahankan:

-   assessor;
-   method/profile;
-   evidence inputs;
-   timestamp;
-   state/context version;
-   prior assessment;
-   change reason.

\[ RiskDecision\Rightarrow Provenance\]

untuk consequential High/Critical operations.

------------------------------------------------------------------------

## 13.38 Risk Trace Events

Reference events:

-   `RiskAssessmentRequested`;
-   `RiskClassified`;
-   `RiskReassessed`;
-   `RiskIncreased`;
-   `RiskReduced`;
-   `RiskControlApplied`;
-   `ResidualRiskCalculated`;
-   `RiskAccepted`;
-   `RiskRejected`;
-   `RiskEscalated`.

------------------------------------------------------------------------

## 13.39 Risk Failure Modes

### RISK-F01 --- Missing Assessment

Required risk assessment tidak tersedia.

### RISK-F02 --- Stale Assessment

Assessment tidak mencerminkan material context/state change.

### RISK-F03 --- Unsupported Classification

Risk class tidak memiliki sufficient basis.

### RISK-F04 --- Control Mapping Failure

Required control tidak dapat ditentukan.

### RISK-F05 --- Unauthorized Acceptance

Residual risk diterima oleh actor tanpa authority.

### RISK-F06 --- Risk Underclassification

Risk ditetapkan terlalu rendah akibat missing factors.

### RISK-F07 --- Risk Drift

Actual exposure berubah tetapi classification tidak diperbarui.

### RISK-F08 --- Evidence Failure

Risk basis tidak dapat diverifikasi.

### RISK-F09 --- Aggregation Failure

Cumulative risk tidak terdeteksi.

### RISK-F10 --- Control Effectiveness Assumption

Residual risk dianggap rendah tanpa basis control effectiveness.

Mandatory risk failure MUST NOT silently fail-open.

------------------------------------------------------------------------

## 13.40 Reference Risk Evaluation Algorithm

```text
INPUT:
  subject
  action
  resource
  context
  state
  evidence
  applicable Risk Profile

1. Identify hazards.
2. Determine impact dimensions.
3. Estimate likelihood.
4. Determine exposure.
5. Compute/classify inherent risk.
6. Identify existing controls.
7. Evaluate control applicability/effectiveness.
8. Determine residual risk.
9. Map residual risk to required controls.
10. Check acceptance/escalation thresholds.
11. Record assessment provenance.
12. Return:
      risk class
      residual risk
      required controls
      reassessment triggers
      acceptance requirement
```

------------------------------------------------------------------------

## 13.41 Risk Gate

`Risk Gate` adalah logical Safety Kernel component.

\[ K\supset eq RiskGate\]

Reference result:

\[
RiskGate(x,s)\rightarrow { Acceptable, ControlRequired, Escalate, Reject, Pending }
\]

`Acceptable` berarti risk predicate satisfied; bukan authority grant.

------------------------------------------------------------------------

## 13.42 Risk Conformance Requirements

### Core

**AOF-RISK-003 (canonical cross-reference)** — See the primary normative definition above.
reevaluation.

**AOF-RISK-005** --- Applicable Risk Profile MUST menentukan risk levels
dan control mapping.

**AOF-RISK-006** --- Required risk assessment yang unresolved MUST NOT
menjadi implicit permission.

**AOF-RISK-007** --- High/Critical consequential risk decision MUST
traceable.

### Governed

**AOF-RISK-008** --- Residual risk MUST mempertimbangkan applicable
controls.

**AOF-RISK-009** --- Material replan MUST memicu risk reassessment.

**AOF-RISK-010** --- Partial effect MUST memicu state reconciliation dan
risk reassessment jika material.

**AOF-RISK-011** --- Risk acceptance MUST scoped, authorized, dan
traceable.

**AOF-RISK-012** --- Non-acceptable risk MUST menghasilkan reject/abort
atau explicit valid governance path.

**AOF-RISK-013** --- Retry threshold SHOULD memicu
reassessment/escalation sesuai Risk Profile.

**AOF-RISK-014** --- Risk-sensitive Agent selection SHOULD
mempertimbangkan agent risk compatibility.

### Assured / High-Assurance

**AOF-RISK-015** --- High risk MUST menggunakan independent verification
jika required oleh AOF reference profile.

**AOF-RISK-016** --- Critical risk MUST menggunakan independent
verification dan explicit approval kecuali stricter domain prohibition
berlaku.

**AOF-RISK-017** --- High-assurance Risk Profile MUST menentukan
evidence expectations untuk risk classification dan acceptance.

**AOF-RISK-018** --- High-assurance implementation MUST menentukan
revalidation behavior pada Effect Boundary untuk dynamic risk.

------------------------------------------------------------------------

## 13.43 Risk Invariants

### RISK-INV-01 --- Risk-Proportional Control

\[
Risk\uparrow\Rightarrow ControlStrength\uparrow
\]

### RISK-INV-02 --- Risk Non-Authority

\[ RiskResult\not\Rightarrow Authority\]

### RISK-INV-03 --- Dynamic Reassessment

\[ MaterialRiskTrigger\Rightarrow Reassess\]

### RISK-INV-04 --- Acceptance Separation

\[ AssessRisk\neq AcceptRisk\]

### RISK-INV-05 --- Residual Risk Accountability

\[ AcceptedResidualRisk\Rightarrow AuthorizedAcceptance\]

### RISK-INV-06 --- High-Risk Assurance

\[ HighRisk\Rightarrow IndependentVerification\]

sesuai reference profile.

### RISK-INV-07 --- Critical-Risk Governance

\[
CriticalRisk\Rightarrow IndependentVerification\land ExplicitApproval
\]

sesuai reference profile.

### RISK-INV-08 --- No Stale Risk

\[
MaterialContextChange\Rightarrow\neg BlindReuse(RiskAssessment)
\]

### RISK-INV-09 --- Partial Effect Reassessment

\[ PartialEffect\Rightarrow Reconcile+Reassess \]

### RISK-INV-10 --- Cost Non-Dominance

\[
CostOptimization\not\Rightarrow MandatoryControlRemoval
\]

------------------------------------------------------------------------

## 13.44 Cross-Domain Integration

Risk Model mengikat:

```text
Authority
   |
Policy
   |
Risk Gate
   |
State Validation
   |
Verification Requirements
   |
Effect Boundary
```

Namun semantic ordering MAY dioptimalkan.

Canonical condition tetap:

\[ ExecuteAllowed=
C\land H\land P\land S\land R\land V
\]

Risk Gate tidak menggantikan predicate lain.

------------------------------------------------------------------------

## 13.45 Risk Freeze Candidate Criteria

Risk area MAY dinyatakan `Freeze Candidate` jika:

1.  Risk Profile Contract stabil;
2.  classification method semantics stabil;
3.  risk classes dan control mapping stabil;
4.  inherent/residual distinction stabil;
5.  dynamic reassessment triggers stabil;
6.  risk acceptance authority semantics stabil;
7.  Risk--Authority dan Risk--Policy separation stabil;
8.  High/Critical assurance mapping compatible dengan Verification;
9.  partial effect/retry/replan integration compatible dengan Failure &
    Recovery;
10. conformance requirements dapat dipetakan ke tests;
11. domain profiles dapat memperketat tanpa merusak core semantics.

------------------------------------------------------------------------

## 13.46 Risk Formalization Result

Risk v1.0 RC-Risk diringkas sebagai:

\[ RiskGovernance= Assess + Classify + Control + Reassess +
Accept/Escalate + Trace \]

dengan:

\[ \boxed{ Risk\ Does\ Not\ Grant\ Authority } \]

\[ \boxed{ Higher\ Risk\ Requires\ Stronger\ Control } \]

\[ \boxed{ Material\ Change\ Requires\ Risk\ Reassessment } \]

dan:

\[
\boxed{ Residual\ Risk\ Acceptance\ Requires\ Valid\ Governance\ Authority }
\] \# 14. Evidence Requirements

## 14.1 Purpose

`Evidence Model` mendefinisikan information object yang digunakan untuk
mendukung atau menyangkal `Claim`, membuktikan execution/effect,
mendukung `Verification`, merekonstruksi `Decision`, menilai `Risk`, dan
menunjukkan `Conformance`.

Canonical principle:

\[ Claim\neq Evidence\neq Verification\]

`Claim` menyatakan sesuatu. `Evidence` menyediakan support material.
`Verification` mengevaluasi claim terhadap criteria menggunakan
evidence.

\[ Evidence\not\Rightarrow Verified\]

Evidence dapat valid tetapi insufficient, irrelevant, stale, dependent,
atau contradictory.

------------------------------------------------------------------------

## 14.2 Evidence Definition

Canonical evidence object:

\[ e= \langle id, source, claim, content, provenance, integrity,
freshness, confidence, classification, scope, timestamp, relations
\rangle\]

dengan:

-   `id`: stable evidence identity;
-   `source`: origin;
-   `claim`: claim yang didukung/disangkal;
-   `content`: evidence payload atau durable reference;
-   `provenance`: origin dan derivation chain;
-   `integrity`: integrity metadata;
-   `freshness`: temporal relevance;
-   `confidence`: source/assessment confidence jika applicable;
-   `classification`: sensitivity/trust classification;
-   `scope`: applicability boundary;
-   `timestamp`: creation/observation time;
-   `relations`: dependencies, supersession, corroboration,
    contradiction.

**AOF-EVD-001** --- Evidence yang digunakan untuk consequential
verification MUST memiliki identifiable source dan provenance yang cukup
untuk applicable profile.

------------------------------------------------------------------------

## 14.3 Evidence vs Claim

Agent output, tool output, Human statement, test result, log, artifact,
dan observation dapat mengandung claims.

Contoh:

```text
Claim:
"Deployment completed successfully."

Possible Evidence:
- deployment job result;
- target version observation;
- health check;
- artifact digest;
- production endpoint verification.
```

Satu claim MAY memerlukan multiple evidence items.

\[ Claim(c)\rightarrow{e_1,e_2,\ldots,e_n} \]

------------------------------------------------------------------------

## 14.4 Evidence Sources

Evidence source MAY berupa:

-   deterministic tool;
-   external service;
-   Agent;
-   Human;
-   state store;
-   trace store;
-   test system;
-   scanner;
-   monitoring system;
-   signed artifact;
-   database observation;
-   runtime observation;
-   document;
-   independent verifier.

Source type MUST NOT dengan sendirinya menentukan truth.

\[ SourceIdentity\neq TruthGuarantee\]

------------------------------------------------------------------------

## 14.5 Evidence Provenance

Evidence provenance SHOULD menjawab:

-   siapa/apa menghasilkan evidence;
-   kapan;
-   dari resource/context apa;
-   melalui operation apa;
-   transformasi apa yang terjadi;
-   evidence parent apa yang digunakan;
-   actor/tool/version apa yang terlibat.

Conceptual:

\[ Provenance(e)= Origin+Derivation+Transformation+Custody \]

**AOF-EVD-002** --- Derived evidence MUST preserve reference ke relevant
source evidence atau derivation basis jika derivation material terhadap
verification.

------------------------------------------------------------------------

## 14.6 Evidence Integrity

Integrity menunjukkan apakah evidence tetap konsisten dengan
captured/declared form.

Possible controls MAY mencakup:

-   digest/hash;
-   signature;
-   append-only storage;
-   protected database;
-   immutable object version;
-   authenticated source;
-   access-controlled audit store.

AOF tidak mewajibkan cryptographic mechanism untuk seluruh evidence.

High-assurance profile SHOULD menggunakan stronger integrity controls
untuk consequential evidence.

------------------------------------------------------------------------

## 14.7 Evidence Freshness

Evidence dapat menjadi stale.

\[ ValidAt(e,t_1)\not\Rightarrow ValidAt(e,t_2) \]

Evidence profile SHOULD menentukan freshness requirement jika
state/resource berubah seiring waktu.

Contoh:

-   dependency vulnerability scan dari enam bulan lalu mungkin tidak
    cukup untuk release saat ini;
-   authority status observation sebelum revocation mungkin stale;
-   health check sebelum deployment tidak membuktikan post-deployment
    health.

**AOF-EVD-003** --- Stale evidence MUST NOT digunakan sebagai sole
support jika applicable criteria mensyaratkan fresher observation.

------------------------------------------------------------------------

## 14.8 Evidence Relevance

Evidence harus relevan terhadap claim.

\[ Relevant(e,c)\rightarrow{true,false,partial} \]

Evidence bahwa build berhasil tidak otomatis membuktikan security
requirements terpenuhi.

Evidence relevance SHOULD dinilai terhadap explicit verification
criteria.

------------------------------------------------------------------------

## 14.9 Evidence Independence

Evidence independence menunjukkan seberapa jauh evidence tidak
bergantung pada source/process yang sedang dinilai.

Reference levels:

-   `EI0` --- self-produced;
-   `EI1` --- same execution domain, separate mechanism;
-   `EI2` --- separate agent/tool or control path;
-   `EI3` --- organizationally/administratively independent or
    externally anchored.

Evidence independence berbeda dari verifier independence, tetapi
keduanya dapat berinteraksi.

------------------------------------------------------------------------

## 14.10 Evidence Confidence

Confidence MAY digunakan sebagai metadata, tetapi:

\[ Confidence\neq Verification\]

Agent-reported confidence MUST NOT menggantikan required evidence.

Confidence SHOULD memiliki defined semantics jika digunakan dalam
automated governance.

------------------------------------------------------------------------

## 14.11 Evidence Quality

Reference quality function:

\[ Q_e= f( Provenance, Integrity, Relevance, Freshness, Independence )
\]

Implementation MAY menambahkan completeness, precision, reproducibility,
atau domain-specific dimensions.

AOF tidak mewajibkan universal numeric score.

------------------------------------------------------------------------

## 14.12 Evidence Admissibility

`Admissibility` menentukan apakah evidence boleh digunakan untuk
verification tertentu.

\[ Admissible(e,c,k)\rightarrow{true,false,conditional} \]

dengan (k) sebagai verification criteria/profile.

Evidence MAY inadmissible karena:

-   source tidak allowed;
-   provenance missing;
-   integrity unknown;
-   stale;
-   wrong environment;
-   wrong resource;
-   self-generated ketika independence required;
-   sensitivity restrictions;
-   unverifiable transformation.

**AOF-EVD-004** --- Verification MUST NOT memperlakukan inadmissible
evidence sebagai sufficient evidence.

------------------------------------------------------------------------

## 14.13 Evidence Sufficiency

Sufficiency adalah property dari evidence set terhadap claim/criteria.

\[ Sufficient(E,c,k)\rightarrow{true,false,inconclusive} \]

Satu high-quality evidence item MAY cukup untuk simple deterministic
claim.

Complex/high-risk claim MAY membutuhkan corroboration.

\[ EvidencePresent\not\Rightarrow EvidenceSufficient\]

------------------------------------------------------------------------

## 14.14 Corroboration

Corroboration menggunakan multiple evidence items yang independently
mendukung claim.

\[ Corroborated(c)=Support(e_1,c)\land Support(e_2,c) \]

Jika (e_1) dan (e_2) berasal dari same underlying source, independence
MAY rendah walaupun jumlah evidence dua.

Implementation SHOULD menghindari false corroboration.

------------------------------------------------------------------------

## 14.15 Contradictory Evidence

Evidence set dapat mengandung contradiction.

\[ Support(e_i,c)\land Reject(e_j,c) \]

Contradiction MUST NOT silently diabaikan jika material.

Possible outcomes:

-   collect more evidence;
-   mark verification `Inconclusive`;
-   escalate;
-   replan;
-   reject claim.

**AOF-EVD-005** --- Material contradictory evidence MUST
direpresentasikan dalam verification input atau explicitly resolved
dengan traceable rationale.

------------------------------------------------------------------------

## 14.16 Negative Evidence and Absence

Absence of evidence berbeda dari evidence of absence.

\[ NoEvidence(c)\neq Evidence(\neg c) \]

Missing expected evidence MAY menjadi failure condition jika evidence
tersebut mandatory.

------------------------------------------------------------------------

## 14.17 Evidence Collection

Evidence SHOULD dikumpulkan sedekat mungkin dengan event/effect yang
dibuktikan jika practical.

Reference flow:

```text
Action / Observation
        |
        v
Evidence Capture
        |
        v
Source + Provenance Binding
        |
        v
Integrity / Freshness Metadata
        |
        v
Evidence Store / Durable Reference
```

------------------------------------------------------------------------

## 14.18 Effect Evidence

Consequential `Action` SHOULD menghasilkan evidence yang membedakan:

-   request accepted;
-   execution started;
-   execution completed;
-   target state observed;
-   intended effect confirmed;
-   unintended effect observed.

\[ ExecutionResult\neq EffectEvidence\]

Contoh API `200 OK` tidak selalu membuktikan intended downstream effect.

------------------------------------------------------------------------

## 14.19 Decision Evidence

Consequential `Decision` SHOULD memiliki evidence yang cukup untuk
menunjukkan basis yang relevan:

-   applicable authority result;
-   applicable policy result;
-   risk result;
-   state version;
-   verification/approval requirements;
-   decision actor/evaluator;
-   timestamp.

Decision evidence tidak memerlukan private chain-of-thought.

------------------------------------------------------------------------

## 14.20 Authority Evidence

Authority evidence MAY mencakup:

-   grant ID;
-   issuer;
-   subject;
-   operation/resource scope;
-   validity;
-   status;
-   delegation chain;
-   evaluation result.

Authority evidence MUST distinguish nominal grant dari effective valid
authority at decision time.

------------------------------------------------------------------------

## 14.21 Policy Evidence

Policy evidence MAY mencakup:

-   policy IDs;
-   versions;
-   applicability;
-   effects;
-   conflict-resolution result;
-   override/exception;
-   final policy result.

------------------------------------------------------------------------

## 14.22 Risk Evidence

Risk evidence SHOULD mencakup basis classification dan residual risk
yang relevant.

High/Critical risk acceptance SHOULD preserve evidence yang mendukung
assessment dan acceptance decision.

------------------------------------------------------------------------

## 14.23 Verification Evidence

Verification menghasilkan evidence tentang verification process itu
sendiri, seperti:

-   criteria;
-   evidence set;
-   verifier;
-   method;
-   result;
-   independence level;
-   timestamp;
-   confidence jika applicable.

Verification result dapat menjadi evidence untuk downstream decision,
tetapi tidak otomatis membuktikan claims di luar verification scope.

------------------------------------------------------------------------

## 14.24 Human-Generated Evidence

Human review/approval MAY menghasilkan evidence.

Human evidence SHOULD memiliki:

-   actor identity;
-   role/authority basis jika relevant;
-   subject;
-   decision;
-   timestamp;
-   scope;
-   rationale atau structured reason jika required.

Human statement tidak otomatis memiliki stronger truth status daripada
deterministic evidence.

------------------------------------------------------------------------

## 14.25 Agent-Generated Evidence

Agent-generated output MAY menjadi evidence candidate.

Default:

\[ AgentOutput=UntrustedProposal \]

untuk control semantics.

Agent-generated evidence MAY diterima jika verification profile
mengizinkannya dan provenance/scope tersedia.

High-risk claim SHOULD NOT bergantung hanya pada self-generated agent
evidence jika independence required.

------------------------------------------------------------------------

## 14.26 Tool-Generated Evidence

Tool output SHOULD mempertahankan:

-   tool identity;
-   version jika material;
-   invocation parameters;
-   target;
-   timestamp;
-   result;
-   error state;
-   execution identity jika available.

Tool output dapat salah atau incomplete; verification criteria
menentukan admissibility.

------------------------------------------------------------------------

## 14.27 Evidence Transformation

Evidence MAY ditransformasi melalui parsing, summarization, aggregation,
normalization, atau extraction.

Derived evidence:

\[ e_d=Transform(e_s) \]

SHOULD mempertahankan:

-   source reference;
-   transform identity/method;
-   transform version jika material;
-   timestamp;
-   transformation result.

Lossy transformation SHOULD ditandai jika dapat mempengaruhi
verification.

------------------------------------------------------------------------

## 14.28 Evidence Aggregation

Evidence aggregation MAY menghasilkan summary atau composite evidence.

Aggregation MUST NOT menghilangkan material contradiction atau
provenance yang diperlukan.

\[ Aggregate(E)\not\Rightarrow Erase(Provenance(E)) \]

------------------------------------------------------------------------

## 14.29 Evidence Chain

Complex workflow MAY memiliki evidence chain:

```text
Source Artifact
    |
    v
Build Evidence
    |
    v
Test Evidence
    |
    v
Verification Result
    |
    v
Approval Evidence
    |
    v
Release Evidence
```

Each link SHOULD retain references sehingga accountability chain dapat
direkonstruksi.

------------------------------------------------------------------------

## 14.30 Evidence Store

Evidence Store MAY menyimpan payload atau durable references.

Evidence storage SHOULD mempertimbangkan:

-   integrity;
-   confidentiality;
-   retention;
-   access control;
-   versioning;
-   deletion policy;
-   legal requirements;
-   correlation.

Evidence Store tidak harus sama dengan Trace Store.

------------------------------------------------------------------------

## 14.31 Evidence Classification

Evidence dapat mengandung sensitive information.

Evidence SHOULD memiliki classification yang memungkinkan policy
menentukan:

-   siapa boleh membaca;
-   siapa boleh disclose;
-   retention;
-   redaction;
-   external transfer.

Evidence availability untuk verification MUST NOT menghilangkan data
governance obligations.

------------------------------------------------------------------------

## 14.32 Evidence Minimization

System SHOULD mengumpulkan evidence secukupnya untuk assurance dan
accountability, bukan tanpa batas.

\[ EvidenceCollection\approx MinimumSufficientEvidence\]

Evidence minimization membantu privacy, cost, dan security.

------------------------------------------------------------------------

## 14.33 Evidence Retention

Retention SHOULD mengikuti applicable policy/profile.

Retention period MAY berbeda antara:

-   operational evidence;
-   security evidence;
-   compliance evidence;
-   transient evidence;
-   audit evidence.

Deletion atau expiry MUST NOT membuat required conformance evidence
unavailable sebelum applicable retention obligation selesai.

------------------------------------------------------------------------

## 14.34 Evidence Redaction

Redaction MAY diperlukan sebelum evidence diberikan ke verifier, Human,
Agent, atau external service.

Redaction MUST NOT menghilangkan material information yang diperlukan
untuk claim verification tanpa menandai limitation.

Redacted evidence SHOULD mempertahankan reference ke protected original
jika governance mengizinkan.

------------------------------------------------------------------------

## 14.35 Evidence Disclosure

Authority untuk menyimpan/read evidence berbeda dari authority untuk
disclose evidence.

\[ EvidenceReadAuthority\neq EvidenceDisclosureAuthority\]

Cross-boundary evidence transfer MUST tunduk pada Authority, Policy,
Risk, dan Context controls.

------------------------------------------------------------------------

## 14.36 Evidence Immutability and Correction

Evidence SHOULD tidak silently overwritten.

Jika correction diperlukan, implementation SHOULD mempertahankan
supersession relationship:

\[ e\_{new} supersedes e\_{old} \]

tanpa menghapus historical governance meaning kecuali retention/privacy
policy secara sah mensyaratkan deletion.

------------------------------------------------------------------------

## 14.37 Evidence Identity and Deduplication

Evidence SHOULD memiliki identity yang cukup untuk mencegah accidental
duplicate counting.

Dua references ke payload yang sama tidak otomatis merupakan independent
corroboration.

------------------------------------------------------------------------

## 14.38 Evidence Ordering

Jika order material, evidence SHOULD memiliki timestamp atau
causal/correlation metadata.

Distributed systems MAY memiliki clock uncertainty; implementation
SHOULD menggunakan sequence/version/causal identifiers jika wall-clock
time tidak cukup.

------------------------------------------------------------------------

## 14.39 Evidence and State

Evidence MAY memicu state transition hanya melalui governed decision.

\[ Evidence\not\Rightarrow DirectStateMutation\]

Evidence ingestion itself MAY menjadi state event jika implementation
memodelkannya demikian.

------------------------------------------------------------------------

## 14.40 Evidence and Retry

Retry SHOULD menghasilkan new evidence atau explicit reference ke prior
evidence.

Prior failure evidence MUST dipertahankan jika material terhadap retry
decision.

Retry MUST NOT overwrite failure evidence sehingga workflow terlihat
seolah hanya successful attempt yang pernah terjadi.

------------------------------------------------------------------------

## 14.41 Evidence and Replan

Replan SHOULD mempertahankan evidence yang masih relevant dan menandai
evidence yang tidak lagi applicable terhadap new plan.

Old evidence MUST NOT blind-reused jika target, environment, artifact,
atau criteria berubah.

------------------------------------------------------------------------

## 14.42 Evidence and Partial Effect

Partial effect evidence sangat penting untuk recovery.

Minimum SHOULD mencakup:

-   intended action;
-   observed partial result;
-   affected resources;
-   time;
-   errors;
-   state reconciliation input.

------------------------------------------------------------------------

## 14.43 Evidence and Failure

Failure itself menghasilkan governance evidence.

Reference failure evidence:

-   failure type;
-   actor;
-   action;
-   state;
-   error;
-   prior attempts;
-   affected resources;
-   containment;
-   recovery result.

------------------------------------------------------------------------

## 14.44 Evidence Profile

Verification atau domain profile MAY mendefinisikan `Evidence Profile`.

Reference:

```text
profile_id
claim_types
admissible_sources
required_provenance
integrity_level
freshness_limit
independence_requirement
minimum_evidence_set
retention
classification
```

Evidence Profile SHOULD menjadi machine-testable untuk
conformance-critical claims.

------------------------------------------------------------------------

## 14.45 Evidence Failure Modes

### EVD-F01 --- Missing Evidence

Mandatory evidence tidak tersedia.

### EVD-F02 --- Missing Provenance

Origin/derivation tidak cukup.

### EVD-F03 --- Integrity Unknown

Evidence mungkin berubah atau tidak dapat dipercaya sesuai profile.

### EVD-F04 --- Stale Evidence

Freshness requirement tidak terpenuhi.

### EVD-F05 --- Irrelevant Evidence

Evidence tidak mendukung claim/criteria.

### EVD-F06 --- Insufficient Evidence

Evidence present tetapi tidak sufficient.

### EVD-F07 --- False Corroboration

Multiple evidence berasal dari same dependency tanpa recognized
dependence.

### EVD-F08 --- Contradiction

Material evidence saling bertentangan.

### EVD-F09 --- Transformation Loss

Derived evidence kehilangan material information.

### EVD-F10 --- Unauthorized Disclosure

Evidence dipindahkan ke actor/domain tanpa authority.

### EVD-F11 --- Evidence Overwrite

Historical evidence silently diganti.

### EVD-F12 --- Wrong-Scope Evidence

Evidence berasal dari resource/environment/artifact yang berbeda.

Evidence failure MUST menghasilkan `Rejected`, `Inconclusive`,
`Pending`, `Escalate`, atau equivalent controlled outcome sesuai
verification/policy.

------------------------------------------------------------------------

## 14.46 Evidence Evaluation Algorithm

Reference algorithm:

```text
INPUT:
  claim
  candidate evidence set
  verification criteria/profile

1. Resolve claim identity and scope.
2. Resolve evidence identities.
3. Validate source.
4. Validate provenance.
5. Validate integrity requirement.
6. Validate freshness.
7. Validate relevance.
8. Validate scope/resource/environment match.
9. Evaluate independence.
10. Detect duplicate dependency.
11. Detect contradiction.
12. Evaluate admissibility.
13. Evaluate sufficiency.
14. Return normalized evidence set plus:
      admissible
      inadmissible
      missing
      contradictory
      sufficiency status
15. Record evidence evaluation.
```

------------------------------------------------------------------------

## 14.47 Evidence Conformance Requirements

### Core

**AOF-EVD-006** --- Evidence presence MUST NOT otomatis dianggap
verification success.

**AOF-EVD-007** --- Evidence MUST dapat dikaitkan dengan relevant
claim/resource/scope.

### Governed

**AOF-EVD-008** --- Consequential effect SHOULD menghasilkan observable
result/effect evidence.

**AOF-EVD-009** --- Retry MUST preserve material prior-attempt evidence.

**AOF-EVD-010** --- Replan MUST reevaluate applicability of reused
evidence.

**AOF-EVD-011** --- Evidence disclosure MUST tunduk pada applicable
Authority/Policy controls.

**AOF-EVD-012** --- Evidence correction SHOULD preserve
supersession/history.

**AOF-EVD-013** --- Required evidence retention MUST mengikuti
applicable policy/profile.

**AOF-EVD-014** --- Evidence aggregation MUST NOT silently erase
material contradiction/provenance.

### Assured / High-Assurance

**AOF-EVD-015** --- High-risk evidence profile MUST menentukan
admissibility, provenance, freshness, dan independence requirements.

**AOF-EVD-016** --- High-assurance consequential evidence MUST memiliki
stronger integrity protection sesuai profile.

**AOF-EVD-017** --- Independent verification MUST NOT bergantung hanya
pada evidence yang secara substantif berasal dari same self-validating
source jika independence required.

**AOF-EVD-018** --- High-assurance evidence chain MUST dapat
direkonstruksi dari claim ke source dan verification result.

------------------------------------------------------------------------

## 14.48 Evidence Invariants

### EVD-INV-01 --- Provenance

\[ ConsequentialEvidence\Rightarrow Provenance\]

### EVD-INV-02 --- Claim Separation

\[ Claim\neq Evidence\]

### EVD-INV-03 --- Verification Separation

\[ Evidence\neq Verification\]

### EVD-INV-04 --- Sufficiency

\[ EvidencePresent\not\Rightarrow EvidenceSufficient\]

### EVD-INV-05 --- Freshness

\[
Stale(e)\land FreshRequired\Rightarrow\neg Sufficient(e)
\]

### EVD-INV-06 --- Contradiction Visibility

\[ MaterialContradiction\Rightarrow VisibleToVerification\]

### EVD-INV-07 --- Derived Provenance

\[ DerivedEvidence\Rightarrow SourceReference\]

### EVD-INV-08 --- No False Corroboration

\[
SameUnderlyingSource\not\Rightarrow IndependentCorroboration
\]

### EVD-INV-09 --- Disclosure Control

\[ EvidenceAccess\not\Rightarrow EvidenceDisclosure\]

### EVD-INV-10 --- Historical Preservation

\[ Correction(e)\Rightarrow SupersessionOrTrace\]

------------------------------------------------------------------------

## 14.49 Architecture Integration

Evidence mengalir terutama dari Effect Plane ke Assurance Plane dan
kembali ke Control Plane:

```text
Effect Plane
    |
    v
Result + Effect Evidence
    |
    v
Evidence Collection / Store
    |
    v
Assurance Plane
    |
    v
Verification Result
    |
    v
Control Plane / State Transition
```

Evidence MAY juga berasal dari Control Plane, Human Governance, State
Store, atau external sources.

------------------------------------------------------------------------

## 14.50 Evidence Freeze Candidate Criteria

Evidence area MAY dinyatakan `Freeze Candidate` jika:

1.  Evidence object semantics stabil;
2.  Claim--Evidence--Verification separation stabil;
3.  provenance/integrity/freshness semantics stabil;
4.  admissibility dan sufficiency semantics stabil;
5.  contradiction/corroboration semantics stabil;
6.  evidence independence compatible dengan Verification independence;
7.  evidence storage/disclosure compatible dengan Security dan
    State/Trace;
8.  retry/replan/partial-effect evidence semantics stabil;
9.  Evidence Profile dapat dipetakan ke conformance tests;
10. tidak ada contradiction dengan Risk, Verification, Human Governance,
    atau Privacy controls.

------------------------------------------------------------------------

## 14.51 Evidence Formalization Result

Evidence v1.0 RC-Evidence diringkas sebagai:

\[ EvidenceAssurance= Capture + Provenance + Integrity + Freshness +
Relevance + Admissibility + Sufficiency + Traceability \]

dengan:

\[ \boxed{ Claim\neq Evidence\neq Verification } \]

\[ \boxed{ Evidence\ Present\neq Evidence\ Sufficient } \]

\[ \boxed{ Consequential\ Evidence\Rightarrow Provenance } \]

dan:

\[ \boxed{ Verification\ Trust\ Depends\ On\ Evidence\ Quality }
\] \# 15. Verification Requirements

## 15.1 Purpose

`Verification Model` mendefinisikan bagaimana AOF menentukan apakah
suatu `Claim`, `Result`, `Effect`, `Artifact`, `Decision`, atau
`Outcome` memenuhi explicit `Criteria` berdasarkan admissible dan
sufficient `Evidence`.

Canonical separation:

\[
Claim\neq Evidence\neq Verification\neq Approval
\]

Verification adalah assurance process. Verification tidak memberikan
authority dan tidak menggantikan policy atau risk acceptance.

\[ Verified(x)\not\Rightarrow Authorized(x) \]

\[ Verified(x)\not\Rightarrow Approved(x) \]

------------------------------------------------------------------------

## 15.2 Verification Definition

Canonical verification object:

\[ v= \langle id, claim, criteria, evidence, verifier, method,
profile, independence, result, confidence, limitations, timestamp,
provenance \rangle\]

dengan:

-   `claim`: subject claim yang diuji;
-   `criteria`: explicit acceptance/verification criteria;
-   `evidence`: admissible evidence set;
-   `verifier`: actor/mechanism yang melakukan verification;
-   `method`: deterministic, agentic, Human, composite, atau
    domain-specific method;
-   `profile`: applicable Verification Profile;
-   `independence`: verifier independence level;
-   `result`: normalized verification outcome;
-   `confidence`: optional assessment confidence;
-   `limitations`: known limitations;
-   `timestamp`: verification time;
-   `provenance`: verification process provenance.

Reference result:

\[ VerificationResult= { Verified, Rejected, Inconclusive } \]

**AOF-VER-001** --- Required verification MUST menghasilkan explicit
normalized result dan MUST NOT diasumsikan berhasil hanya karena
evidence tersedia.

------------------------------------------------------------------------

## 15.3 Verification Predicate

Canonical function:

\[ V: \langle claim,evidence,criteria\rangle
\rightarrow result\]

dengan:

\[ result\in{Verified,Rejected,Inconclusive} \]

Jika verification required untuk execution/completion:

\[ V=Verified \]

harus terpenuhi sebelum governed transition yang mensyaratkannya.

`Inconclusive` MUST NOT diperlakukan sebagai `Verified`.

------------------------------------------------------------------------

## 15.4 Verification Criteria

Criteria menentukan apa yang harus benar.

Criteria SHOULD:

-   explicit;
-   scoped;
-   testable atau reviewable;
-   linked ke claim;
-   versioned jika material;
-   berasal dari valid specification, policy, profile, requirement, atau
    governance source.

\[ VerificationWithoutCriteria\Rightarrow AmbiguousAssurance\]

**AOF-VER-002** --- Consequential verification MUST memiliki
identifiable criteria.

------------------------------------------------------------------------

## 15.5 Verification Subject

Verification MAY berlaku terhadap:

-   requirement;
-   artifact;
-   code;
-   configuration;
-   action result;
-   resource state;
-   security claim;
-   compliance claim;
-   risk-control claim;
-   release readiness;
-   task completion;
-   final outcome.

Subject scope MUST jelas agar result tidak digunakan di luar claim yang
diverifikasi.

------------------------------------------------------------------------

## 15.6 Verification Modes

Reference modes:

### Self Verification

Executor atau generating agent melakukan self-check.

### Independent Agent Verification

Distinct agent melakukan verification.

### Deterministic Verification

Test, rule engine, compiler, scanner, validator, invariant checker, atau
deterministic mechanism.

### Human Verification

Human reviewer mengevaluasi evidence dan criteria.

### Composite Verification

Gabungan dua atau lebih mechanisms.

\[ VerificationMode= { Self, IndependentAgent, Deterministic, Human,
Composite } \]

------------------------------------------------------------------------

## 15.7 Verifier Independence

Reference independence levels:

-   `VI0` --- same actor/self-verification;
-   `VI1` --- distinct logical role tetapi shared execution context;
-   `VI2` --- distinct actor/mechanism dengan separated responsibility;
-   `VI3` --- administratively/organizationally independent atau
    externally anchored.

Independence requirement ditentukan oleh Risk/Profile/Policy.

\[ HighRisk\Rightarrow VI\geq RequiredLevel\]

AOF reference profile mensyaratkan independent verification untuk High
risk.

------------------------------------------------------------------------

## 15.8 Independence Is Not Identity Alone

Distinct agent IDs tidak otomatis berarti independent.

\[ DifferentID\not\Rightarrow Independent\]

Independence SHOULD mempertimbangkan:

-   shared model/runtime;
-   shared context;
-   shared evidence source;
-   shared failure mode;
-   shared operator;
-   shared policy;
-   shared tool;
-   shared prompt lineage;
-   administrative separation.

------------------------------------------------------------------------

## 15.9 Verification and Evidence

Verification MUST mengevaluasi evidence admissibility dan sufficiency
sesuai Section 14.

\[ Verified(c) \Rightarrow Admissible(E,c) \land
Sufficient(E,c) \]

sesuai applicable profile.

Evidence yang contradictory atau insufficient SHOULD menghasilkan
`Rejected` atau `Inconclusive`, bukan fabricated certainty.

------------------------------------------------------------------------

## 15.10 Verification and Authority

Verifier authority berbeda dari execution authority.

Verifier MAY memiliki authority untuk:

-   inspect;
-   test;
-   attest;
-   reject;
-   recommend;
-   approve jika separately granted.

Verification role MUST NOT otomatis memberikan authority untuk execute
atau approve.

\[ VerifyAuthority\not\Rightarrow ExecuteAuthority\]

------------------------------------------------------------------------

## 15.11 Verification and Approval

Verification menjawab:

> Apakah claim memenuhi criteria berdasarkan evidence?

Approval menjawab:

> Apakah authorized approver mengizinkan governed progression/action?

\[ Verification\neq Approval\]

Critical risk MAY memerlukan keduanya:

\[ Verified\land Approved\]

------------------------------------------------------------------------

## 15.12 Verification and Risk

Reference mapping:

  Risk       Reference Verification
  ---------- ------------------------------------------------------
  Low        Self or deterministic verification MAY be sufficient
  Moderate   Policy-directed verification
  High       Independent verification
  Critical   Independent verification + explicit approval

Domain profile MAY memperketat mapping.

**AOF-VER-003** --- Jika independent verification required,
self-verification alone MUST NOT memenuhi requirement.

------------------------------------------------------------------------

## 15.13 Verification and Policy

Policy MAY menentukan:

-   verification required/not required;
-   criteria/profile;
-   verifier type;
-   independence;
-   evidence requirements;
-   timeout;
-   failure behavior;
-   re-verification triggers.

Policy result `RequireVerification` MUST menghasilkan explicit
verification gate sebelum governed progression yang terkait.

------------------------------------------------------------------------

## 15.14 Verification and State

Verification state SHOULD menjadi bagian authoritative orchestration
state.

Possible task flow:

```text
Executing
   |
   v
Verifying
   |
   +--> Verified      -> Completed candidate
   +--> Rejected      -> Replan/Fail/Reject
   +--> Inconclusive  -> More Evidence/Escalate
```

Verification result MUST committed melalui controlled transition.

------------------------------------------------------------------------

## 15.15 Verification Gate

`Verification Gate` merupakan Safety Kernel component.

\[ K\supset eq VerificationGate\]

Reference:

\[
VerificationGate(x,s)\rightarrow { Satisfied, Required, Rejected, Inconclusive, Pending }
\]

`Satisfied` hanya valid jika applicable verification obligations telah
dipenuhi.

------------------------------------------------------------------------

## 15.16 Pre-Action Verification

Beberapa action memerlukan verification sebelum effect.

Examples:

-   validate generated command;
-   verify deployment artifact;
-   verify target environment;
-   verify change plan;
-   verify authorization package.

\[ PreVerify(x)=Required \Rightarrow VerifiedBeforeEffect(x) \]

------------------------------------------------------------------------

## 15.17 Post-Action Verification

Post-action verification memastikan actual effect/outcome.

Examples:

-   confirm deployed version;
-   run health check;
-   verify database migration;
-   verify security controls;
-   confirm intended file modification.

\[ ExecutionSuccess\not\Rightarrow PostConditionVerified
\]

------------------------------------------------------------------------

## 15.18 Continuous Verification

Long-running workflow MAY memerlukan repeated verification pada
checkpoints.

\[ Checkpoint_i\Rightarrow V_i \]

Continuous verification SHOULD digunakan jika state/risk dapat berubah
material selama execution.

------------------------------------------------------------------------

## 15.19 Verification Profile

Canonical `Verification Profile` SHOULD mendefinisikan:

```text
profile_id
version
scope
claim_types
criteria_source
verification_modes
minimum_independence
evidence_profile
required_methods
result_semantics
timeout
reverification_triggers
failure_behavior
retention
```

**AOF-VER-004** --- High/Critical risk profile MUST memiliki explicit
Verification Profile atau equivalent enforceable semantics.

------------------------------------------------------------------------

## 15.20 Verification Method

Method MAY berupa:

-   unit/integration/system test;
-   static analysis;
-   dynamic analysis;
-   schema validation;
-   policy validation;
-   state observation;
-   differential comparison;
-   formal check;
-   Human review;
-   Agent critique;
-   multi-agent review;
-   runtime health check;
-   domain-specific test.

Method MUST sesuai dengan claim.

------------------------------------------------------------------------

## 15.21 Deterministic Verification Preference

Jika claim dapat diverifikasi secara deterministic dengan reliable
mechanism, deterministic verification SHOULD diprioritaskan dibanding
probabilistic judgment untuk enforcement-critical claims.

\[ DeterministicCheckAvailable \Rightarrow PreferDeterministic
\]

bukan absolute requirement jika deterministic mechanism sendiri
insufficient.

------------------------------------------------------------------------

## 15.22 Composite Verification

Composite verification:

\[ V_c=f(V_1,V_2,\ldots,V_n) \]

Composition rule MUST explicit.

Examples:

```text
Unit Tests = Verified
AND Security Scan = Verified
AND Human Review = Approved
```

atau quorum-based review jika profile mendefinisikannya.

Composite verification MUST NOT silently ignore failed mandatory
component.

------------------------------------------------------------------------

## 15.23 Verification Quorum

Profile MAY menggunakan quorum:

\[ Verified\iffCount(IndependentPositiveResults)\geq q\]

Quorum semantics MUST menentukan:

-   eligible verifier;
-   independence;
-   required count;
-   handling of rejection;
-   handling of inconclusive;
-   conflict resolution.

------------------------------------------------------------------------

## 15.24 Conflicting Verification Results

Jika verifier berbeda menghasilkan conflicting results:

\[ V_1=Verified,\quadV\_2=Rejected \]

system MUST NOT memilih positive result secara arbitrary.

Possible governed outcomes:

-   additional verifier;
-   stronger method;
-   `Inconclusive`;
-   escalation;
-   reject.

**AOF-VER-005** --- Material conflicting verification results MUST
menggunakan explicit resolution rule.

------------------------------------------------------------------------

## 15.25 Verification Confidence

Confidence MAY menjadi metadata tetapi tidak menggantikan result
semantics.

\[ HighConfidence\not\Rightarrow Verified\]

Jika confidence threshold digunakan, threshold MUST defined dalam
profile.

------------------------------------------------------------------------

## 15.26 Verification Limitations

Verifier SHOULD mencatat known limitations yang material.

Examples:

-   incomplete environment access;
-   partial evidence;
-   unsupported platform;
-   unavailable external dependency;
-   sampling-only validation.

Material limitation MAY menyebabkan `Inconclusive`.

------------------------------------------------------------------------

## 15.27 Verification Freshness

Verification dapat menjadi stale jika verified subject berubah.

\[ Verified(x\_{v1})\not\Rightarrow Verified(x\_{v2}) \]

Artifact/resource identity SHOULD diikat pada verification result.

Change terhadap verified subject MUST memicu re-verification jika
material.

------------------------------------------------------------------------

## 15.28 Verification Binding

Verification result SHOULD di-bind ke:

-   claim;
-   artifact/resource identity;
-   version/digest jika applicable;
-   environment;
-   criteria version;
-   evidence set;
-   verifier;
-   timestamp.

Ini mencegah verification reuse pada wrong target.

------------------------------------------------------------------------

## 15.29 Re-Verification Triggers

Triggers MAY mencakup:

-   artifact change;
-   code/config change;
-   environment change;
-   policy change;
-   risk increase;
-   new contradictory evidence;
-   authority change yang mempengaruhi claim;
-   retry/replan;
-   partial failure;
-   expiry/freshness threshold.

\[ MaterialSubjectChange\Rightarrow Reverify\]

------------------------------------------------------------------------

## 15.30 Verification and Retry

Retry SHOULD menghasilkan verification baru jika result/effect berubah.

Prior rejected verification MUST NOT silently overwritten.

Repeated verification failure SHOULD memicu replan/escalation sesuai
failure budget/policy.

------------------------------------------------------------------------

## 15.31 Verification and Replan

Replan yang mengubah artifact, method, target, resource, atau acceptance
criteria MUST memicu reevaluation terhadap applicable verification
obligations.

Old verification MAY reused hanya jika scope dan subject tetap valid.

------------------------------------------------------------------------

## 15.32 Verification and Partial Effect

Partial effect MUST NOT dianggap successful completion hanya karena
pre-action verification berhasil.

Post-action verification SHOULD menentukan actual resulting state.

------------------------------------------------------------------------

## 15.33 Verification and Human Review

Human verifier MUST memiliki sufficient context/evidence.

Human review SHOULD structured untuk consequential claims, misalnya:

```text
subject
criteria
evidence
decision
limitations
identity
timestamp
```

Human verification tetap tunduk pada separation-of-duties jika required.

------------------------------------------------------------------------

## 15.34 Verification and Agent Review

Agent verifier SHOULD menerima scoped context dan evidence, bukan
uncontrolled access.

Verifier agent MUST NOT memperoleh broader execution authority hanya
karena verification assignment.

Agent verification output default merupakan verification proposal sampai
accepted melalui applicable control path jika profile memerlukan.

------------------------------------------------------------------------

## 15.35 Verification and Tool Failure

Jika verification tool gagal:

\[ ToolFailure\neq Verified\]

Outcome SHOULD menjadi `Inconclusive`, `Pending`, `Rejected`, atau
escalation sesuai profile.

Fail-open verification MUST NOT digunakan untuk mandatory High/Critical
verification.

------------------------------------------------------------------------

## 15.36 Verification and Missing Evidence

Jika mandatory evidence missing:

\[ MissingRequiredEvidence\Rightarrow\neg Verified\]

Possible result:

-   `Inconclusive`;
-   `Rejected`;
-   request more evidence;
-   escalation.

------------------------------------------------------------------------

## 15.37 Verification and Contradictory Evidence

Material contradiction MUST masuk dalam verification decision.

Verifier MUST NOT discard contradictory evidence tanpa traceable reason.

------------------------------------------------------------------------

## 15.38 Verification Provenance

Verification provenance SHOULD mencakup:

-   verifier identity;
-   method;
-   profile;
-   criteria;
-   evidence references;
-   result;
-   timestamp;
-   environment;
-   tool/model/version jika material;
-   limitations.

------------------------------------------------------------------------

## 15.39 Verification Trace Events

Reference events:

-   `VerificationRequested`;
-   `VerifierAssigned`;
-   `VerificationStarted`;
-   `EvidenceEvaluated`;
-   `VerificationCompleted`;
-   `VerificationRejected`;
-   `VerificationInconclusive`;
-   `ReverificationRequired`;
-   `VerificationEscalated`.

------------------------------------------------------------------------

## 15.40 Verification Failure Modes

### VER-F01 --- Missing Criteria

Verification dilakukan tanpa explicit criteria.

### VER-F02 --- Missing Evidence

Required evidence tidak tersedia.

### VER-F03 --- Insufficient Evidence

Evidence tidak sufficient.

### VER-F04 --- Inadmissible Evidence

Evidence tidak memenuhi profile.

### VER-F05 --- Independence Failure

Required independence tidak terpenuhi.

### VER-F06 --- Wrong Subject

Verification result diterapkan ke artifact/resource berbeda.

### VER-F07 --- Stale Verification

Subject berubah setelah verification.

### VER-F08 --- Tool Failure

Verification mechanism gagal.

### VER-F09 --- Conflict

Multiple verifier results bertentangan.

### VER-F10 --- Circular Verification

Verifier bergantung pada same unsupported claim yang sedang
diverifikasi.

### VER-F11 --- Scope Overreach

Verification result digunakan untuk claim di luar verified scope.

### VER-F12 --- Silent Override

Rejected/Inconclusive result diubah menjadi success tanpa governed
decision.

------------------------------------------------------------------------

## 15.41 Circular Verification

Verification non-circularity:

\[ Verify(c,e) \]

MUST NOT bergantung solely pada evidence yang validitasnya hanya berasal
dari claim (c) sendiri.

Example invalid pattern:

```text
Agent says output is correct
-> same statement used as evidence
-> same agent verifies statement
-> system marks Verified
```

**AOF-VER-006** --- Required verification MUST NOT bersifat purely
self-referential.

------------------------------------------------------------------------

## 15.42 Verification Result Consumption

Verification result adalah governed input.

\[ VerificationResult\rightarrow ControlDecision\]

Result MUST NOT langsung menyebabkan consequential effect tanpa
applicable Authority, Policy, Risk, dan State controls.

------------------------------------------------------------------------

## 15.43 Completion Verification

Task/session MUST NOT mencapai successful terminal state jika mandatory
completion verification belum satisfied.

\[ Completed \Rightarrow GoalSatisfied
\land RequiredVerificationSatisfied\]

sesuai lifecycle semantics.

------------------------------------------------------------------------

## 15.44 Verification of Goal Satisfaction

Goal satisfaction SHOULD diverifikasi terhadap `SuccessCriteria`.

\[ GoalSatisfied(g) = Verify( Outcome, Evidence, SuccessCriteria(g) ) \]

Agent declaration "task selesai" bukan sufficient proof jika explicit
success criteria tersedia.

------------------------------------------------------------------------

## 15.45 Verification of Control Operation

High-assurance profile MAY memverifikasi control operation itu sendiri,
misalnya:

-   authority evaluator result;
-   policy version;
-   risk mapping;
-   state transition validity;
-   trace completeness.

Ini disebut `Control Assurance`.

------------------------------------------------------------------------

## 15.46 Verification Escalation

Escalation SHOULD terjadi jika:

-   evidence cannot be obtained;
-   verifier conflict unresolved;
-   required independence unavailable;
-   verification mechanism unavailable;
-   criteria ambiguous;
-   critical limitation exists.

Escalation MUST preserve verification package.

------------------------------------------------------------------------

## 15.47 Reference Verification Algorithm

```text
INPUT:
  claim
  criteria
  candidate evidence
  Verification Profile
  current state

1. Resolve claim identity/scope.
2. Resolve criteria and criteria version.
3. Resolve required verification mode.
4. Resolve required independence.
5. Select eligible verifier.
6. Evaluate evidence admissibility.
7. Evaluate evidence sufficiency.
8. Detect contradiction/dependency.
9. Execute verification method.
10. Evaluate limitations.
11. Produce:
      VERIFIED
      REJECTED
      INCONCLUSIVE
12. Bind result to subject, criteria, evidence, verifier, time.
13. Record verification trace.
14. Return result to Control Plane.
```

------------------------------------------------------------------------

## 15.48 Verification Conformance Requirements

### Core

**AOF-VER-001 (canonical cross-reference)** — See the primary normative definition above.
result.

**AOF-VER-002 (canonical cross-reference)** — See the primary normative definition above.
identifiable criteria.

**AOF-VER-007** --- `Inconclusive` MUST NOT diperlakukan sebagai
`Verified`.

**AOF-VER-008** --- Required verification MUST evaluate applicable
evidence admissibility/sufficiency.

### Governed

**AOF-VER-009** --- Verification result MUST bound ke relevant
subject/scope.

**AOF-VER-010** --- Material subject change MUST memicu re-verification.

**AOF-VER-011** --- Verification failure MUST NOT silently fail-open.

**AOF-VER-012** --- Mandatory completion verification MUST satisfied
sebelum successful terminal completion.

**AOF-VER-013** --- Replan/retry MUST reevaluate verification
applicability jika subject/effect berubah.

**AOF-VER-014** --- Verification result MUST kembali melalui governed
Control/State path.

### Assured / High-Assurance

**AOF-VER-015** --- High risk MUST menggunakan verifier independence
sesuai profile.

**AOF-VER-016** --- Critical risk MUST menggunakan independent
verification dan explicit approval sesuai reference profile.

**AOF-VER-017** --- High-assurance verification provenance MUST cukup
untuk independent reconstruction.

**AOF-VER-018** --- High-assurance profile MUST menentukan behavior
untuk verifier unavailability, conflict, stale result, dan evidence
insufficiency.

------------------------------------------------------------------------

## 15.49 Verification Invariants

### VER-INV-01 --- Criteria Requirement

\[ Verification\Rightarrow Criteria\]

### VER-INV-02 --- Evidence Requirement

\[ Verified(c)\Rightarrow SufficientAdmissibleEvidence(c) \]

### VER-INV-03 --- Inconclusive Non-Success

\[ Inconclusive\not\Rightarrow Verified\]

### VER-INV-04 --- Independence

\[ IndependentVerificationRequired \Rightarrow
SelfVerificationInsufficient \]

### VER-INV-05 --- Subject Binding

\[ Verified(x)\not\Rightarrow Verified(y) \]

untuk materially different subject (y).

### VER-INV-06 --- Reverification

\[ MaterialSubjectChange\Rightarrow Reverify\]

### VER-INV-07 --- Verification Non-Authority

\[ Verified\not\Rightarrow Authorized\]

### VER-INV-08 --- Verification Non-Approval

\[ Verified\not\Rightarrow Approved\]

### VER-INV-09 --- Non-Circularity

\[ Verification\not\Rightarrow PureSelfReference\]

### VER-INV-10 --- Completion Assurance

\[ SuccessfulCompletion \Rightarrow
RequiredVerificationSatisfied \]

------------------------------------------------------------------------

## 15.50 Evidence--Verification Contract

Section 14 dan Section 15 membentuk contract:

\[ EvidenceProfile \rightarrow AdmissibleEvidenceSet
\rightarrow VerificationProfile \rightarrow
VerificationResult \]

Evidence menentukan support material.

Verification menentukan evaluation.

\[ EvidenceQuality + CriteriaQuality + VerifierSuitability
\rightarrow AssuranceQuality \]

------------------------------------------------------------------------

## 15.51 Architecture Integration

Reference flow:

```text
Effect / Claim
     |
     v
Evidence Collection
     |
     v
Evidence Evaluation
     |
     v
Verification Gate
     |
     +--> Verified
     +--> Rejected
     +--> Inconclusive
     |
     v
Control Plane
     |
     v
State Transition / Retry / Replan / Escalate / Complete
```

------------------------------------------------------------------------

## 15.52 Verification Freeze Candidate Criteria

Verification area MAY dinyatakan `Freeze Candidate` jika:

1.  result semantics stabil;
2.  criteria requirement stabil;
3.  verification modes stabil;
4.  independence levels stabil;
5.  Evidence--Verification contract stabil;
6.  High/Critical risk mapping stabil;
7.  pre/post/continuous verification semantics stabil;
8.  re-verification triggers stabil;
9.  completion verification compatible dengan Lifecycle/State;
10. conformance requirements dapat dipetakan ke executable tests;
11. tidak ada contradiction dengan Policy, Risk, Human Governance,
    Failure & Recovery, atau Security.

------------------------------------------------------------------------

## 15.53 Verification Formalization Result

Verification v1.0 RC-Verification diringkas sebagai:

\[ Verification= Criteria + AdmissibleEvidence + SufficientEvidence +
SuitableVerifier + Method + Independence + ExplicitResult + Traceability
\]

dengan:

\[ \boxed{ Evidence\neq Verification } \]

\[ \boxed{ Inconclusive\neq Verified } \]

\[ \boxed{ HighRisk\Rightarrow IndependentVerification } \]

\[ \boxed{ Verification\ Does\ Not\ Create\ Authority } \]

dan:

\[
\boxed{ SuccessfulCompletion\Rightarrow RequiredVerificationSatisfied }
\] \# 16. State & Trace Requirements

## 16.1 Purpose

`State & Trace Model` mendefinisikan bagaimana AOF merepresentasikan
authoritative orchestration condition, mengendalikan consequential
mutation, menjaga consistency, dan merekam sufficient history untuk
accountability, recovery, verification, audit, dan conformance.

Canonical separation:

\[ State\neq Trace\neq AgentMemory\]

`State` menjawab kondisi authoritative sistem saat ini. `Trace` menjawab
bagaimana kondisi tersebut dicapai melalui events, decisions, actions,
evidence, dan transitions.

\[ AuthoritativeState\neq AgentPrivateMemory\]

------------------------------------------------------------------------

## 16.2 Canonical State

Canonical orchestration state:

\[ s_t= \langle Tasks, Agents, Context, Authority, Policies,
Evidence, Risks, Resources, Verification, Approvals, History
\rangle\_t \]

Deployment MAY memecah state ke beberapa stores selama semantic
consistency tetap dipertahankan.

**AOF-ST-001** --- Consequential orchestration decision MUST menggunakan
authoritative state atau controlled projection dari authoritative state.

------------------------------------------------------------------------

## 16.3 State Scope

State MAY berada pada beberapa scopes:

-   framework/system;
-   organization/domain;
-   session;
-   task;
-   agent assignment;
-   resource;
-   authority;
-   policy;
-   risk;
-   verification;
-   approval.

Implementation MUST dapat menentukan scope dari consequential state
item.

------------------------------------------------------------------------

## 16.4 State Identity and Version

Consequential state SHOULD memiliki identity dan version/revision.

Reference:

\[ StateRef=\langle scope,id,version\rangle\]

Decision yang bergantung pada mutable state SHOULD bind ke relevant
state version.

\[ Decision(d,s_v) \]

Perubahan material setelah decision MAY membuat decision stale.

------------------------------------------------------------------------

## 16.5 State Transition

Canonical transition:

\[ \Delta:S\times D\rightarrow S' \]

Expanded:

\[ transition= \langle id, stateBefore, decision, action,
evidence, stateAfter, actor, timestamp \rangle\]

Transition MUST memenuhi applicable lifecycle, authority, policy, risk,
dan verification constraints.

------------------------------------------------------------------------

## 16.6 No Silent State Mutation

\[ ConsequentialStateChange\Rightarrow ControlledTransition\]

**AOF-ST-002** --- Consequential state mutation MUST NOT terjadi secara
silent di luar controlled transition path.

Agent internal reasoning atau private memory MAY berubah tanpa global
transition jika tidak consequential, tetapi MUST NOT menjadi hidden
source of authoritative governance state.

------------------------------------------------------------------------

## 16.7 State Validation

`State Validator` adalah Safety Kernel component.

\[ K\supset eq StateValidator\]

Reference:

\[ StateValid(s,x)\rightarrow{Pass,Fail,Pending} \]

Validation MAY memeriksa:

-   lifecycle transition;
-   version;
-   prerequisites;
-   dependency status;
-   resource state;
-   authority status;
-   verification status;
-   approval status;
-   concurrency conflict.

`Pending` MUST NOT menjadi implicit Pass.

------------------------------------------------------------------------

## 16.8 Lifecycle State Integrity

Task/session transitions MUST mengikuti allowed transition model.

Example invalid transition:

\[ Created\rightarrow Completed\]

tanpa required intermediate control jika lifecycle/profile
mensyaratkannya.

Implementation MAY optimize internal states tetapi externally
consequential semantics MUST equivalent.

------------------------------------------------------------------------

## 16.9 State Preconditions and Postconditions

Action SHOULD mendefinisikan relevant preconditions dan expected
postconditions.

\[ Execute(x)\Rightarrow Preconditions(x)=true \]

Postconditions SHOULD diuji melalui result/effect evidence jika
material.

\[ ExpectedEffect\neq ObservedEffect\]

------------------------------------------------------------------------

## 16.10 State Ownership

Setiap authoritative state domain SHOULD memiliki logical
owner/controller.

Owner bertanggung jawab atas valid mutation semantics, bukan necessarily
Human owner.

Examples:

-   Task Manager owns task lifecycle state;
-   Authority service owns grant lifecycle;
-   Policy service owns policy activation/version;
-   Risk component owns authoritative risk assessment records;
-   Verification subsystem owns verification result records.

No component SHOULD mutate another domain's authoritative state tanpa
defined interface/control.

------------------------------------------------------------------------

## 16.11 State Projection

Agent SHOULD menerima minimum necessary state projection:

\[ Projection(a,t)=S\_{a,t}\subset eq S\]

Projection MAY omit sensitive atau irrelevant fields.

Projection MUST NOT mengubah authoritative semantics.

Agent output based on stale projection harus diperlakukan sebagai
proposal yang perlu current-state validation.

------------------------------------------------------------------------

## 16.12 Stale State

\[ StateVersion\_{decision}\<StateVersion\_{current} \]

tidak selalu berarti decision invalid, tetapi material change MUST
diperiksa.

**AOF-ST-003** --- Implementation MUST memiliki mechanism untuk
mendeteksi atau mengendalikan material stale-state use pada
consequential actions.

------------------------------------------------------------------------

## 16.13 Optimistic Concurrency

Implementation MAY menggunakan optimistic concurrency:

\[ Commit\iffExpectedVersion=CurrentVersion \]

Jika version mismatch:

-   reject;
-   reload;
-   re-evaluate;
-   replan;
-   escalate.

Blind overwrite MUST dihindari untuk consequential shared state.

------------------------------------------------------------------------

## 16.14 Pessimistic Concurrency

Implementation MAY menggunakan locks, leases, serialization, atau
transaction boundaries.

Locking mechanism SHOULD memiliki timeout/recovery semantics untuk
mencegah permanent deadlock.

AOF tidak mewajibkan specific concurrency technology.

------------------------------------------------------------------------

## 16.15 Conflict Detection

Concurrent transitions yang incompatible MUST NOT silently committed.

\[
Conflict(\Delta\_1,\Delta\_2)\Rightarrow ResolveBeforeCommit
\]

Resolution MAY berupa:

-   reject one transition;
-   serialize;
-   merge jika semantically safe;
-   replan;
-   escalate.

**AOF-ST-004** --- Shared consequential state MUST memiliki
conflict-control mechanism.

------------------------------------------------------------------------

## 16.16 Idempotency

Retryable consequential operation SHOULD memiliki idempotency semantics
jika practical.

\[ Repeat(x,key)\Rightarrow NoDuplicateUnintendedEffect\]

Idempotency MAY menggunakan:

-   idempotency key;
-   operation ID;
-   transaction ID;
-   deduplication record;
-   state predicate.

------------------------------------------------------------------------

## 16.17 Duplicate Execution

Duplicate request MUST dibedakan dari authorized repeated action.

Implementation SHOULD mendeteksi duplicate consequential execution jika
repeated effect dapat menyebabkan harm.

------------------------------------------------------------------------

## 16.18 Replay

Replay adalah reprocessing event/request/decision lama.

Replay MUST memvalidasi current Authority, Policy, State, Risk, dan
verification obligations jika replay dapat menghasilkan new effect.

\[ HistoricalPermit\not\Rightarrow CurrentPermit\]

------------------------------------------------------------------------

## 16.19 Partial Commit

Distributed action MAY menghasilkan partial state mutation.

Jika partial commit terjadi:

1.  capture actual state;
2.  record partial transition;
3.  capture evidence;
4.  reassess risk;
5.  reconcile;
6.  compensate/escalate sesuai policy.

System MUST NOT represent partial commit as atomic success.

------------------------------------------------------------------------

## 16.20 Distributed State

Distributed deployment SHOULD mendefinisikan:

-   consistency model;
-   authoritative source per state domain;
-   version semantics;
-   conflict behavior;
-   replication lag handling;
-   failure recovery;
-   revocation propagation.

Strong consistency tidak diwajibkan universal, tetapi unsafe ambiguity
MUST dikendalikan.

------------------------------------------------------------------------

## 16.21 State Freshness

State freshness requirement tergantung domain.

Authority revocation dan production target state MAY membutuhkan fresher
state daripada informational planning context.

Profile SHOULD menentukan freshness constraints untuk high-risk control
data.

------------------------------------------------------------------------

## 16.22 TOCTOU State Control

\[ Check(s\_{t_1})\not\Rightarrow Valid(s\_{t_2}) \]

Material state changes antara control evaluation dan Effect Boundary
SHOULD memicu revalidation.

High-risk implementation SHOULD bind permit/decision ke state version
atau equivalent freshness guarantee.

------------------------------------------------------------------------

## 16.23 State Reconciliation

Reconciliation membandingkan intended state dan observed actual state.

\[ Reconcile= Compare(IntendedState,ObservedState) \]

Possible results:

-   consistent;
-   drift;
-   partial;
-   unknown.

Drift yang material MUST menghasilkan controlled response.

------------------------------------------------------------------------

## 16.24 External State

External resources MAY berubah di luar AOF.

External state MUST dianggap independently mutable kecuali deployment
guarantees otherwise.

System SHOULD observe/revalidate external state sebelum high-risk effect
jika material.

------------------------------------------------------------------------

## 16.25 State and Authority

Authority lifecycle adalah authoritative state.

Revocation, suspension, expiry, dan consumption MUST visible terhadap
relevant control decisions sesuai propagation guarantees.

Stale cached authority state MUST NOT digunakan untuk new high-risk
effect jika revocation freshness requirement tidak terpenuhi.

------------------------------------------------------------------------

## 16.26 State and Policy

Policy version/activation state MUST identifiable.

Pending decision yang menggunakan superseded policy SHOULD direevaluasi
jika change material.

------------------------------------------------------------------------

## 16.27 State and Risk

Risk assessment state MUST preserve current class, residual risk,
controls, and assessment provenance.

Material state change MAY trigger Risk reassessment.

------------------------------------------------------------------------

## 16.28 State and Verification

Verification result MUST bind ke verified subject/version.

If subject state changes materially:

\[ Verified(s_v)\not\Rightarrow Verified(s\_{v+1}) \]

unless Verification Profile explicitly permits reuse.

------------------------------------------------------------------------

## 16.29 State and Approval

Approval SHOULD bind ke subject/scope/state/version jika state mutation
dapat mengubah approval meaning.

Approval for plan version 1 MUST NOT automatically authorize materially
changed plan version 2.

------------------------------------------------------------------------

## 16.30 State and Retry

Retry MUST consider current authoritative state, prior effect, prior
evidence, authority consumption, and idempotency.

\[ Retry\neq BlindRepeat\]

------------------------------------------------------------------------

## 16.31 State and Replan

Replan menghasilkan new plan state dan MAY invalidate:

-   prior assignments;
-   authority applicability;
-   policy applicability;
-   risk classification;
-   verification;
-   approval.

Material invalidation MUST be represented.

------------------------------------------------------------------------

## 16.32 State and Cancellation

Cancellation SHOULD memiliki explicit state transition.

Cancellation does not guarantee external effect reversal.

System MUST distinguish:

\[ CancelledWorkflow\neq RevertedEffects\]

------------------------------------------------------------------------

## 16.33 State and Termination

Terminal states SHOULD include at least semantically equivalent
outcomes:

`Completed`, `Failed`, `Rejected`, `Aborted`, `Cancelled`.

Terminal transition MUST memiliki basis yang traceable.

------------------------------------------------------------------------

# 16.34 Trace Definition

Canonical trace event:

\[ x_i= \langle id, timestamp, actor, event, input, decision,
action, evidence, stateBefore, stateAfter, result, correlation
\rangle\]

Trace MAY store references rather than full payload.

**AOF-TRC-001** --- Consequential transition MUST menghasilkan
sufficient Trace untuk reconstruction sesuai applicable profile.

------------------------------------------------------------------------

## 16.35 Trace Purpose

Trace mendukung:

-   accountability;
-   audit;
-   debugging;
-   incident response;
-   verification;
-   failure learning;
-   conformance;
-   provenance;
-   state reconstruction;
-   security investigation.

Trace bukan sekadar application log.

------------------------------------------------------------------------

## 16.36 Trace Completeness

Trace completeness berarti sufficient consequential events tersedia
untuk menjawab:

-   siapa/apa bertindak;
-   terhadap task/resource apa;
-   decision apa;
-   authority/policy/risk basis apa;
-   action/effect apa;
-   evidence apa;
-   verification apa;
-   state berubah dari apa ke apa;
-   outcome apa.

Private chain-of-thought MUST NOT diperlukan.

------------------------------------------------------------------------

## 16.37 Trace Correlation

Trace events SHOULD memiliki correlation identifiers seperti:

-   session ID;
-   task ID;
-   action ID;
-   decision ID;
-   authority grant ID;
-   verification ID;
-   resource ID.

Correlation memungkinkan causal reconstruction.

------------------------------------------------------------------------

## 16.38 Trace Ordering

Implementation SHOULD menyediakan ordering yang cukup untuk
consequential reconstruction.

Possible mechanisms:

-   monotonic sequence;
-   event version;
-   causal link;
-   transaction sequence;
-   trusted timestamp.

Wall-clock timestamp saja MAY insufficient dalam distributed system.

------------------------------------------------------------------------

## 16.39 Trace Actor Identity

Trace SHOULD mengidentifikasi actor secara stable.

Actor MAY berupa:

-   Human;
-   Agent;
-   deterministic service;
-   external service;
-   orchestrator;
-   control component.

Shared generic identity SHOULD dihindari untuk high-assurance
consequential operations.

------------------------------------------------------------------------

## 16.40 Trace Decision Record

Consequential decision trace SHOULD merekam:

```text
decision_id
actor/evaluator
decision_type
subject
state reference
authority result
policy result
risk result
verification/approval status
outcome
timestamp
```

Rationale MAY structured tanpa private reasoning chain.

------------------------------------------------------------------------

## 16.41 Trace Action Record

Action trace SHOULD merekam:

```text
action_id
actor
operation
target
parameters/reference
permit/control decision
start
completion
result
effect evidence
```

Sensitive parameters MAY redacted atau referenced.

------------------------------------------------------------------------

## 16.42 Trace State Transition Record

Transition trace SHOULD merekam:

\[ stateBeforeRef \rightarrow decision \rightarrow
stateAfterRef \]

Jika full state terlalu besar, versioned references MAY digunakan.

------------------------------------------------------------------------

## 16.43 Trace Evidence References

Trace SHOULD menghubungkan evidence yang mendukung decision, action
result, verification, dan outcome.

Trace store tidak harus menyimpan evidence payload.

------------------------------------------------------------------------

## 16.44 Trace Integrity

Unauthorized modification terhadap trace MUST dicegah atau detectable
sesuai profile.

Possible mechanisms:

-   append-only store;
-   hash chaining;
-   signatures;
-   immutable retention;
-   protected audit service;
-   restricted write access.

High-assurance profile MUST mendefinisikan stronger integrity
requirements.

------------------------------------------------------------------------

## 16.45 Trace Immutability and Correction

Trace event SHOULD tidak silently overwritten.

Correction SHOULD menggunakan new event, annotation, supersession, atau
equivalent append-preserving mechanism.

\[ Correction\Rightarrow HistoricalVisibility\]

------------------------------------------------------------------------

## 16.46 Trace Availability

Required trace MUST tersedia selama applicable retention period.

Trace subsystem failure setelah consequential effect merupakan
governance failure.

System MUST NOT claim complete traceability jika mandatory trace
persistence failed.

------------------------------------------------------------------------

## 16.47 Trace Failure Before Effect

Jika mandatory trace cannot be recorded sebelum high-risk effect dan
profile requires pre-effect trace guarantee, action MUST become
`Pending`, `Denied`, atau `Escalated`.

Fail-open MAY only exist jika explicitly allowed by applicable
profile/policy.

------------------------------------------------------------------------

## 16.48 Trace Failure After Effect

Jika effect terjadi tetapi trace persistence gagal:

1.  mark audit gap;
2.  preserve available evidence;
3.  reconcile state;
4.  attempt trace recovery;
5.  escalate if required.

System MUST NOT fabricate missing trace.

------------------------------------------------------------------------

## 16.49 Trace Confidentiality

Trace dapat mengandung sensitive information.

Access MUST mengikuti Authority/Policy.

Trace SHOULD support redaction, field-level restriction, protected
references, atau equivalent mechanism.

------------------------------------------------------------------------

## 16.50 Trace Data Minimization

Trace SHOULD merekam sufficient governance data tanpa unnecessary
sensitive content.

\[ TraceData\approx MinimumSufficientAuditData\]

Private chain-of-thought MUST NOT disimpan sebagai conformance
requirement.

------------------------------------------------------------------------

## 16.51 Trace Retention

Trace retention SHOULD ditentukan oleh:

-   governance;
-   compliance;
-   security;
-   operational needs;
-   privacy;
-   domain profile.

Retention policy SHOULD distinguish operational logs dari governance
trace jika semantics berbeda.

------------------------------------------------------------------------

## 16.52 Trace Redaction

Redaction MUST mempertahankan audit meaning.

Jika material field disembunyikan dari viewer, protected original atau
reference SHOULD tersedia bagi authorized audit path bila applicable.

------------------------------------------------------------------------

## 16.53 Trace Export

Trace export ke external domain merupakan disclosure action dan MUST
tunduk pada Authority, Policy, Risk, dan data classification.

------------------------------------------------------------------------

## 16.54 Trace and Evidence

\[ Trace\neq EvidenceStore\]

Tetapi trace event MAY itself menjadi evidence.

Trace SHOULD reference evidence rather than duplicate sensitive payload
jika practical.

------------------------------------------------------------------------

## 16.55 Trace and Observability

Operational telemetry MAY lebih verbose daripada governance trace.

AOF hanya mensyaratkan sufficient observability untuk consequential
reconstruction.

Observability MUST NOT bergantung pada disclosure of private model
chain-of-thought.

------------------------------------------------------------------------

## 16.56 Trace and Failure Learning

Trace SHOULD memungkinkan reconstruction dari failure path:

```text
Task
 -> Decision
 -> Action
 -> Failure
 -> Evidence
 -> Retry/Replan
 -> Verification
 -> Outcome
```

Ini mendukung learning loop tanpa menghapus historical failures.

------------------------------------------------------------------------

## 16.57 Trace and Conformance

Conformance test MAY menggunakan trace sebagai proof bahwa requirement
dipenuhi.

\[ Requirement \rightarrow Test \rightarrow
Trace/Evidence \]

Trace alone MAY insufficient jika control effectiveness perlu evidence
lain.

------------------------------------------------------------------------

## 16.58 Trace Event Taxonomy

Reference event classes:

-   `SessionEvent`;
-   `TaskEvent`;
-   `AssignmentEvent`;
-   `AuthorityEvent`;
-   `PolicyEvent`;
-   `RiskEvent`;
-   `DecisionEvent`;
-   `ActionEvent`;
-   `EvidenceEvent`;
-   `VerificationEvent`;
-   `ApprovalEvent`;
-   `StateTransitionEvent`;
-   `FailureEvent`;
-   `RecoveryEvent`;
-   `EscalationEvent`;
-   `TerminationEvent`.

Extensions MAY menambahkan domain-specific events.

------------------------------------------------------------------------

## 16.59 State Failure Modes

### ST-F01 --- Hidden Mutation

Consequential state berubah di luar controlled path.

### ST-F02 --- Stale State

Decision menggunakan materially outdated state.

### ST-F03 --- Lost Update

Concurrent update silently overwritten.

### ST-F04 --- Duplicate Commit

Action/effect committed lebih dari intended.

### ST-F05 --- Partial Commit

Only subset dari intended mutation berhasil.

### ST-F06 --- Invalid Transition

Lifecycle transition tidak valid.

### ST-F07 --- State Drift

Authoritative/intended state berbeda dari observed resource state.

### ST-F08 --- Projection Error

Agent menerima state projection yang materially incorrect.

### ST-F09 --- Replay Violation

Historical decision/action replayed tanpa current validation.

### ST-F10 --- Version Ambiguity

Decision tidak dapat dikaitkan ke relevant state version.

------------------------------------------------------------------------

## 16.60 Trace Failure Modes

### TRC-F01 --- Missing Event

Consequential event tidak direkam.

### TRC-F02 --- Broken Correlation

Event tidak dapat dikaitkan dengan session/task/action.

### TRC-F03 --- Ordering Ambiguity

Causal sequence tidak dapat direkonstruksi.

### TRC-F04 --- Actor Ambiguity

Actor tidak identifiable.

### TRC-F05 --- Unauthorized Mutation

Trace diubah tanpa valid process.

### TRC-F06 --- Retention Failure

Required trace hilang terlalu dini.

### TRC-F07 --- Sensitive Data Leakage

Trace mengungkap data melampaui authorized scope.

### TRC-F08 --- Fabricated Trace

Missing event diganti dengan invented record.

### TRC-F09 --- Trace Persistence Failure

Effect terjadi tetapi required trace tidak durable.

### TRC-F10 --- Incomplete Governance Basis

Decision trace tidak cukup untuk menjelaskan control outcome.

------------------------------------------------------------------------

## 16.61 Reference State Transition Algorithm

```text
INPUT:
  current authoritative state
  candidate decision
  candidate action
  expected state version

1. Resolve state scope and current version.
2. Validate expected version/freshness.
3. Validate lifecycle transition.
4. Validate prerequisites.
5. Validate Authority/Policy/Risk/Verification obligations.
6. Detect concurrency conflict.
7. If unresolved:
      PENDING / REPLAN / ESCALATE
8. Execute governed action if applicable.
9. Capture result/effect evidence.
10. Determine actual post-state.
11. Commit state transition.
12. Record trace atomically or with equivalent recoverable semantics.
13. Return new state reference and transition result.
```

------------------------------------------------------------------------

## 16.62 Reference Trace Recording Algorithm

```text
INPUT:
  event
  actor
  decision/action
  state before/after
  evidence references
  correlation context

1. Assign event identity.
2. Resolve actor identity.
3. Bind correlation identifiers.
4. Record timestamp/ordering metadata.
5. Record decision/action/result.
6. Bind state references.
7. Bind evidence/verification references.
8. Apply classification/redaction rules.
9. Persist with required integrity guarantees.
10. Return trace reference.
```

------------------------------------------------------------------------

## 16.63 State Conformance Requirements

### Core

**AOF-ST-005** --- Invalid lifecycle transition MUST NOT silently
committed.

**AOF-ST-006** --- Agent private memory MUST NOT menjadi sole
authoritative consequential state.

**AOF-ST-007** --- Partial commit MUST represented sebagai
partial/reconciled condition, bukan atomic success.

**AOF-ST-008** --- Replay yang dapat menghasilkan new effect MUST
melalui current control validation.

### Governed

**AOF-ST-009** --- Retry MUST mempertimbangkan current state dan prior
effect.

**AOF-ST-010** --- Material replan MUST invalidate/reassess affected
governance state.

**AOF-ST-011** --- High-risk Effect Boundary SHOULD revalidate
materially mutable state.

**AOF-ST-012** --- Cancellation MUST distinguish workflow termination
dari effect reversal.

**AOF-ST-013** --- External state drift yang material MUST menghasilkan
reconciliation/control response.

**AOF-ST-014** --- State transitions MUST memiliki sufficient
correlation dengan decision/action.

### Assured / High-Assurance

**AOF-ST-015** --- High-assurance profile MUST menentukan state
consistency/freshness requirements.

**AOF-ST-016** --- High-assurance shared state MUST memiliki defined
concurrency and recovery semantics.

**AOF-ST-017** --- High-assurance state mutation MUST support
independent reconstruction dari Trace/Evidence.

**AOF-ST-018** --- High-assurance permit SHOULD bind ke relevant state
version atau equivalent anti-TOCTOU control.

------------------------------------------------------------------------

## 16.64 Trace Conformance Requirements

### Core

**AOF-TRC-001 (canonical cross-reference)** — See the primary normative definition above.
sufficient Trace.

**AOF-TRC-002** --- Trace MUST identify consequential
actor/event/result.

**AOF-TRC-003** --- Trace SHOULD menyediakan sufficient correlation
untuk session/task/action reconstruction.

**AOF-TRC-004** --- Trace MUST NOT memerlukan private chain-of-thought.

**AOF-TRC-005** --- Trace correction MUST NOT silently erase historical
governance meaning.

**AOF-TRC-006** --- Mandatory trace failure MUST NOT disembunyikan
sebagai complete traceability.

### Governed

**AOF-TRC-007** --- Consequential decision trace SHOULD merekam
applicable governance results/references.

**AOF-TRC-008** --- Trace MUST tunduk pada data classification/access
policy.

**AOF-TRC-009** --- Required trace MUST retained sesuai applicable
policy/profile.

**AOF-TRC-010** --- Trace SHOULD preserve ordering/causal information
yang cukup.

**AOF-TRC-011** --- Effect with trace persistence failure MUST memicu
controlled recovery/audit-gap handling.

**AOF-TRC-012** --- Trace export MUST diperlakukan sebagai governed
disclosure.

### Assured / High-Assurance

**AOF-TRC-013** --- High-assurance trace MUST memiliki tamper-resistant
atau tamper-evident integrity sesuai profile.

**AOF-TRC-014** --- High-assurance consequential trace MUST support
independent reconstruction.

**AOF-TRC-015** --- High-assurance profile MUST menentukan retention,
integrity, ordering, actor identity, dan confidentiality semantics.

**AOF-TRC-016** --- High-assurance audit gaps MUST explicit dan MUST NOT
silently normalized.

------------------------------------------------------------------------

## 16.65 State Invariants

### ST-INV-01 --- Authoritative State

\[ AuthoritativeState\neq AgentPrivateMemory\]

### ST-INV-02 --- Controlled Mutation

\[ ConsequentialStateChange\Rightarrow ControlledTransition\]

### ST-INV-03 --- State Validity

\[ Commit(\Delta)\Rightarrow StateValid(\Delta)
\]

### ST-INV-04 --- Conflict Control

\[ ConcurrentConflict\Rightarrow NoSilentCommit\]

### ST-INV-05 --- Replay Revalidation

\[ ReplayWithEffect\Rightarrow CurrentControlValidation\]

### ST-INV-06 --- Partial Effect Honesty

\[ PartialEffect\not\Rightarrow AtomicSuccess\]

### ST-INV-07 --- Replan Consistency

\[ MaterialReplan\Rightarrow ReevaluateAffectedState\]

### ST-INV-08 --- TOCTOU Control

\[ MaterialStateChange\Rightarrow RevalidateBeforeEffect\]

sesuai profile/risk.

------------------------------------------------------------------------

## 16.66 Trace Invariants

### TRC-INV-01 --- Trace Completeness

\[ ConsequentialTransition\Rightarrow SufficientTrace\]

### TRC-INV-02 --- Attribution

\[ ConsequentialEvent\Rightarrow IdentifiableActor\]

### TRC-INV-03 --- Correlation

\[ TraceEvent\Rightarrow ReconstructableContext\]

untuk consequential events.

### TRC-INV-04 --- Historical Preservation

\[ Correction\Rightarrow NoSilentHistoricalErase\]

### TRC-INV-05 --- Trace Integrity

\[ UnauthorizedMutation\Rightarrow PreventedOrDetectable\]

sesuai profile.

### TRC-INV-06 --- No Fabrication

\[ MissingTrace\not\Rightarrow InventedTrace\]

### TRC-INV-07 --- Trace Confidentiality

\[ TraceAccess\Rightarrow AuthorizedAccess\]

### TRC-INV-08 --- Chain-of-Thought Independence

\[ ConformanceTrace\not\Rightarrow PrivateChainOfThought
\]

------------------------------------------------------------------------

## 16.67 State--Trace Coherence

Canonical invariant:

\[ CommittedTransition(s_i,s_j) \Rightarrow Traceable(s_i,s_j)
\]

dan:

\[ TraceClaimsTransition(x) \Rightarrow
ConsistentWithAuthoritativeState(x) \]

State dan Trace MAY disimpan terpisah, tetapi contradiction yang
material MUST detectable/reconciled.

------------------------------------------------------------------------

## 16.68 Architecture Integration

Reference flow:

```text
Current State
     |
     v
Control Evaluation
     |
     v
Decision
     |
     v
Effect Boundary
     |
     v
Action / Effect
     |
     v
Evidence
     |
     v
Post-State Determination
     |
     v
State Commit
     |
     v
Trace Record
```

Implementation MAY menggunakan transactional coupling atau recoverable
event sequence. Yang diwajibkan adalah semantic coherence, bukan
technology tertentu.

------------------------------------------------------------------------

## 16.69 State & Trace Freeze Candidate Criteria

Area ini MAY dinyatakan `Freeze Candidate` jika:

1.  authoritative state semantics stabil;
2.  controlled transition semantics stabil;
3.  state version/freshness semantics stabil;
4.  concurrency/conflict/replay semantics stabil;
5.  partial commit/reconciliation semantics stabil;
6.  trace event semantics stabil;
7.  trace integrity/confidentiality/retention semantics compatible
    dengan Security;
8.  State--Trace Coherence stabil;
9.  retry/replan/cancellation semantics compatible dengan Failure &
    Recovery;
10. conformance requirements dapat dipetakan ke tests;
11. schema representation dapat dibuat tanpa semantic ambiguity.

------------------------------------------------------------------------

## 16.70 State & Trace Formalization Result

State & Trace v1.0 RC-State-Trace diringkas sebagai:

\[ StateGovernance= AuthoritativeState + ControlledTransition +
Versioning + Consistency + Reconciliation \]

\[ TraceGovernance= Attribution + Correlation + Ordering + Integrity +
Retention + Confidentiality + Reconstruction \]

dengan:

\[ \boxed{ AgentMemory\neq AuthoritativeState } \]

\[
\boxed{ No\ Consequential\ State\ Change\ Without\ Controlled\ Transition }
\]

\[ \boxed{ Committed\ Transition\Rightarrow Sufficient\ Trace }
\]

dan:

\[
\boxed{ Traceability\ Does\ Not\ Require\ Private\ Chain\ of\ Thought }
\] \# 17. Human Governance

## 17.1 Purpose

`Human Governance` mendefinisikan posisi Human dan Organization sebagai
governance root AOF, termasuk ownership atas Intent, organizational
objectives, governance policy, delegation boundaries, risk acceptance,
accountability, approval, override, dan emergency authority.

AOF membedakan secara tegas:

\[
Human/Organization Governance\neq Human In Every Execution Loop
\]

AOF tidak mensyaratkan Human approval untuk setiap Action. Sebaliknya,
Human/Organization menetapkan `Governance Envelope` di mana bounded
operational autonomy dapat berlangsung.

Canonical formulation:

\[ Human/Organization=GovernanceRoot \]

\[ Agent=BoundedOperationalActor \]

\[ AgentAutonomy\subset eq
Human/OrganizationalGovernanceEnvelope \]

------------------------------------------------------------------------

## 17.2 Governance Root

`Governance Root` adalah ultimate organizational source untuk legitimate
delegation, policy authority, risk acceptance authority, dan
accountability assignment dalam deployment AOF.

Governance Root MAY diwujudkan melalui:

-   individual Human;
-   authorized organizational role;
-   governance board;
-   delegated management function;
-   legal/contractual authority structure;
-   combination thereof.

AOF tidak mengasumsikan satu Human memiliki unlimited power.

\[ GovernanceRoot\neq OmnipotentHuman\]

**AOF-HG-001** --- Deployment MUST identify authoritative
Human/organizational governance root atau equivalent accountable
governance structure.

------------------------------------------------------------------------

## 17.3 Human Intent

Human/Organization menetapkan legitimate Intent yang menjadi dasar Goal
dan Task creation.

Reference chain:

\[
Intent\rightarrow Goal\rightarrow Task\rightarrow Decision\rightarrow Action\rightarrow Outcome
\]

Intent SHOULD mencakup sufficient purpose, constraints, dan success
boundaries untuk consequential workflows.

Agent MAY refine operational interpretation tetapi MUST NOT silently
replace governing Intent.

------------------------------------------------------------------------

## 17.4 Intent Integrity

Material change terhadap governing Intent MUST diperlakukan sebagai
governance change, bukan ordinary planning optimization.

\[ OperationalOptimization\not\Rightarrow IntentMutation
\]

Jika proposed plan tidak dapat memenuhi Intent tanpa mengubah material
constraints, system SHOULD `Escalate`, `Reject`, atau request authorized
change.

**AOF-HG-002** --- Agent MUST NOT unilaterally redefine governing
Intent, Goal success criteria, atau mandatory organizational
constraints.

------------------------------------------------------------------------

## 17.5 Organizational Goal Ownership

Organization/Human governance menentukan Goal legitimacy dan success
criteria.

Agent MAY:

-   decompose Goal;
-   propose alternative Goal wording;
-   identify conflicts;
-   recommend success criteria;
-   identify infeasibility.

Agent MUST NOT self-legitimize a new organizational Goal.

------------------------------------------------------------------------

## 17.6 Governance Envelope

`Governance Envelope` mendefinisikan bounded operating space:

\[ GE= \langle Intent, Authority, Policy, RiskLimits,
ContextScope, ResourceScope, VerificationRequirements, ApprovalRules,
TemporalLimits \rangle\]

Operational Agent autonomy MUST remain inside applicable Governance
Envelope.

\[ Agency(a)\subset eq GE_a \]

------------------------------------------------------------------------

## 17.7 Delegated Operational Authority

Human/Organization MAY delegate operational Authority kepada Agent
sesuai Authority Model.

\[ DelegatedOperationalAuthority \subset eq
OrganizationalGovernanceAuthority \]

Delegation MAY memungkinkan Agent menjalankan Action tanpa per-action
Human approval jika:

-   Authority valid;
-   Policy satisfied;
-   State valid;
-   Risk acceptable;
-   required Verification satisfied;
-   applicable approval rule does not require Human approval.

**AOF-HG-003** --- Human governance MUST be able to bound delegated
operational Authority by scope, resource, operation, constraints, dan
validity.

------------------------------------------------------------------------

## 17.8 Governance Authority vs Operational Authority

AOF membedakan:

`OrganizationalGovernanceAuthority` --- authority untuk
menetapkan/delegasikan governance rules, organizational intent, risk
acceptance, dan accountability structure.

`DelegatedOperationalAuthority` --- authority untuk melakukan bounded
operational actions.

Canonical separation:

\[ OrganizationalGovernanceAuthority \neq
DelegatedOperationalAuthority \]

Operational delegation MUST NOT automatically transfer governance-root
status.

------------------------------------------------------------------------

## 17.9 Accountability Non-Transfer

Operational execution dapat didelegasikan; organizational accountability
mengikuti applicable governance, policy, contract, dan law.

\[
DelegatedExecution\not\Rightarrow AutomaticAccountabilityTransfer
\]

AOF tidak menentukan legal liability. AOF menyediakan Trace dan
accountability chain agar responsibility dapat direkonstruksi.

**AOF-HG-004** --- Delegation record MUST preserve delegator/delegatee
provenance untuk consequential delegated Authority.

------------------------------------------------------------------------

## 17.10 Human as Agent

Human MAY direpresentasikan sebagai `AgentType=Human`.

Human Agent dapat:

-   propose;
-   review;
-   approve;
-   reject;
-   execute;
-   verify;
-   escalate;
-   override jika authorized.

Human-as-Agent representation memungkinkan Human participation menjadi
bagian dari same State, Decision, Evidence, dan Trace model.

------------------------------------------------------------------------

## 17.11 Human Is Not Implicitly Unlimited

Human participation tidak otomatis menghilangkan Authority, Policy,
Risk, State, atau Trace requirements.

\[ HumanPresence\not\Rightarrow UnlimitedAuthority\]

\[ HumanAction\not\Rightarrow PolicyExemption\]

Profile MAY memberikan Human role broader Authority, tetapi grant
tersebut MUST explicit atau berasal dari documented governance source.

**AOF-HG-005** --- Human actor MUST NOT be treated as implicitly
unlimited within governed execution solely because actor is Human.

------------------------------------------------------------------------

## 17.12 Human Identity

Consequential Human governance decision SHOULD bind ke
authenticated/verified actor identity sesuai risk.

Identity MAY berupa:

-   organizational identity;
-   authenticated account;
-   cryptographic identity;
-   approved role binding;
-   equivalent identity mechanism.

High-Assurance profile SHOULD require stronger identity assurance untuk
high-impact approval/override.

------------------------------------------------------------------------

## 17.13 Human Role and Authority Binding

Human role title tidak otomatis membuktikan Authority.

\[ Role\neq Authority\]

System SHOULD resolve:

\[ HumanIdentity + Role + AuthorityGrant + Scope \rightarrow
EffectiveHumanAuthority \]

------------------------------------------------------------------------

## 17.14 Human Approval

`Approval` adalah explicit governance Decision yang menyatakan bahwa
authorized Human/approver accepts progression untuk defined subject dan
scope.

Approval MUST NOT dianggap generic unlimited permission.

Canonical:

\[ Approval= \langle subject, approver, authority, scope,
conditions, version, validity, decision \rangle\]

------------------------------------------------------------------------

## 17.15 Approval Is Not Authority Grant

Approval dan Authority adalah constructs berbeda.

\[ Approval\neq AuthorityGrant\]

Approval MAY satisfy a required gate, tetapi tidak menciptakan unrelated
Authority.

\[ Approved(x)\not\Rightarrow Authorized(y) \]

untuk unrelated (y).

**AOF-HG-006** --- Approval MUST NOT implicitly expand actor/action
Authority beyond approved subject and scope.

------------------------------------------------------------------------

## 17.16 Approval Scope

Approval SHOULD bind ke:

-   specific Task/Action/Plan/Release;
-   material parameters;
-   target/resource;
-   applicable risk;
-   subject version;
-   time/validity;
-   conditions.

Blanket approval SHOULD NOT digunakan untuk high-risk action kecuali
explicitly permitted oleh profile dan bounded governance policy.

------------------------------------------------------------------------

## 17.17 Approval Freshness

\[ Approval\_{t_1}\not\Rightarrow Approval\_{t_2} \]

jika material conditions berubah.

Reapproval SHOULD required jika terjadi material change pada:

-   target;
-   operation;
-   parameters;
-   risk;
-   plan;
-   Authority;
-   Policy;
-   State;
-   artifact version;
-   security posture.

------------------------------------------------------------------------

## 17.18 Approval Lifecycle

Reference lifecycle:

```text
Requested
   |
   v
Pending
   |
   +--> Approved
   +--> Rejected
   +--> Expired
   +--> Cancelled
   +--> Superseded
```

Approved state MAY later become invalid karena expiry, subject change,
revocation, atau superseding governance decision.

------------------------------------------------------------------------

## 17.19 Approval Evidence

Consequential approval SHOULD menghasilkan Evidence/Trace yang mencakup:

-   approver identity;
-   Authority basis;
-   subject;
-   scope;
-   decision;
-   timestamp;
-   conditions;
-   relevant Evidence references;
-   risk information;
-   version/freshness binding.

Approval record SHOULD tidak memerlukan private Human reasoning beyond
rationale required by policy.

------------------------------------------------------------------------

## 17.20 Approval Rejection

Rejection MUST NOT silently converted menjadi approval melalui retry
atau alternate Agent.

\[ RejectedApproval\not\Rightarrow RetryUntilApproved\]

Alternate approver MAY digunakan hanya jika governance policy
mengizinkan dan Authority valid.

------------------------------------------------------------------------

## 17.21 Approval Conflict

Jika multiple valid Human decisions conflict, system MUST apply defined
governance resolution.

Possible resolution:

-   policy precedence;
-   role precedence;
-   quorum;
-   escalation;
-   deny;
-   higher authority review.

Unknown conflict MUST NOT implicit Allow.

------------------------------------------------------------------------

## 17.22 Approval Quorum

Profile MAY require quorum:

\[ ApprovalSatisfied \iffCount(EligibleApprovals)\geq q
\]

Quorum MUST evaluate eligible independent approvers sesuai policy.

Duplicate identity/session MUST NOT dihitung sebagai multiple
independent approvals.

------------------------------------------------------------------------

## 17.23 Separation of Duties

High-risk governance SHOULD memisahkan incompatible roles.

Examples:

\[ Proposer\neq Approver\]

\[ Approver\neq IndependentVerifier\]

jika profile requires independence.

Human participation MUST NOT automatically satisfy independent
verification jika Human yang sama adalah proposer/executor dan profile
melarang circular assurance.

------------------------------------------------------------------------

## 17.24 Human Risk Acceptance

Risk acceptance adalah governance Decision berbeda dari risk assessment.

\[ RiskAssessment\neq RiskAcceptance\]

Human/organizational role MAY accept residual risk hanya jika memiliki
applicable acceptance Authority.

Risk acceptance SHOULD bind ke:

-   subject;
-   residual risk;
-   conditions;
-   duration;
-   scope;
-   owner;
-   evidence;
-   review trigger.

------------------------------------------------------------------------

## 17.25 Risk Acceptance Is Not Control Removal

\[ RiskAccepted\not\Rightarrow AllControlsDisabled\]

Acceptance MAY permit progression terhadap explicitly accepted residual
risk, tetapi mandatory security/legal/policy controls tetap berlaku
kecuali valid governance mechanism explicitly mengubahnya.

**AOF-HG-007** --- Residual risk acceptance MUST NOT implicitly disable
unrelated mandatory controls.

------------------------------------------------------------------------

## 17.26 Human Override

`Override` adalah explicit authorized governance Decision yang mengganti
normal decision path dalam bounded circumstances.

Override MUST:

-   memiliki valid Authority;
-   memiliki defined subject/scope;
-   memiliki rationale;
-   identify overridden rule/decision jika applicable;
-   record residual risk;
-   be traceable;
-   preserve non-overridable constraints.

\[ Override\neq ControlBypass\]

------------------------------------------------------------------------

## 17.27 Override Boundary

Tidak semua control dapat dioverride.

Deployment/Profile MUST classify applicable controls sebagai:

-   `Overridable`;
-   `ConditionallyOverridable`;
-   `NonOverridable`.

Examples dari potentially non-overridable constraints MAY berasal dari:

-   law;
-   contractual obligation;
-   hard safety boundary;
-   tenant isolation;
-   cryptographic integrity;
-   organizational prohibition.

**AOF-HG-008** --- Override MUST NOT bypass a control classified
`NonOverridable`.

------------------------------------------------------------------------

## 17.28 Override Authority

Authority untuk ordinary approval tidak otomatis mencakup override.

\[ ApprovalAuthority\not\Rightarrow OverrideAuthority\]

Override Authority SHOULD lebih sempit dan explicitly granted untuk
high-risk contexts.

------------------------------------------------------------------------

## 17.29 Override Lifecycle

Reference:

```text
OverrideRequested
       |
       v
EvaluateAuthority
       |
       +--> Denied
       +--> Pending
       +--> Authorized
                  |
                  v
             Applied
                  |
                  v
           Review/Expire
```

Applied override SHOULD memiliki validity/expiry jika temporary.

------------------------------------------------------------------------

## 17.30 Override Evidence

Override Trace SHOULD mencakup:

-   actor;
-   Authority;
-   affected control/decision;
-   reason;
-   subject;
-   scope;
-   risk;
-   expected consequence;
-   duration;
-   approval/evidence;
-   post-action review requirement.

------------------------------------------------------------------------

## 17.31 Break-Glass

`Break-Glass` adalah emergency governance mechanism untuk memperoleh
narrowly bounded emergency operational capability ketika normal path
tidak dapat memenuhi urgent safety/business/security need.

Break-Glass bukan universal superuser mode.

\[ BreakGlass\neq UnlimitedAuthority\]

------------------------------------------------------------------------

## 17.32 Break-Glass Preconditions

Break-Glass SHOULD hanya available jika predefined emergency conditions
berlaku, misalnya:

-   imminent material harm;
-   critical service restoration;
-   security containment;
-   loss of normal approval path;
-   urgent safety intervention.

Mere convenience atau cost reduction SHOULD NOT menjadi sufficient
trigger.

------------------------------------------------------------------------

## 17.33 Break-Glass Authority Contract

Reference:

\[ BG= \langle subject, emergency, operations, resources, scope,
issuer, constraints, validity, monitoring, review \rangle\]

Break-Glass Authority SHOULD:

-   narrow;
-   time-limited;
-   purpose-limited;
-   auditable;
-   revocable;
-   independently reviewable.

------------------------------------------------------------------------

## 17.34 Break-Glass Does Not Disable Audit

\[ BreakGlass\not\Rightarrow NoAudit\]

Jika normal Trace subsystem unavailable, implementation SHOULD preserve
alternative emergency evidence dan reconcile ke authoritative Trace
setelah recovery.

**AOF-HG-009** --- Break-Glass use MUST produce or preserve auditable
governance evidence.

------------------------------------------------------------------------

## 17.35 Break-Glass Does Not Eliminate Risk

Emergency context dapat meningkatkan accepted risk tetapi tidak mengubah
risk menjadi zero.

\[ Emergency\not\Rightarrow RiskFree\]

Residual risk SHOULD explicit dan post-event review SHOULD assess
consequences.

------------------------------------------------------------------------

## 17.36 Break-Glass Expiry

Emergency Authority MUST expire atau be explicitly revoked ketika
emergency scope berakhir.

\[ EmergencyEnded\Rightarrow RevokeOrExpire(BreakGlassAuthority)
\]

Persistent emergency privilege tanpa review merupakan governance
failure.

------------------------------------------------------------------------

## 17.37 Break-Glass Post-Review

Post-event review SHOULD mencakup:

-   trigger validity;
-   actor Authority;
-   actions/effects;
-   residual harm;
-   controls bypassed/overridden;
-   evidence completeness;
-   recovery;
-   lessons learned;
-   whether governance design needs improvement.

------------------------------------------------------------------------

## 17.38 Human Unavailability

Required Human decision MAY unavailable.

System MUST NOT fabricate approval.

\[ HumanUnavailable\not\Rightarrow Approved\]

Possible outcomes:

-   `Pending`;
-   alternate authorized approver;
-   escalation;
-   bounded safe degradation;
-   abort;
-   valid Break-Glass path.

**AOF-HG-010** --- Required Human unavailability MUST NOT produce
implicit approval.

------------------------------------------------------------------------

## 17.39 Approval Timeout

Approval request SHOULD memiliki timeout/expiry behavior sesuai risk.

Timeout MUST NOT default to approval.

\[ ApprovalTimeout\Rightarrow\neg ImplicitApproval\]

------------------------------------------------------------------------

## 17.40 Human Decision Latency

Orchestration MAY optimize Human involvement dengan risk-proportional
gates.

Low-risk actions MAY execute within delegated envelope tanpa Human
interaction.

Critical actions MAY require explicit Human approval.

AOF goal adalah bounded autonomy, bukan mandatory Human micromanagement.

------------------------------------------------------------------------

## 17.41 Human-in-the-Loop vs Human-on-the-Loop

AOF MAY support:

-   `Human-in-the-Loop` --- Human decision required sebelum progression;
-   `Human-on-the-Loop` --- Human supervises bounded autonomous
    execution;
-   `Human-out-of-immediate-loop` --- operational execution proceeds
    under pre-authorized governance envelope.

Semua modes tetap berada di bawah organizational governance.

------------------------------------------------------------------------

## 17.42 Human Governance and Autonomy Levels

Higher operational autonomy MUST NOT imply removal of governance root.

\[ AutonomyLevel\uparrow\not\Rightarrow
GovernanceAuthority\uparrow\]

Autonomy increase SHOULD require sufficient Authority, Policy, Risk
controls, Verification, observability, dan recovery.

------------------------------------------------------------------------

## 17.43 Delegation to AI

Delegation kepada AI Agent MUST specify bounded operational
responsibility.

AI Agent MAY:

-   plan;
-   recommend;
-   generate;
-   execute;
-   coordinate;
-   verify jika independence permits.

AI Agent MUST NOT infer unlimited delegation dari vague organizational
intent.

------------------------------------------------------------------------

## 17.44 No Authority Laundering Through AI

Human/Agent MUST NOT use delegation chain untuk memperoleh effect yang
original actor tidak authorized untuk initiate jika Authority Model
melarangnya.

\[ DelegationChain\not\Rightarrow PrivilegeExpansion\]

------------------------------------------------------------------------

## 17.45 AI Cannot Self-Appoint Governance Root

\[ AIAgent\not\Rightarrow GovernanceRoot\]

Agent MUST NOT self-assign:

-   ultimate organizational authority;
-   risk acceptance authority;
-   override authority;
-   Break-Glass authority;
-   approval authority.

Authority harus berasal dari valid governance chain.

------------------------------------------------------------------------

## 17.46 Organizational Accountability

AOF distinguishes:

-   execution responsibility;
-   decision responsibility;
-   governance responsibility;
-   organizational accountability;
-   legal liability.

Framework memformalkan first four sejauh representable dalam system
governance.

Legal liability ditentukan oleh applicable law/contract dan berada di
luar AOF determination.

------------------------------------------------------------------------

## 17.47 Accountability Chain

Reference:

\[ Intent \rightarrow Goal\rightarrow Task
\rightarrow Decision\rightarrow Authority
\rightarrow Policy\rightarrow Action
\rightarrow Evidence\rightarrow Verification
\rightarrow Outcome\]

Human governance SHOULD dapat ditelusuri pada points yang memerlukan
organizational decision.

------------------------------------------------------------------------

## 17.48 Responsibility Assignment

Governance-critical workflow SHOULD identify responsible role untuk:

-   Goal ownership;
-   Authority issuance;
-   Policy ownership;
-   Risk ownership;
-   approval;
-   override;
-   Break-Glass;
-   incident response;
-   residual risk acceptance.

Satu role MAY memegang multiple responsibilities hanya jika
separation-of-duties requirements tetap satisfied.

------------------------------------------------------------------------

## 17.49 Accountability Cannot Be Erased by Automation

\[ Automation\not\Rightarrow AccountabilityErasure\]

Absence of Human interaction pada individual Action tidak berarti
absence of organizational governance/accountability.

------------------------------------------------------------------------

## 17.50 Human Governance and Policy

Human governance MAY author/approve Policy melalui valid governance
process.

Runtime Human request MUST NOT automatically override active Policy.

\[ HumanRequest\neq PolicyMutation\]

Policy mutation SHOULD menggunakan defined Policy lifecycle.

------------------------------------------------------------------------

## 17.51 Human Governance and Authority

Human governance dapat grant/revoke/suspend Authority sesuai Authority
Model.

Human MAY memiliki Authority untuk delegate tetapi tidak necessarily
untuk perform every delegated operation.

Authority provenance MUST remain explicit.

------------------------------------------------------------------------

## 17.52 Human Governance and Risk

Human governance menetapkan:

-   risk appetite/tolerance;
-   classification rules;
-   acceptance thresholds;
-   escalation thresholds;
-   acceptance Authority.

Agent MAY assess/recommend risk, tetapi acceptance of residual
organizational risk MUST follow valid governance authority.

------------------------------------------------------------------------

## 17.53 Human Governance and Evidence

Human decisions SHOULD menggunakan sufficient Evidence sesuai risk.

Human assertion sendiri MAY menjadi Evidence untuk facts within Human
authority/knowledge, tetapi:

\[ HumanAssertion\not\Rightarrow UniversalVerifiedFact\]

Evidence quality/provenance rules tetap berlaku.

------------------------------------------------------------------------

## 17.54 Human Governance and Verification

Human MAY menjadi verifier.

Human verification MUST memenuhi applicable:

-   capability;
-   independence;
-   criteria;
-   evidence;
-   Authority jika required.

Human identity tidak otomatis membuat verification independent.

------------------------------------------------------------------------

## 17.55 Human Governance and State

Human governance Decision yang consequential MUST masuk authoritative
State melalui controlled transition.

\[ HumanDecision\not\Rightarrow SilentStateMutation\]

------------------------------------------------------------------------

## 17.56 Human Governance and Trace

Consequential Human governance events SHOULD traceable, termasuk:

-   grant;
-   revoke;
-   approve;
-   reject;
-   override;
-   Break-Glass;
-   risk acceptance;
-   policy change;
-   escalation resolution.

Trace MUST respect privacy/data minimization.

------------------------------------------------------------------------

## 17.57 Human Governance and Security

Human channels merupakan security boundary.

Threats mencakup:

-   identity spoofing;
-   account compromise;
-   social engineering;
-   approval fatigue;
-   misleading evidence;
-   coercion;
-   session hijacking;
-   replay;
-   overbroad privilege.

Security Profile SHOULD menentukan controls sesuai risk.

------------------------------------------------------------------------

## 17.58 Approval Fatigue

Excessive low-value approval gates dapat mengurangi governance quality.

AOF SHOULD menggunakan risk-proportional approval.

\[ MoreApprovals\not\Rightarrow BetterGovernance\]

Design SHOULD prefer meaningful approval points dengan adequate
evidence/context.

------------------------------------------------------------------------

## 17.59 Decision Presentation

Approval/override interface SHOULD menyajikan sufficient decision
context, misalnya:

-   requested action;
-   target;
-   material parameters;
-   risk;
-   evidence;
-   verification;
-   alternatives;
-   expected effect;
-   residual risk.

Interface SHOULD menghindari misleading simplification untuk high-risk
decisions.

------------------------------------------------------------------------

## 17.60 Human Error

Human decision dapat salah.

AOF tidak menganggap Human infallible.

Controls MAY mencakup:

-   independent review;
-   quorum;
-   verification;
-   policy constraints;
-   bounded Authority;
-   post-action monitoring;
-   reversal/compensation.

\[ HumanDecision\neq GuaranteedCorrectDecision\]

------------------------------------------------------------------------

## 17.61 Human Conflict of Interest

Profile MAY require conflict-of-interest declaration atau independent
approver untuk sensitive decisions.

Known conflict SHOULD mempengaruhi approver eligibility sesuai policy.

------------------------------------------------------------------------

## 17.62 Legal and Regulatory Boundary

AOF tidak menentukan legal validity dari Human consent, signature,
delegation, liability, atau regulatory approval.

Implementation MUST apply applicable law/regulation/contract
independently.

AOF approval object tidak otomatis equivalent dengan legal signature.

------------------------------------------------------------------------

## 17.63 Non-Delegable Governance Responsibilities

Organization MAY classify responsibilities sebagai non-delegable kepada
AI.

Examples MAY include:

-   final legal attestation;
-   regulated sign-off;
-   employment decisions;
-   risk acceptance above threshold;
-   policy exceptions;
-   emergency authority issuance.

Classification harus berasal dari applicable governance source.

------------------------------------------------------------------------

## 17.64 Governance Change Management

Material changes terhadap:

-   governance root;
-   approval thresholds;
-   override policy;
-   Break-Glass rules;
-   risk acceptance authority;
-   delegation limits;

SHOULD versioned, reviewed, dan traceable.

------------------------------------------------------------------------

## 17.65 Governance Continuity

Organization SHOULD define continuity ketika key Human role unavailable.

Continuity MAY mencakup:

-   alternate role;
-   succession;
-   quorum;
-   escalation;
-   emergency process.

Continuity MUST NOT create undocumented unlimited authority.

------------------------------------------------------------------------

## 17.66 Human Governance Failure Taxonomy

### HG-F01 --- Intent Drift

Operational behavior bergeser dari governing Intent.

### HG-F02 --- Unauthorized Approval

Approval dibuat tanpa applicable Authority.

### HG-F03 --- Stale Approval

Old approval digunakan setelah material change.

### HG-F04 --- Approval Scope Creep

Approval digunakan di luar subject/scope.

### HG-F05 --- Implicit Human Omnipotence

Human actor dianggap unlimited tanpa grant.

### HG-F06 --- Override Abuse

Override digunakan sebagai ordinary bypass.

### HG-F07 --- Break-Glass Abuse

Emergency mechanism digunakan tanpa valid emergency.

### HG-F08 --- Persistent Emergency Privilege

Break-Glass Authority tidak expired/revoked.

### HG-F09 --- Accountability Loss

Delegation membuat responsibility chain tidak dapat direkonstruksi.

### HG-F10 --- Approval Fabrication

System menganggap Human unavailable sebagai approved.

### HG-F11 --- Governance Conflict

Conflicting Human decisions tidak memiliki resolution path.

### HG-F12 --- Approval Fatigue

Approval process menghasilkan low-quality rubber-stamping.

### HG-F13 --- Risk Acceptance Overreach

Actor menerima risk di luar Authority.

### HG-F14 --- Governance Channel Compromise

Human identity/approval channel compromised.

------------------------------------------------------------------------

## 17.67 Reference Human Approval Algorithm

```text
INPUT:
  approval request
  subject
  current state
  risk
  evidence
  candidate approver

1. Resolve approver identity.
2. Validate approval Authority.
3. Validate subject and scope.
4. Validate subject version/freshness.
5. Validate required Evidence.
6. Validate separation-of-duties/quorum.
7. Present material risk/effect information.
8. Obtain explicit:
      APPROVE
      REJECT
      ESCALATE
9. Bind decision to subject/version/scope.
10. Update authoritative State.
11. Record Evidence + Trace.
```

Unknown/timeout MUST NOT become `APPROVE`.

------------------------------------------------------------------------

## 17.68 Reference Override Algorithm

```text
INPUT:
  override request
  actor
  target control/decision
  reason
  risk
  state

1. Resolve actor identity.
2. Validate explicit Override Authority.
3. Determine whether target is overridable.
4. Validate scope and emergency/exception conditions.
5. Reassess risk.
6. Determine required independent approval/quorum.
7. Record rationale and affected controls.
8. If authorized:
      issue bounded override
   else:
      deny/escalate.
9. Apply through controlled transition.
10. Monitor effect.
11. Expire/revoke as defined.
12. Perform post-review if required.
```

------------------------------------------------------------------------

## 17.69 Reference Break-Glass Algorithm

```text
INPUT:
  emergency request
  actor
  emergency condition
  requested operation/resource

1. Validate actor identity.
2. Validate emergency trigger.
3. Validate Break-Glass eligibility.
4. Minimize requested Authority.
5. Apply time/purpose/resource constraints.
6. Record reason and residual risk.
7. Issue temporary emergency Authority.
8. Execute through governed Effect Boundary.
9. Capture Evidence + Trace.
10. Revoke/expire Authority.
11. Reconcile State.
12. Perform mandatory post-event review.
```

------------------------------------------------------------------------

## 17.70 Human Governance Profile

Deployment SHOULD define `Human Governance Profile`:

```text
profile_id
version
governance_root
goal_owners
authority_issuers
policy_owners
risk_owners
risk_acceptance_roles
approval_rules
approval_thresholds
quorum_rules
override_rules
non_overridable_controls
break_glass_rules
separation_of_duties
continuity_rules
trace_requirements
review_requirements
```

High-Assurance deployment MUST memiliki equivalent explicit
configuration.

------------------------------------------------------------------------

## 17.71 Human Governance Conformance Requirements

### Core

**AOF-HG-002 (canonical cross-reference)** — See the primary normative definition above.
Intent, Goal success criteria, atau mandatory constraints.

**AOF-HG-005 (canonical cross-reference)** — See the primary normative definition above.
unlimited solely because actor is Human.

### Governed

**AOF-HG-011** --- Consequential Human approval SHOULD bind identity,
subject, scope, version/freshness, dan timestamp.

**AOF-HG-012** --- Material change setelah approval SHOULD trigger
reapproval sesuai applicable profile.

**AOF-HG-013** --- Override Authority SHOULD be explicit dan distinct
dari ordinary approval where applicable.

**AOF-HG-014** --- Break-Glass Authority SHOULD be narrow,
purpose-limited, time-limited, dan revocable.

**AOF-HG-015** --- Human governance decisions SHOULD update
authoritative State melalui controlled transition.

**AOF-HG-016** --- Consequential Human governance events SHOULD be
traceable.

**AOF-HG-017** --- Governance conflict SHOULD memiliki deterministic
resolution/escalation rule.

**AOF-HG-018** --- Risk-proportional governance SHOULD avoid unnecessary
approval gates.

### Assured / High-Assurance

**AOF-HG-019** --- High-Assurance profile MUST define Human Governance
Profile atau equivalent.

**AOF-HG-020** --- High-Assurance approval/override MUST satisfy
applicable identity assurance dan separation-of-duties requirements.

**AOF-HG-021** --- High-Assurance Break-Glass MUST require post-event
review.

**AOF-HG-022** --- High-Assurance deployment MUST define continuity for
unavailable critical Human governance roles.

**AOF-HG-023** --- High-Assurance override MUST record affected control,
rationale, residual risk, Authority basis, dan review requirement.

**AOF-HG-024** --- High-Assurance governance changes MUST be versioned
dan traceable.

------------------------------------------------------------------------

## 17.72 Human Governance Invariants

### HG-INV-01 --- Governance Root

\[ AgentAutonomy\subset eq
Human/OrganizationalGovernanceEnvelope \]

### HG-INV-02 --- Human Non-Omnipotence

\[ HumanPresence\not\Rightarrow UnlimitedAuthority\]

### HG-INV-03 --- Intent Integrity

\[ AgentOptimization\not\Rightarrow IntentMutation\]

### HG-INV-04 --- Delegation Bound

\[ DelegatedOperationalAuthority \subset eq
OrganizationalGovernanceAuthority \]

### HG-INV-05 --- Accountability Persistence

\[
DelegatedExecution\not\Rightarrow AccountabilityErasure
\]

### HG-INV-06 --- Approval Separation

\[ Approval\neq AuthorityGrant\]

### HG-INV-07 --- Approval Freshness

\[ MaterialSubjectChange\Rightarrow ReevaluateApproval\]

### HG-INV-08 --- Override Governance

\[ Override\neq ControlBypass\]

### HG-INV-09 --- Break-Glass Auditability

\[ BreakGlass\not\Rightarrow NoAudit\]

### HG-INV-10 --- No Fabricated Approval

\[ HumanUnavailable\not\Rightarrow Approved\]

### HG-INV-11 --- Risk Acceptance Separation

\[ RiskAssessment\neq RiskAcceptance\]

### HG-INV-12 --- Automation Accountability

\[ Automation\not\Rightarrow AccountabilityErasure\]

### HG-INV-13 --- Human Decision Fallibility

\[ HumanDecision\neq GuaranteedCorrectDecision\]

### HG-INV-14 --- Policy Integrity

\[ HumanRequest\neq PolicyMutation\]

------------------------------------------------------------------------

## 17.73 Cross-Domain Human Governance Matrix

  ---------------------------------------------------------------------
  Human Governance Concern           Primary AOF Domains
  ---------------------------------- ----------------------------------
  Intent/Goal ownership              Conceptual Foundation, Goal, Human
                                     Governance

  Operational delegation             Authority, Agent, Human Governance

  Approval                           Authority, Risk, State, Human
                                     Governance

  Risk acceptance                    Risk, Human Governance

  Override                           Authority, Policy, Security, Human
                                     Governance

  Break-Glass                        Authority, Risk, Failure &
                                     Recovery, Security

  Human identity                     Security, Trace, Human Governance

  Accountability                     Trace, Evidence, Human Governance

  Separation of duties               Verification, Security, Human
                                     Governance

  Governance continuity              Failure & Recovery, Human
                                     Governance

  Human-as-Agent                     Agent Model, Human Governance

  Conformance                        Conformance, Human Governance
  ---------------------------------------------------------------------

------------------------------------------------------------------------

## 17.74 Reference Conformance Tests

### CT-HG-001 --- Human Without Authority

Given Human actor has technical access but no applicable Authority:

Expected:

\[ ExecuteAllowed=false \]

untuk governed consequential Action.

### CT-HG-002 --- Stale Approval

Given approved plan changes materially:

Expected: old approval MUST NOT automatically satisfy new approval gate.

### CT-HG-003 --- Approval Scope

Approval untuk Resource A MUST NOT authorize Resource B.

### CT-HG-004 --- Human Unavailability

Required approver unavailable:

Expected: `Pending`, authorized alternate, escalation, abort, atau valid
Break-Glass; never implicit approval.

### CT-HG-005 --- Override Non-Overridable Control

Attempt override terhadap `NonOverridable` control:

Expected: deny.

### CT-HG-006 --- Break-Glass Expiry

Expired emergency Authority:

Expected: new execution blocked.

### CT-HG-007 --- Delegation Accountability

Delegated AI Action:

Expected: delegation provenance dan accountable governance chain
reconstructable.

### CT-HG-008 --- Risk Acceptance Authority

Actor without risk-acceptance Authority attempts to accept Critical
residual risk:

Expected: deny/escalate.

------------------------------------------------------------------------

## 17.75 Freeze Candidate Criteria

Human Governance MAY dinyatakan `Freeze Candidate` jika:

1.  Governance Root semantics stabil;
2.  Human Intent/Goal ownership stabil;
3.  delegated operational Authority boundary stabil;
4.  Human-as-Agent semantics stabil;
5.  approval lifecycle/scope/freshness stabil;
6.  Approval vs Authority separation stabil;
7.  risk acceptance semantics stabil;
8.  Override boundaries stabil;
9.  Break-Glass protocol stabil;
10. accountability persistence stabil;
11. Human unavailability/conflict semantics stabil;
12. Human Governance Profile stabil;
13. requirements/invariants memiliki Conformance hooks;
14. no contradiction dengan Authority, Policy, Risk, Security,
    State/Trace, dan Failure/Recovery;
15. final cross-document review confirms v0.1 Human-Directed principle
    telah direkonsiliasi secara explicit dengan bounded operational
    autonomy.

------------------------------------------------------------------------

## 17.76 Formalization Result

Human Governance v1.0 RC-Human-Governance diringkas sebagai:

\[ HumanGovernance= Intent + GovernanceRoot + Delegation + Approval +
RiskAcceptance + Override + BreakGlass + Accountability \]

dengan:

\[ \boxed{ Human/Organization=GovernanceRoot } \]

\[ \boxed{ Agent=BoundedOperationalActor } \]

\[
\boxed{ AgentAutonomy\subset eq Human/OrganizationalGovernanceEnvelope }
\]

\[ \boxed{ Approval\neq AuthorityGrant } \]

\[ \boxed{ Override\neq ControlBypass } \]

\[
\boxed{ DelegatedExecution\not\Rightarrow AccountabilityErasure }
\]

AOF v1.x dengan demikian mempertahankan `Human-Directed` governance
tanpa mensyaratkan Human micromanagement terhadap setiap operational
Action. \# 18. Failure & Recovery

## 18.1 Purpose

`Failure & Recovery Model` mendefinisikan bagaimana AOF mendeteksi,
mengklasifikasikan, mengandung, merekam, memulihkan, mengeskalasi, dan
belajar dari failure tanpa mengorbankan Authority, Policy, Risk,
Verification, State, atau Trace semantics.

Canonical principles:

\[ Failure\neq PermissionToBypassControl\]

\[ Recovery\neq BlindRetry\]

\[ FailedAction\not\Rightarrow NoEffect\]

Failure adalah governed state, bukan exceptional condition yang berada
di luar framework.

------------------------------------------------------------------------

## 18.2 Failure Definition

Canonical failure object:

\[ f= \langle id, subject, type, severity, cause, state, effect,
evidence, risk, containment, recoverability, attempts, owner, timestamp,
provenance \rangle\]

dengan:

-   `subject`: Task, Action, Agent, Resource, Control, Verification,
    atau Session;
-   `type`: normalized failure category;
-   `severity`: consequence classification;
-   `cause`: known/suspected cause;
-   `state`: state saat failure terjadi;
-   `effect`: observed or possible external effect;
-   `evidence`: supporting failure evidence;
-   `risk`: updated risk;
-   `containment`: applied containment;
-   `recoverability`: recovery feasibility;
-   `attempts`: retry/recovery history;
-   `owner`: recovery responsibility;
-   `provenance`: failure record origin.

**AOF-FR-001** --- Material failure MUST direpresentasikan sebagai
explicit governed condition dan MUST NOT silently normalized menjadi
success.

------------------------------------------------------------------------

## 18.3 Failure Taxonomy

AOF reference taxonomy mempertahankan v0.1 failure families dan
menggeneralisasikannya:

-   `F1 Hallucination`;
-   `F2 Wrong Assumption`;
-   `F3 Context Failure`;
-   `F4 Tool Failure`;
-   `F5 Policy Failure`;
-   `F6 Authority Failure`;
-   `F7 Verification Failure`;
-   `F8 State Failure`;
-   `F9 Coordination Failure`;
-   `F10 Execution Failure`;
-   `F11 Security Failure`;
-   `F12 Outcome Failure`.

Domain profiles MAY menambahkan subtypes.

Taxonomy classification tidak menggantikan root-cause analysis.

------------------------------------------------------------------------

## 18.4 Failure Severity

Reference severity MAY menggunakan:

`Low`, `Moderate`, `High`, `Critical`.

Severity SHOULD mempertimbangkan:

-   actual effect;
-   potential effect;
-   blast radius;
-   reversibility;
-   data sensitivity;
-   control failure;
-   external exposure;
-   regulatory/safety impact.

Failure severity dan risk classification RELATED tetapi tidak identical.

------------------------------------------------------------------------

## 18.5 Failure Detection

Failure MAY dideteksi oleh:

-   Agent;
-   deterministic tool;
-   verifier;
-   Human;
-   State Validator;
-   Policy Evaluator;
-   Authority Evaluator;
-   Risk Gate;
-   Trace Recorder;
-   monitoring/observability;
-   external service.

Detection SHOULD menghasilkan evidence dan correlation ke affected
task/action/resource.

------------------------------------------------------------------------

## 18.6 Failure State

Failure state MUST distinguish at least:

-   known failure;
-   suspected failure;
-   partial failure;
-   unresolved failure;
-   recovered failure;
-   terminal failure.

Implementation MAY menggunakan more detailed lifecycle.

Unknown material outcome SHOULD NOT diperlakukan sebagai success.

------------------------------------------------------------------------

## 18.7 Failure Containment

Containment bertujuan membatasi further harm.

Possible controls:

-   stop new execution;
-   isolate resource;
-   revoke/suspend authority;
-   disable tool;
-   freeze task;
-   reduce context disclosure;
-   block downstream action;
-   switch to read-only;
-   quarantine artifact;
-   escalate to Human.

\[ FailureDetected\Rightarrow EvaluateContainment\]

High/Critical failure SHOULD evaluate containment before retry.

------------------------------------------------------------------------

## 18.8 Recovery Definition

Recovery adalah governed process untuk membawa system dari
failed/degraded state ke safe known state atau explicitly accepted
degraded state.

\[ Recovery: S\_{failed}\rightarrow S\_{safe/known} \]

Recovery success MUST berdasarkan observed state/evidence, bukan hanya
absence of error.

------------------------------------------------------------------------

## 18.9 Recovery Strategy

Reference strategies:

-   `Retry`;
-   `Replan`;
-   `Compensate`;
-   `Rollback`;
-   `Restore`;
-   `Failover`;
-   `Degrade`;
-   `Escalate`;
-   `Abort`;
-   `ManualRecovery`.

Strategy selection MUST mempertimbangkan current State, prior effects,
Authority, Policy, Risk, Evidence, dan Verification.

------------------------------------------------------------------------

## 18.10 Retry

Retry adalah reattempt terhadap operation atau semantically equivalent
operation.

\[ Retry\neq ReplayWithoutValidation\]

Retry MUST mempertimbangkan:

-   current state;
-   prior partial/full effects;
-   idempotency;
-   authority validity/consumption;
-   policy version;
-   risk;
-   retry budget;
-   new evidence;
-   verification obligations.

**AOF-FR-002** --- Consequential retry MUST NOT blindly reuse stale
permit atau stale state.

------------------------------------------------------------------------

## 18.11 Retry Eligibility

Reference:

\[ RetryEligible= Recoverable \land StateKnown
\land AuthorityValid\land PolicyValid
\land RiskAcceptable\land BudgetAvailable\]

Verification MAY juga required.

Unknown material effect SHOULD block automatic retry sampai
reconciliation cukup.

------------------------------------------------------------------------

## 18.12 Retry Budget

Retry MUST bounded untuk consequential operation.

\[ RetryCount\leq RetryBudget\]

Budget MAY bergantung pada:

-   failure type;
-   risk;
-   operation;
-   resource;
-   session;
-   cost;
-   time.

Exhaustion SHOULD menghasilkan `Replan`, `Escalate`, `Fail`, atau
`Abort`.

------------------------------------------------------------------------

## 18.13 Backoff and Rate Control

Retry MAY menggunakan backoff/rate control untuk transient failure.

AOF tidak menentukan algorithm tertentu.

Retry timing MUST tetap menghormati authority expiry, task deadlines,
policy validity, dan state freshness.

------------------------------------------------------------------------

## 18.14 Replan

Replan mengubah execution plan karena original plan tidak lagi
valid/optimal/safe.

\[ Replan\Rightarrow Reevaluate( Authority, Policy, Risk, State,
Verification ) \]

untuk materially affected dimensions.

Replan MUST preserve original goal dan inherited constraints kecuali
authorized governance decision mengubahnya.

------------------------------------------------------------------------

## 18.15 Recovery Plan

High-risk recovery SHOULD memiliki explicit Recovery Plan:

```text
failure_id
affected_resources
actual_state
desired_safe_state
strategy
required_authority
required_controls
steps
verification
rollback/compensation
owner
termination_condition
```

------------------------------------------------------------------------

## 18.16 Compensation

Compensation adalah action yang mengurangi/membalik business effect
ketika transactional rollback tidak tersedia.

\[ Compensation\neq ExactRollback\]

Compensation merupakan consequential action dan MUST melalui normal
control evaluation.

------------------------------------------------------------------------

## 18.17 Rollback

Rollback mencoba mengembalikan prior known state.

Rollback MUST NOT diasumsikan possible atau complete.

\[ RollbackRequested\not\Rightarrow RollbackSucceeded\]

Rollback result SHOULD diverifikasi.

------------------------------------------------------------------------

## 18.18 Restore

Restore menggunakan known recovery source seperti backup, snapshot,
prior artifact, atau configuration.

Restore source SHOULD memiliki provenance/integrity yang sesuai risk.

Post-restore verification SHOULD memastikan actual state.

------------------------------------------------------------------------

## 18.19 Failover

Failover mengalihkan operation ke alternate component/resource.

Failover MAY mengubah:

-   resource;
-   trust boundary;
-   authority scope;
-   policy applicability;
-   risk;
-   verification requirements.

Material failover MUST memicu relevant reevaluation.

------------------------------------------------------------------------

## 18.20 Degraded Operation

System MAY masuk controlled degraded mode.

Degraded mode MUST explicit dan SHOULD menentukan:

-   unavailable capabilities;
-   allowed operations;
-   restricted authority;
-   risk;
-   duration;
-   exit criteria;
-   monitoring.

Degraded mode MUST NOT menjadi implicit bypass.

------------------------------------------------------------------------

## 18.21 Partial Effect

Canonical rule:

\[ PartialEffect\not\Rightarrow FailureWithoutEffect\]

Jika action gagal setelah sebagian effect:

1.  stop uncontrolled continuation;
2.  capture evidence;
3.  determine actual state;
4.  mark partial effect;
5.  reassess risk;
6.  choose compensation/rollback/replan/escalation;
7.  verify recovery.

**AOF-FR-003** --- Partial effect MUST direconciled sebelum automatic
retry jika duplicate/additional effect dapat material.

------------------------------------------------------------------------

## 18.22 Unknown Effect

Jika effect tidak dapat ditentukan:

\[ Effect=Unknown \Rightarrow NoBlindRetry \]

System SHOULD observe/reconcile target state atau escalate.

Unknown effect merupakan risk signal.

------------------------------------------------------------------------

## 18.23 Failure and State

Failure MUST menghasilkan controlled state transition jika material.

Possible task transitions:

```text
Executing
   |
   +--> Waiting
   +--> Failed
   +--> Escalated
   +--> Planning/Replan
   +--> Verifying
```

Exact transition mengikuti lifecycle.

------------------------------------------------------------------------

## 18.24 Failure and Trace

Failure path MUST traceable.

Trace SHOULD mencakup:

-   failure event;
-   detection source;
-   affected action/resource;
-   state before/after;
-   evidence;
-   containment;
-   retry/recovery decisions;
-   verification;
-   final outcome.

Failure history MUST NOT silently erased setelah recovery.

------------------------------------------------------------------------

## 18.25 Failure and Evidence

Failure evidence MAY mencakup:

-   errors;
-   tool responses;
-   logs;
-   state observations;
-   verification results;
-   resource snapshots;
-   external alerts.

Recovery decision SHOULD menggunakan sufficient evidence untuk
consequence level.

------------------------------------------------------------------------

## 18.26 Failure and Risk

Failure MAY meningkatkan risk:

\[ Failure\Rightarrow ReassessRisk\]

jika failure material terhadap likelihood, impact, exposure, control
effectiveness, atau uncertainty.

Repeated failure SHOULD menjadi reassessment trigger.

------------------------------------------------------------------------

## 18.27 Failure and Authority

Failure tidak memperluas authority.

\[ Failure\not\Rightarrow EmergencyAuthority\]

Recovery action MUST memiliki valid Authority.

Emergency/break-glass authority hanya valid jika explicit governance
mechanism mengizinkannya.

------------------------------------------------------------------------

## 18.28 Failure and Policy

Policy MAY menentukan:

-   retryability;
-   retry limit;
-   containment;
-   recovery strategy;
-   escalation threshold;
-   Human approval;
-   termination;
-   incident handling.

Policy failure itself MUST fail-controlled.

------------------------------------------------------------------------

## 18.29 Failure and Verification

Recovery MUST diverifikasi jika recovery effect consequential.

\[ RecoveryClaim\neq RecoveryVerified\]

High-risk recovery SHOULD menggunakan independent verification sesuai
applicable profile.

------------------------------------------------------------------------

## 18.30 Verification Failure

Verification `Rejected` atau repeated `Inconclusive` MAY menyebabkan:

-   collect evidence;
-   retry verification;
-   replan;
-   rollback;
-   escalate;
-   reject outcome.

Verification failure MUST NOT diubah menjadi successful completion tanpa
governed override/alternative criteria path.

------------------------------------------------------------------------

## 18.31 Control Component Failure

Failure pada Safety Kernel component merupakan governance-critical
failure.

Examples:

-   Authority Evaluator unavailable;
-   Policy Evaluator unavailable;
-   State Validator unavailable;
-   Risk Gate unavailable;
-   Verification Gate unavailable;
-   Trace Recorder unavailable.

Mandatory control failure MUST default ke controlled non-execution
(`Pending`, `Deny`, `Escalate`) kecuali profile explicitly defines safe
degraded behavior.

**AOF-FR-004** --- Mandatory Safety Kernel failure MUST NOT silently
fail-open.

------------------------------------------------------------------------

## 18.32 Orchestrator Failure

Orchestrator restart/crash SHOULD preserve enough durable state untuk
menentukan:

-   in-flight tasks;
-   issued decisions;
-   effects possibly started;
-   authority usage;
-   retry state;
-   pending verification;
-   trace gaps.

Recovery MUST avoid duplicate consequential effect.

------------------------------------------------------------------------

## 18.33 Agent Failure

Agent failure MAY berupa:

-   unavailable;
-   timeout;
-   malformed output;
-   context loss;
-   unsafe proposal;
-   repeated low-quality output.

Agent replacement MUST NOT inherit Authority implicitly dan SHOULD
reevaluate assignment/risk/context.

------------------------------------------------------------------------

## 18.34 Tool Failure

Tool failure SHOULD distinguish:

-   request rejected;
-   timeout;
-   connection failure;
-   execution failure;
-   partial execution;
-   unknown result;
-   malformed response.

Timeout MUST NOT automatically mean no effect.

------------------------------------------------------------------------

## 18.35 External Service Failure

External service failure MAY require:

-   failover;
-   wait;
-   cached/read-only behavior;
-   escalation;
-   abort.

Cached fallback MUST respect freshness and policy.

------------------------------------------------------------------------

## 18.36 Human Unavailability

Jika required Human approval/review unavailable:

\[ RequiredHumanUnavailable\Rightarrow Pending/Escalate \]

bukan implicit approval.

Profile MAY menyediakan alternate authorized approver path.

------------------------------------------------------------------------

## 18.37 Escalation

Escalation transfers unresolved decision/recovery need ke authorized
higher/different control actor.

Escalation package SHOULD mencakup:

```text
task/session
failure
current state
actual/possible effects
evidence
risk
authority/policy status
attempt history
recommended options
decision required
```

------------------------------------------------------------------------

## 18.38 Escalation Is Not Failure Resolution

\[ Escalated\neq Resolved\]

Escalated task tetap unresolved sampai valid decision/action mengubah
state.

------------------------------------------------------------------------

## 18.39 Abort

`Abort` menghentikan further execution karena continuation tidak
acceptable.

Abort MUST:

-   stop new governed actions within scope;
-   preserve evidence/trace;
-   reconcile in-flight effects;
-   update state;
-   identify residual risk.

Abort tidak otomatis rollback prior effects.

------------------------------------------------------------------------

## 18.40 Cancellation

Cancellation berasal dari governance/user/system request untuk
menghentikan workflow.

\[ Cancel\neq Abort\neq Rollback\]

Cancellation SHOULD menggunakan same safety principles untuk in-flight
effects dan reconciliation.

------------------------------------------------------------------------

## 18.41 Termination

Terminal outcome MUST explicit.

Reference terminal results:

-   `Completed`;
-   `Failed`;
-   `Rejected`;
-   `Aborted`;
-   `Cancelled`.

Successful terminal state MUST memenuhi completion verification.

Failure terminal state MUST preserve residual effect/risk information
jika applicable.

------------------------------------------------------------------------

## 18.42 Recovery Verification

Reference:

\[ RecoverySuccessful= SafeStateObserved
\land RequiredVerificationSatisfied\]

Absence of new error tidak cukup.

Recovery verification SHOULD bind ke actual recovered resource/state.

------------------------------------------------------------------------

## 18.43 Recovery Idempotency

Recovery action SHOULD idempotent jika repeated execution possible.

Compensation/rollback operations yang non-idempotent MUST memiliki
stronger state reconciliation.

------------------------------------------------------------------------

## 18.44 Recovery Authority

Recovery MAY memerlukan authority berbeda dari original action.

\[
Authority\_{execute}\not\Rightarrow Authority\_{rollback}
\]

\[
Authority\_{deploy}\not\Rightarrow Authority\_{restore}
\]

Recovery Plan MUST resolve required authority explicitly untuk
consequential recovery.

------------------------------------------------------------------------

## 18.45 Recovery Risk

Recovery action sendiri memiliki risk.

\[ Risk(recovery)\neq Risk(original) \]

System SHOULD compare:

-   risk of continuing;
-   risk of recovery;
-   risk of doing nothing.

Decision tetap tunduk pada policy/authority.

------------------------------------------------------------------------

## 18.46 Recovery Evidence

Recovery evidence SHOULD mencakup:

-   actual pre-recovery state;
-   recovery action;
-   tool/result;
-   observed post-state;
-   verification result;
-   remaining limitations;
-   residual risk.

------------------------------------------------------------------------

## 18.47 Recovery Time and Deadline

Recovery MAY memiliki deadline/timeout.

Exceeded recovery deadline SHOULD memicu escalation atau terminal
handling sesuai profile.

Time pressure MUST NOT create implicit authority or bypass mandatory
controls.

------------------------------------------------------------------------

## 18.48 Failure Budget

`Failure Budget` membatasi tolerated failure/retry behavior.

Reference:

\[ FailureBudget= \langle scope, maxAttempts, maxDuration,
maxCost, maxRiskIncrease \rangle\]

Exhaustion MUST menghasilkan governed decision.

------------------------------------------------------------------------

## 18.49 Circuit Breaker

Implementation MAY menggunakan circuit breaker untuk repeated failure.

Reference states:

`Closed`, `Open`, `HalfOpen`.

Circuit breaker MAY mengurangi cascading failure tetapi tidak
menggantikan Policy/Risk evaluation.

------------------------------------------------------------------------

## 18.50 Recovery Checkpoint

Long-running workflows MAY menggunakan checkpoints.

Checkpoint SHOULD bind:

-   state version;
-   completed effects;
-   evidence;
-   authority/policy references;
-   pending work.

Resume dari checkpoint MUST revalidate time-sensitive controls.

------------------------------------------------------------------------

## 18.51 Saga-Style Recovery

Multi-step distributed workflows MAY menggunakan compensating
transaction/saga pattern.

AOF tidak mewajibkan saga technology.

Jika digunakan, each compensating action tetap governed Action.

------------------------------------------------------------------------

## 18.52 Irrecoverable Failure

Failure MAY diklasifikasikan irrecoverable jika safe automated recovery
tidak tersedia.

\[ Irrecoverable\Rightarrow Escalate/Abort/Fail \]

sesuai policy.

System MUST NOT fabricate recovery success.

------------------------------------------------------------------------

## 18.53 Recovery Conflict

Concurrent recovery attempts terhadap same resource dapat menambah harm.

Recovery SHOULD menggunakan state conflict controls, ownership/lease,
serialization, atau equivalent mechanism jika material.

------------------------------------------------------------------------

## 18.54 Security Failure

Suspected security compromise SHOULD dapat memicu stronger containment:

-   suspend credentials/authority;
-   isolate resource;
-   preserve forensic evidence;
-   restrict mutation;
-   escalate.

Detailed threat semantics berada di Section 19.

------------------------------------------------------------------------

## 18.55 Failure Learning

Failure record MAY menjadi input learning loop.

Learning MUST distinguish:

-   observed failure;
-   inferred cause;
-   confirmed cause;
-   proposed improvement;
-   validated improvement.

\[
Failure\rightarrow Evidence\rightarrow Analysis\rightarrow ImprovementProposal
\]

Improvement proposal tidak otomatis mengubah Policy atau Authority.

------------------------------------------------------------------------

## 18.56 Post-Incident Review

High/Critical failure SHOULD menghasilkan review sesuai profile.

Review MAY mencakup:

-   timeline;
-   root cause;
-   control effectiveness;
-   recovery effectiveness;
-   trace/evidence gaps;
-   policy changes;
-   test additions;
-   risk profile updates.

------------------------------------------------------------------------

## 18.57 Failure Recovery Profile

Deployment/profile SHOULD mendefinisikan `Failure Recovery Profile`
untuk consequential operations.

Reference:

```text
profile_id
failure_classes
severity_mapping
retry_policy
retry_budget
containment
replan_rules
recovery_strategies
escalation_thresholds
verification
termination
trace_requirements
```

------------------------------------------------------------------------

## 18.58 Failure Modes of Recovery

### FR-F01 --- Blind Retry

Retry tanpa state/effect reconciliation.

### FR-F02 --- Retry Storm

Repeated retry memperbesar failure/blast radius.

### FR-F03 --- Duplicate Effect

Retry mengulang consequential effect.

### FR-F04 --- Stale Permit

Recovery/retry memakai old authorization/control decision.

### FR-F05 --- Failed Compensation

Compensation tidak menghasilkan intended state.

### FR-F06 --- Failed Rollback

Rollback incomplete/failed.

### FR-F07 --- Recovery Drift

Recovered state berbeda dari expected safe state.

### FR-F08 --- Hidden Partial Effect

Partial effect tidak direpresentasikan.

### FR-F09 --- Escalation Loss

Critical context/evidence hilang saat escalation.

### FR-F10 --- Recovery Authority Failure

Recovery actor tidak memiliki required authority.

### FR-F11 --- Control Fail-Open

Safety control failure menyebabkan execution tanpa valid gate.

### FR-F12 --- False Recovery

System menandai recovered tanpa sufficient verification.

------------------------------------------------------------------------

## 18.59 Reference Failure Handling Algorithm

```text
INPUT:
  failure signal
  current state
  action/effect evidence
  applicable Failure Recovery Profile

1. Identify affected subject/resource.
2. Classify failure type/severity.
3. Determine known/unknown/partial effect.
4. Capture failure evidence.
5. Reconcile authoritative state.
6. Reassess risk if material.
7. Evaluate containment.
8. Determine recoverability.
9. Evaluate retry/replan/recovery eligibility.
10. Revalidate Authority/Policy/State/Risk.
11. Execute selected governed recovery action.
12. Verify recovery result.
13. Update state.
14. Record complete trace.
15. Continue, escalate, abort, or terminate.
```

------------------------------------------------------------------------

## 18.60 Reference Retry Algorithm

```text
1. Check retry budget.
2. Determine prior actual effect.
3. Reconcile state.
4. Validate idempotency/deduplication.
5. Revalidate Authority.
6. Re-evaluate Policy.
7. Reassess Risk when triggered.
8. Re-evaluate Verification obligations.
9. Execute retry.
10. Capture new evidence.
11. Verify result.
12. Update retry history and Trace.
```

------------------------------------------------------------------------

## 18.61 Failure & Recovery Conformance Requirements

### Core

**AOF-FR-002 (canonical cross-reference)** — See the primary normative definition above.
permit/state.

**AOF-FR-004 (canonical cross-reference)** — See the primary normative definition above.
fail-open.

**AOF-FR-005** --- Unknown material effect MUST NOT dianggap no-effect.

**AOF-FR-006** --- Recovery action MUST memiliki valid
Authority/Policy/State/Risk controls.

**AOF-FR-007** --- Recovery success MUST berdasarkan observed/verified
recovery condition.

**AOF-FR-008** --- Failure/recovery history MUST traceable.

### Governed

**AOF-FR-009** --- Retry MUST bounded oleh retry/failure budget.

**AOF-FR-010** --- Material replan MUST reevaluate affected governance
controls.

**AOF-FR-011** --- Compensation/Rollback MUST diperlakukan sebagai
consequential Action.

**AOF-FR-012** --- Escalation MUST preserve sufficient failure
context/evidence.

**AOF-FR-013** --- Abort/Cancel MUST reconcile material in-flight
effects.

**AOF-FR-014** --- Agent replacement after failure MUST NOT inherit
Authority implicitly.

**AOF-FR-015** --- Material failure SHOULD trigger Risk reassessment.

**AOF-FR-016** --- Required recovery verification failure MUST prevent
false successful recovery.

### Assured / High-Assurance

**AOF-FR-017** --- High-risk recovery MUST menggunakan explicit Recovery
Plan atau equivalent controlled semantics.

**AOF-FR-018** --- High-assurance profile MUST menentukan retry,
partial-effect, containment, recovery, escalation, dan terminal
behavior.

**AOF-FR-019** --- High-assurance recovery MUST preserve sufficient
Evidence/Trace untuk independent reconstruction.

**AOF-FR-020** --- High/Critical control subsystem failure MUST
menghasilkan conservative non-execution atau explicitly defined safe
degraded mode.

------------------------------------------------------------------------

## 18.62 Failure & Recovery Invariants

### FR-INV-01 --- Controlled Failure

\[ Failure\not\Rightarrow ControlBypass\]

### FR-INV-02 --- No Blind Retry

\[ Retry\Rightarrow CurrentStateValidation\]

### FR-INV-03 --- Partial Effect Honesty

\[ PartialEffect\not\Rightarrow NoEffect\]

### FR-INV-04 --- Recovery Authority

\[ RecoveryAction\Rightarrow ValidAuthority\]

### FR-INV-05 --- Recovery Verification

\[ RecoverySuccess\Rightarrow RequiredVerificationSatisfied\]

### FR-INV-06 --- Bounded Retry

\[ RetryCount\leq RetryBudget\]

### FR-INV-07 --- Safety Kernel Fail-Controlled

\[ MandatoryControlFailure\Rightarrow\neg ImplicitPermit
\]

### FR-INV-08 --- Escalation Non-Resolution

\[ Escalated\not\Rightarrow Resolved\]

### FR-INV-09 --- Historical Preservation

\[ Recovered\Rightarrow PreserveMaterialFailureHistory\]

### FR-INV-10 --- Goal Integrity Under Replan

\[ Replan\Rightarrow PreserveGoalAndConstraints\]

kecuali valid governance change.

------------------------------------------------------------------------

## 18.63 Cross-Domain Integration

Failure & Recovery mengikat seluruh control loop:

```text
Observe
   |
Reason
   |
Propose
   |
Govern
   |
Act
   |
Verify
   |
Update
   |
Failure?
   +---- No ----> Continue/Complete
   |
   Yes
   |
Contain
   |
Reconcile
   |
Reassess Risk
   |
Retry / Replan / Recover / Escalate / Abort
   |
Verify Recovery
   |
Update State + Trace
```

------------------------------------------------------------------------

## 18.64 Failure & Recovery Freeze Candidate Criteria

Area ini MAY dinyatakan `Freeze Candidate` jika:

1.  failure taxonomy stabil;
2.  partial/unknown effect semantics stabil;
3.  retry/replan semantics stabil;
4.  retry/failure budget semantics stabil;
5.  compensation/rollback/restore/failover semantics stabil;
6.  Safety Kernel failure behavior stabil;
7.  recovery verification semantics stabil;
8.  escalation/abort/cancellation/termination semantics stabil;
9.  State & Trace integration stabil;
10. Security failure handling compatible dengan Section 19;
11. conformance requirements dapat dipetakan ke executable tests.

------------------------------------------------------------------------

## 18.65 Failure & Recovery Formalization Result

Failure & Recovery v1.0 RC-Failure-Recovery diringkas sebagai:

\[ FailureHandling= Detect + Contain + Reconcile + Reassess + Recover +
Verify + Trace \]

dengan:

\[ \boxed{ Failure\ Does\ Not\ Suspend\ Governance } \]

\[ \boxed{ Retry\neq Blind\ Replay } \]

\[ \boxed{ Partial\ Effect\neq No\ Effect } \]

\[ \boxed{ Recovery\ Success\ Requires\ Verification } \]

dan:

\[ \boxed{ Mandatory\ Control\ Failure\neq Implicit\ Permit } \]
# 19. Security Requirements

## 19.1 Purpose

`Security Model` mendefinisikan bagaimana AOF melindungi governance
integrity, trust boundaries, Authority, Policy, Context, State,
Evidence, Trace, execution paths, dan external effects dari unauthorized
influence, misuse, compromise, dan control bypass.

Security pada AOF bukan hanya property dari generated artifact. Security
juga merupakan property dari orchestration system itu sendiri.

Canonical objective:

\[ SecureOrchestration= GovernanceIntegrity + LeastAuthority +
TrustedControl + BoundedContext + EffectControl + Assurance +
Traceability \]

Security controls MUST mempertahankan separation:

\[ UntrustedInput\neq ControlInstruction\]

\[ TechnicalAccess\neq Authority\]

\[ AgentOutput\neq SystemDecision\]

------------------------------------------------------------------------

## 19.2 Security Objectives

AOF Security SHOULD melindungi:

-   confidentiality;
-   integrity;
-   availability;
-   authenticity;
-   authorization;
-   accountability;
-   governance integrity;
-   control-plane integrity;
-   evidence integrity;
-   trace integrity;
-   execution integrity;
-   privacy.

Security objective MAY diperketat oleh domain profile.

------------------------------------------------------------------------

## 19.3 Security Trust Model

AOF menggunakan explicit trust boundaries.

Default:

\[ AgentOutput=UntrustedProposal \]

External content, tool output, retrieved documents, user-controlled
data, Agent messages, dan external service responses MUST NOT memperoleh
control authority hanya karena masuk ke context.

\[ Content\not\Rightarrow Authority\]

------------------------------------------------------------------------

## 19.4 Security Assets

Protected assets MAY mencakup:

-   governance rules;
-   Authority grants;
-   Policy;
-   Risk Profiles;
-   State;
-   Trace;
-   Evidence;
-   credentials/secrets;
-   Context;
-   prompts/system instructions;
-   tools/resources;
-   artifacts;
-   source code;
-   production systems;
-   Human approval channels;
-   verification mechanisms.

Security analysis SHOULD mengidentifikasi assets yang material untuk
deployment.

------------------------------------------------------------------------

## 19.5 Threat Model

AOF reference threat classes:

-   `T-AUTH` --- Authority abuse/escalation;
-   `T-POL` --- Policy manipulation/bypass;
-   `T-CTX` --- Context injection/poisoning/disclosure;
-   `T-AGT` --- Agent compromise/misbehavior;
-   `T-TOOL` --- Tool/resource misuse;
-   `T-STATE` --- State corruption/race/replay;
-   `T-EVD` --- Evidence manipulation;
-   `T-VER` --- Verification compromise;
-   `T-TRC` --- Trace tampering/evasion;
-   `T-EXEC` --- Effect-boundary bypass;
-   `T-SUP` --- Supply-chain/external-service compromise;
-   `T-HUM` --- Human governance channel compromise;
-   `T-PRV` --- Privacy/data exposure;
-   `T-AVL` --- Availability/resource exhaustion.

Deployment SHOULD instantiate threats yang relevant.

------------------------------------------------------------------------

## 19.6 Threat--Control Mapping

Security profile SHOULD mendokumentasikan:

\[
Threat\rightarrow Control\rightarrow Requirement\rightarrow Evidence
\]

Untuk High-Assurance:

\[
Threat\rightarrow Control\rightarrow Test\rightarrow Evidence
\]

SHOULD dapat direkonstruksi.

**AOF-SEC-001** --- Security-critical deployment MUST memiliki explicit
threat model atau equivalent documented threat analysis.

------------------------------------------------------------------------

## 19.7 Trust Boundary Identification

Trust boundary SHOULD didefinisikan antara:

-   Human ↔ system;
-   Agent ↔ Control Plane;
-   Agent ↔ Agent;
-   Agent ↔ Tool;
-   Control Plane ↔ Effect Plane;
-   internal ↔ external service;
-   trusted ↔ untrusted Context;
-   Evidence source ↔ verifier;
-   orchestration system ↔ production environment.

Cross-boundary data/action MUST tunduk pada applicable controls.

------------------------------------------------------------------------

## 19.8 Context as Security Boundary

\[ C_a\subset eq C\]

Agent MUST menerima minimum necessary Context sesuai role/task.

Context projection SHOULD mengendalikan:

-   secrets;
-   sensitive data;
-   privileged instructions;
-   unrelated task data;
-   cross-tenant data;
-   internal governance metadata.

**AOF-SEC-002** --- Context access MUST mengikuti least-privilege dan
applicable disclosure controls.

------------------------------------------------------------------------

## 19.9 Instruction--Data Separation

Untrusted data MAY berisi text yang menyerupai instruction.

Canonical rule:

\[ ExternalContent\neq GovernanceInstruction\]

System SHOULD preserve distinction antara:

-   governance instruction;
-   task instruction;
-   retrieved content;
-   user data;
-   tool output;
-   external message.

Mandatory controls MUST NOT bergantung hanya pada model kemampuan
membedakan prompt injection.

------------------------------------------------------------------------

## 19.10 Prompt Injection

Prompt injection SHOULD diperlakukan sebagai untrusted influence attempt
terhadap Reasoning Plane.

Controls MAY mencakup:

-   context segmentation;
-   instruction provenance;
-   tool restrictions;
-   output validation;
-   policy enforcement;
-   content labeling;
-   least context;
-   independent verification.

Prompt injection MUST NOT dapat secara langsung grant Authority, mutate
Policy, atau bypass Safety Kernel.

------------------------------------------------------------------------

## 19.11 Indirect Prompt Injection

Retrieved documents, web content, repository files, emails, tickets,
logs, atau tool responses MAY membawa indirect instructions.

Such content MUST remain data unless valid governance channel explicitly
promotes it.

\[
RetrievedInstruction\not\Rightarrow AuthorizedInstruction
\]

------------------------------------------------------------------------

## 19.12 Agent Compromise Assumption

Security design SHOULD mengasumsikan bahwa individual Agent MAY:

-   hallucinate;
-   be manipulated;
-   misunderstand context;
-   produce unsafe proposal;
-   leak information;
-   attempt unauthorized tool use.

Safety MUST tidak bergantung pada perfect Agent behavior.

\[ CompromisedAgent\not\Rightarrow CompromisedGovernance
\]

merupakan target architectural property.

------------------------------------------------------------------------

## 19.13 Safety Kernel Protection

Safety Kernel:

\[ K= { AuthorityEvaluator, PolicyEvaluator, StateValidator, RiskGate,
VerificationGate, TraceRecorder } \]

MUST berada dalam trusted control boundary yang lebih kuat daripada
ordinary Agent execution.

Agent MUST NOT dapat directly bypass atau redefine mandatory Safety
Kernel semantics.

**AOF-SEC-003** --- Mandatory Safety Kernel controls MUST be
non-bypassable melalui ordinary Agent/tool path.

------------------------------------------------------------------------

## 19.14 Control Plane Integrity

Unauthorized mutation terhadap Control Plane configuration MUST dicegah
atau detectable.

Security-critical changes SHOULD mencakup:

-   authenticated actor;
-   valid Authority;
-   Policy evaluation;
-   change evidence;
-   trace;
-   rollback/recovery semantics.

------------------------------------------------------------------------

## 19.15 Authority Security

Authority security MUST mempertahankan:

-   positive authorization;
-   scope;
-   validity;
-   delegation conservation;
-   revocation;
-   provenance;
-   no self-elevation.

\[ Authority\_{delegatee}\subset eq Authority\_{delegator} \]

Threat examples:

-   privilege escalation;
-   confused deputy;
-   authority laundering;
-   stale grant reuse;
-   credential-to-authority confusion.

------------------------------------------------------------------------

## 19.16 Credential Is Not Authority

Credential possession memberikan technical capability, bukan governance
permission.

\[ CredentialPossession\not\Rightarrow AuthorizedUse\]

Credentials SHOULD scoped, protected, rotated/revoked sesuai applicable
security policy.

Agent SHOULD tidak menerima long-lived broad credentials jika narrower
mechanism tersedia.

------------------------------------------------------------------------

## 19.17 Confused Deputy Protection

Component dengan broad technical privilege MUST validate requesting
subject, intended operation, resource, dan applicable Authority.

Delegated request MUST NOT memperoleh privilege hanya karena
intermediary memiliki broader access.

------------------------------------------------------------------------

## 19.18 Policy Security

Policy source, activation, version, override, dan mutation SHOULD
dilindungi.

\[ UntrustedContent\not\Rightarrow PolicyMutation\]

Unauthorized policy change MUST prevented/detectable sesuai profile.

High-assurance profile SHOULD memiliki protected policy
distribution/version binding.

------------------------------------------------------------------------

## 19.19 Risk Control Security

Risk classification MUST NOT dapat diturunkan oleh unauthorized actor
untuk mengurangi control.

Risk override/acceptance MUST mengikuti valid governance authority.

Security-relevant uncertainty SHOULD bias ke conservative control, bukan
implicit allow.

------------------------------------------------------------------------

## 19.20 Evidence Security

Evidence security SHOULD mempertahankan:

-   provenance;
-   integrity;
-   confidentiality;
-   correct scope;
-   retention;
-   controlled transformation.

Threats:

-   fabricated evidence;
-   evidence substitution;
-   stale evidence;
-   provenance stripping;
-   false corroboration;
-   unauthorized disclosure.

------------------------------------------------------------------------

## 19.21 Verification Security

Verifier compromise dapat merusak Assurance Plane.

Controls SHOULD mencakup:

-   verifier eligibility;
-   independence;
-   evidence binding;
-   method integrity;
-   result binding;
-   separation of duties.

High-risk verification MUST NOT bergantung pada same compromised control
path jika independence profile melarangnya.

------------------------------------------------------------------------

## 19.22 Trace Security

Trace MUST protected dari:

-   deletion;
-   alteration;
-   forgery;
-   actor spoofing;
-   ordering manipulation;
-   unauthorized disclosure.

High-assurance trace SHOULD tamper-resistant atau tamper-evident.

Trace security MUST tetap mendukung privacy/minimization.

------------------------------------------------------------------------

## 19.23 State Security

State security SHOULD mempertahankan:

-   authorized mutation;
-   version integrity;
-   conflict control;
-   freshness;
-   replay protection;
-   recovery.

Unauthorized state mutation merupakan security failure.

------------------------------------------------------------------------

## 19.24 Execution Gateway

Consequential effect SHOULD melalui controlled `Execution Gateway` atau
semantically equivalent boundary.

Reference:

```text
Authorized Control Decision
        |
        v
Execution Gateway
        |
        +--> decision binding
        +--> state/freshness validation
        +--> resource resolution
        +--> operation validation
        |
        v
External Effect
```

**AOF-SEC-004** --- Consequential effect MUST NOT memiliki uncontrolled
bypass path around applicable governance evaluation.

------------------------------------------------------------------------

## 19.25 Decision Binding

Execution request SHOULD bind ke relevant:

-   decision ID;
-   actor;
-   action;
-   resource;
-   Authority;
-   Policy result;
-   state version;
-   risk result;
-   verification/approval;
-   validity window.

Binding MAY diwujudkan sebagai control token, signed permit, transaction
context, protected server-side reference, atau equivalent.

AOF tidak mewajibkan specific token technology.

------------------------------------------------------------------------

## 19.26 TOCTOU Security

\[ Permit\_{t_1}\not\Rightarrow Permit\_{t_2} \]

jika material security state berubah.

High-risk Effect Boundary SHOULD revalidate:

-   Authority;
-   Policy version;
-   target/resource identity;
-   state;
-   risk;
-   required verification/approval freshness.

------------------------------------------------------------------------

## 19.27 Replay Protection

Historical decision/permit MUST NOT reusable untuk unauthorized new
effect.

Controls MAY mencakup:

-   nonce;
-   expiry;
-   operation ID;
-   state version;
-   single-use token;
-   consumption record;
-   idempotency key.

------------------------------------------------------------------------

## 19.28 Resource Identity Security

Resource alias/identifier confusion dapat menyebabkan wrong-target
effect.

High-risk action SHOULD resolve canonical target identity sebelum
effect.

\[ RequestedResource\stackrel{?}{=}AuthorizedResource \]

------------------------------------------------------------------------

## 19.29 Tool Security

Tool exposure SHOULD mengikuti least functionality dan least authority.

Agent SHOULD hanya memperoleh tools yang required.

Tool invocation SHOULD validate:

-   actor;
-   operation;
-   target;
-   parameters;
-   authority;
-   policy;
-   risk;
-   state.

Tool description/prompt MUST NOT menjadi sole enforcement mechanism.

------------------------------------------------------------------------

## 19.30 Parameter Security

Valid operation terhadap valid resource masih dapat berbahaya jika
parameters keluar scope.

Authority/Policy SHOULD dapat membatasi parameter ranges, quantities,
paths, destinations, atau commands.

Input validation SHOULD terjadi sebelum consequential effect.

------------------------------------------------------------------------

## 19.31 Command and Code Execution

Generated code/commands SHOULD diperlakukan sebagai untrusted artifact
sampai applicable validation.

High-risk execution SHOULD menggunakan controls seperti:

-   sandbox;
-   allowlist;
-   static validation;
-   dry-run;
-   staged execution;
-   independent verification.

Generated content MUST NOT self-authorize execution.

------------------------------------------------------------------------

## 19.32 Sandbox and Isolation

Sandbox MAY digunakan untuk membatasi blast radius.

Sandbox SHOULD memiliki explicit boundaries untuk:

-   filesystem;
-   network;
-   credentials;
-   processes;
-   data;
-   resource consumption.

Sandbox escape atau boundary ambiguity merupakan security failure.

------------------------------------------------------------------------

## 19.33 Network Security

Network access SHOULD least-privilege.

Profile MAY membatasi:

-   destinations;
-   protocols;
-   ports;
-   egress;
-   ingress;
-   external APIs.

External network access dapat memperluas Context, disclosure,
supply-chain, dan execution risk.

------------------------------------------------------------------------

## 19.34 Secret Management

Secrets MUST NOT diperlakukan sebagai ordinary Context jika privileged
handling diperlukan.

Controls SHOULD mencakup:

-   least exposure;
-   short-lived credentials;
-   redaction;
-   non-persistence in prompts/logs;
-   rotation/revocation;
-   scoped injection at execution boundary.

Agent SHOULD tidak menerima secret plaintext jika tool-mediated
credential use dapat memenuhi task.

------------------------------------------------------------------------

## 19.35 Sensitive Data

Sensitive data handling SHOULD mengikuti:

-   classification;
-   minimization;
-   purpose limitation;
-   disclosure control;
-   retention;
-   redaction;
-   cross-boundary restrictions.

\[ ReadAuthority\neq DisclosureAuthority\]

------------------------------------------------------------------------

## 19.36 Cross-Tenant and Cross-Task Isolation

Multi-tenant/multi-task system MUST mencegah unauthorized context,
state, evidence, credential, atau trace leakage antar scopes.

Tenant/task identity SHOULD menjadi input policy/authority evaluation
jika relevant.

------------------------------------------------------------------------

## 19.37 Memory Security

Agent memory MAY mengandung sensitive/stale/adversarial information.

Memory MUST NOT menjadi authoritative governance source tanpa
validation.

Persistent memory SHOULD memiliki scope, retention, access control, dan
provenance sesuai risk.

------------------------------------------------------------------------

## 19.38 Supply-Chain Security

External models, tools, packages, plugins, services, artifacts, dan data
sources MAY menjadi supply-chain dependencies.

Security profile SHOULD mengidentifikasi critical dependencies dan
controls seperti:

-   provenance;
-   version pinning;
-   integrity validation;
-   allowlisting;
-   monitoring;
-   fallback;
-   isolation.

------------------------------------------------------------------------

## 19.39 Model and Service Substitution

Changing model/tool/service MAY mengubah capability, trust, data
handling, behavior, dan risk.

Material substitution SHOULD trigger applicable reassessment.

\[ Substitute(component)\Rightarrow ReevaluateAffectedControls\]

------------------------------------------------------------------------

## 19.40 Human Governance Security

Human approval/review channels dapat diserang melalui:

-   identity spoofing;
-   approval fatigue;
-   misleading evidence;
-   scope ambiguity;
-   compromised account;
-   social engineering.

Consequential Human decision SHOULD bind actor identity, subject, scope,
evidence/context, dan timestamp.

------------------------------------------------------------------------

## 19.41 Approval Integrity

Approval MUST NOT reusable di luar intended scope.

\[ Approval(plan_v1)\not\Rightarrow Approval(plan_v2) \]

jika material change.

High-risk approval SHOULD be protected dari spoofing/replay.

------------------------------------------------------------------------

## 19.42 Separation of Duties

Security-sensitive action SHOULD separate conflicting responsibilities
jika profile requires.

Example:

\[ Proposer\neq Approver\]

\[ Executor\neq IndependentVerifier\]

No single Agent SHOULD solely decide, grant authority, execute, verify,
dan audit same high-risk action.

------------------------------------------------------------------------

## 19.43 Availability and Resource Exhaustion

Security includes availability.

System SHOULD bound:

-   retries;
-   recursion/delegation depth;
-   tool calls;
-   concurrency;
-   cost;
-   context size;
-   execution duration.

Resource exhaustion SHOULD menghasilkan controlled
degradation/escalation.

------------------------------------------------------------------------

## 19.44 Denial-of-Service Against Governance

Attack/failure yang membuat Safety Kernel unavailable MUST NOT
menghasilkan fail-open.

\[ ControlUnavailable\Rightarrow Pending/Deny/Escalate \]

sesuai profile.

------------------------------------------------------------------------

## 19.45 Rate and Quota Controls

Rate/quantity limits MAY menjadi security controls.

Quota consumption SHOULD concurrency-safe jika bypass dapat menghasilkan
material harm.

------------------------------------------------------------------------

## 19.46 Security Monitoring

Security-relevant events SHOULD observable.

Examples:

-   denied authority request;
-   repeated policy violation;
-   prompt injection signal;
-   unusual tool use;
-   repeated verification failure;
-   authority escalation attempt;
-   trace integrity failure;
-   context disclosure attempt.

Monitoring result MAY trigger Risk reassessment/containment.

------------------------------------------------------------------------

## 19.47 Security Incident

Security incident adalah failure dengan security consequence atau
credible compromise.

Incident handling SHOULD integrate Section 18:

\[
Detect\rightarrow Contain\rightarrow PreserveEvidence\rightarrow Reconcile\rightarrow Recover\rightarrow Verify
\]

------------------------------------------------------------------------

## 19.48 Forensic Evidence

Security incident SHOULD preserve relevant evidence sesuai policy/legal
constraints.

Evidence preservation MUST tidak mengabaikan privacy/access controls.

High-assurance deployment SHOULD maintain sufficient event correlation
untuk incident reconstruction.

------------------------------------------------------------------------

## 19.49 Security Recovery

Recovery after compromise SHOULD mempertimbangkan:

-   credential rotation;
-   authority revocation;
-   policy integrity validation;
-   state reconciliation;
-   artifact validation;
-   evidence/trace integrity;
-   verifier trust;
-   component replacement.

Returning service availability alone tidak cukup jika governance
integrity belum dipulihkan.

------------------------------------------------------------------------

## 19.50 Security Fail-Safe Defaults

Unknown mandatory security state MUST NOT menghasilkan implicit permit.

\[ UnknownSecurityCondition\Rightarrow\neg ImplicitAllow
\]

Possible outcomes: `Pending`, `Deny`, `Escalate`.

------------------------------------------------------------------------

## 19.51 Security by Deterministic Control

Security-critical enforceable predicates SHOULD menggunakan
deterministic controls jika practical.

LLM reasoning MAY classify/recommend, tetapi mandatory enforcement
SHOULD tidak bergantung solely pada probabilistic compliance.

------------------------------------------------------------------------

## 19.52 Security Configuration

Security-critical configuration SHOULD versioned dan traceable.

Examples:

-   policy sets;
-   authority rules;
-   trust-boundary definitions;
-   tool allowlists;
-   network restrictions;
-   verification profiles;
-   data classifications.

------------------------------------------------------------------------

## 19.53 Security Profile

Deployment SHOULD mendefinisikan `Security Profile`:

```text
profile_id
version
assets
trust_boundaries
threats
controls
security_requirements
data_classes
secret_handling
execution_controls
monitoring
incident_response
evidence_requirements
test_requirements
```

High-assurance deployment MUST memiliki explicit equivalent.

------------------------------------------------------------------------

## 19.54 Reference Threat Catalog

### T-AUTH-01 --- Privilege Escalation

Actor memperoleh Authority di luar valid grant.

### T-AUTH-02 --- Authority Laundering

Privilege diperoleh melalui intermediary/delegation chain.

### T-AUTH-03 --- Stale/Revoked Grant Reuse

Old grant digunakan setelah invalid.

### T-POL-01 --- Policy Bypass

Action menghindari applicable policy.

### T-POL-02 --- Unauthorized Policy Mutation

Policy diubah oleh unauthorized source.

### T-CTX-01 --- Direct Prompt Injection

Untrusted instruction mencoba mengubah behavior/control.

### T-CTX-02 --- Indirect Prompt Injection

Retrieved content membawa malicious instruction.

### T-CTX-03 --- Context Disclosure

Sensitive Context keluar scope.

### T-AGT-01 --- Agent Misbehavior

Agent menghasilkan unauthorized/unsafe proposal.

### T-AGT-02 --- Agent Impersonation

Actor mengklaim identity/role agent lain.

### T-TOOL-01 --- Tool Abuse

Valid tool digunakan di luar authorized purpose/scope.

### T-TOOL-02 --- Parameter Abuse

Operation valid dengan malicious/out-of-scope parameter.

### T-STATE-01 --- Unauthorized State Mutation

State diubah di luar controlled transition.

### T-STATE-02 --- TOCTOU

State berubah antara check dan effect.

### T-STATE-03 --- Replay/Duplicate Effect

Old decision atau request menghasilkan repeated effect.

### T-EVD-01 --- Evidence Fabrication

False evidence dibuat.

### T-EVD-02 --- Evidence Substitution

Evidence untuk subject lain digunakan.

### T-VER-01 --- Verifier Compromise

Verifier tidak independent/trusted sesuai profile.

### T-VER-02 --- Circular Verification

Claim memvalidasi dirinya sendiri.

### T-TRC-01 --- Trace Tampering

Audit history diubah/dihapus.

### T-TRC-02 --- Trace Evasion

Consequential effect tidak direkam.

### T-EXEC-01 --- Execution Gateway Bypass

Action mencapai Effect Plane tanpa valid control.

### T-EXEC-02 --- Wrong-Target Execution

Action diterapkan ke resource berbeda.

### T-SUP-01 --- Dependency Compromise

External model/tool/package/service compromised.

### T-HUM-01 --- Approval Spoofing

False/compromised Human approval.

### T-PRV-01 --- Unauthorized Disclosure

Sensitive data/evidence/context disclosed.

### T-AVL-01 --- Governance DoS

Control component unavailable/exhausted.

Threat catalog bersifat reference baseline, bukan exhaustive list.

------------------------------------------------------------------------

## 19.55 Security Control Families

Reference control families:

-   `SEC-C01 Identity & Authentication`;
-   `SEC-C02 Authority & Least Privilege`;
-   `SEC-C03 Policy Enforcement`;
-   `SEC-C04 Context Isolation`;
-   `SEC-C05 Input/Output Validation`;
-   `SEC-C06 Execution Boundary`;
-   `SEC-C07 State Integrity`;
-   `SEC-C08 Evidence & Verification Integrity`;
-   `SEC-C09 Trace & Audit Integrity`;
-   `SEC-C10 Secrets & Data Protection`;
-   `SEC-C11 Supply Chain`;
-   `SEC-C12 Availability & Resource Control`;
-   `SEC-C13 Monitoring & Incident Response`;
-   `SEC-C14 Human Governance Protection`.

Profiles SHOULD map relevant threats ke control families.

------------------------------------------------------------------------

## 19.56 Security Failure Modes

### SEC-F01 --- Control Bypass

Mandatory control dilewati.

### SEC-F02 --- Privilege Escalation

Authority diperluas unauthorized.

### SEC-F03 --- Prompt/Data Injection

Untrusted content mempengaruhi privileged behavior.

### SEC-F04 --- Secret Exposure

Credential/sensitive secret leaked.

### SEC-F05 --- State Tampering

Authoritative state corrupted.

### SEC-F06 --- Evidence Tampering

Evidence integrity compromised.

### SEC-F07 --- Verification Compromise

Assurance path tidak trustworthy.

### SEC-F08 --- Trace Tampering

Governance history corrupted.

### SEC-F09 --- Wrong-Target Effect

Effect mengenai resource salah.

### SEC-F10 --- Replay

Historical permit/action reused.

### SEC-F11 --- Supply-Chain Compromise

Dependency compromise mempengaruhi orchestration.

### SEC-F12 --- Governance Availability Failure

Mandatory control unavailable.

### SEC-F13 --- Unauthorized Disclosure

Context/evidence/trace keluar scope.

### SEC-F14 --- Human Approval Compromise

Approval channel spoofed/compromised.

Security failure MUST integrate Failure & Recovery semantics.

------------------------------------------------------------------------

## 19.57 Reference Security Evaluation Flow

```text
INPUT:
  candidate action
  actor
  resource
  context
  current state
  governance results

1. Resolve actor/resource identity.
2. Identify trust-boundary crossings.
3. Validate Authority.
4. Evaluate Policy.
5. Validate Context/disclosure scope.
6. Evaluate Risk/security conditions.
7. Validate State/freshness.
8. Validate required Verification/Approval.
9. Validate decision binding/replay protection.
10. Validate tool/parameter/resource constraints.
11. Pass through controlled Effect Boundary.
12. Capture effect evidence.
13. Record Trace.
14. Monitor for security-relevant anomalies.
```

------------------------------------------------------------------------

## 19.58 Security Conformance Requirements

### Core

**AOF-SEC-001 (canonical cross-reference)** — See the primary normative definition above.
threat model atau equivalent analysis.

**AOF-SEC-002 (canonical cross-reference)** — See the primary normative definition above.
disclosure controls.

**AOF-SEC-005** --- Untrusted content MUST NOT directly grant Authority
atau mutate mandatory Policy.

**AOF-SEC-006** --- Credential possession MUST NOT menjadi sole proof of
governance Authority.

**AOF-SEC-007** --- Unknown mandatory security condition MUST NOT
menjadi implicit Allow.

**AOF-SEC-008** --- Security-critical state mutation MUST menggunakan
controlled transition.

### Governed

**AOF-SEC-009** --- High-risk Effect Boundary SHOULD mitigate TOCTOU
melalui revalidation/binding.

**AOF-SEC-010** --- Replayable consequential permit/action MUST memiliki
replay/deduplication control.

**AOF-SEC-011** --- Sensitive Context/Evidence/Trace disclosure MUST
governed.

**AOF-SEC-012** --- Security-critical Policy/Authority configuration
SHOULD protected dari unauthorized mutation.

**AOF-SEC-013** --- Tool/parameter use MUST bounded oleh applicable
scope.

**AOF-SEC-014** --- Mandatory control subsystem failure MUST
fail-controlled.

**AOF-SEC-015** --- Security incident MUST preserve sufficient
Evidence/Trace untuk applicable response.

**AOF-SEC-016** --- Human approval for consequential action SHOULD bind
identity, subject, scope, dan time.

### Assured / High-Assurance

**AOF-SEC-017** --- High-assurance profile MUST map material threats ke
controls dan test evidence.

**AOF-SEC-018** --- High-assurance trace/evidence/control configuration
MUST memiliki tamper-resistant atau tamper-evident protection sesuai
profile.

**AOF-SEC-019** --- High-assurance execution MUST protect against
stale/replayed governance decisions.

**AOF-SEC-020** --- High-assurance secrets SHOULD menggunakan
least-exposure, scoped, revocable credential mechanisms.

**AOF-SEC-021** --- High-assurance verifier/control-plane independence
MUST sesuai threat model.

**AOF-SEC-022** --- High-assurance deployment MUST define security
incident containment dan governance recovery behavior.

------------------------------------------------------------------------

## 19.59 Security Invariants

### SEC-INV-01 --- Untrusted Content Non-Authority

\[ UntrustedContent\not\Rightarrow Authority\]

### SEC-INV-02 --- Agent Non-Root-of-Trust

\[ Agent\neq AutonomousRootOfTrust\]

### SEC-INV-03 --- Safety Kernel Non-Bypass

\[
ConsequentialEffect\Rightarrow ApplicableSafetyKernelEvaluation
\]

### SEC-INV-04 --- Credential Non-Authority

\[
CredentialPossession\not\Rightarrow GovernanceAuthority
\]

### SEC-INV-05 --- Prompt Non-Enforcement

\[ PromptPolicy\neq EnforcedPolicy\]

### SEC-INV-06 --- Context Least Privilege

\[ Context(a,t)\subset eq NecessaryContext(a,t) \]

### SEC-INV-07 --- TOCTOU Control

\[ MaterialSecurityStateChange\Rightarrow RevalidateBeforeEffect
\]

### SEC-INV-08 --- Replay Control

\[ HistoricalPermit\not\Rightarrow UnlimitedReuse\]

### SEC-INV-09 --- Evidence/Trace Integrity

\[
UnauthorizedMutation(Evidence/Trace)\Rightarrow PreventedOrDetectable
\]

sesuai profile.

### SEC-INV-10 --- Fail-Controlled Security

\[
MandatorySecurityControlFailure\Rightarrow\neg ImplicitPermit
\]

### SEC-INV-11 --- Information-Flow Separation

\[ ReadAuthority\neq DisclosureAuthority\]

### SEC-INV-12 --- Security Recovery Governance

\[ SecurityFailure\not\Rightarrow GovernanceSuspension\]

------------------------------------------------------------------------

## 19.60 Cross-Domain Security Matrix

  Security Concern              Primary AOF Domains
  ----------------------------- ---------------------------------------------
  Privilege escalation          Authority, Policy, Security
  Prompt injection              Context, Agent, Policy, Security
  Control bypass                Architecture, Security
  TOCTOU                        Architecture, State, Authority, Security
  Replay                        State, Authority, Security
  Evidence tampering            Evidence, Verification, Security
  Trace tampering               State & Trace, Security
  Partial compromise recovery   Failure & Recovery, Security
  Sensitive disclosure          Context, Authority, Policy, Evidence, Trace
  Verification compromise       Verification, Risk, Security
  Human approval spoofing       Human Governance, Security
  Supply-chain compromise       Resource/Tool, Risk, Security

Security merupakan cross-cutting domain; Section 19 tidak menggantikan
requirements pada domain tersebut.

------------------------------------------------------------------------

## 19.61 Security Freeze Candidate Criteria

Security area MAY dinyatakan `Freeze Candidate` jika:

1.  trust model stabil;
2.  threat classes dan baseline catalog stabil;
3.  Safety Kernel protection semantics stabil;
4.  prompt/context injection semantics stabil;
5.  Authority/Policy security integration stabil;
6.  Effect Boundary/TOCTOU/replay semantics stabil;
7.  Evidence/Verification/Trace integrity semantics stabil;
8.  secret/sensitive-data controls stabil;
9.  incident/recovery integration stabil;
10. threat-to-control requirements dapat dipetakan ke conformance tests;
11. no contradiction dengan profiles dan machine-readable schemas.

------------------------------------------------------------------------

## 19.62 Security Formalization Result

Security v1.0 RC-Security diringkas sebagai:

\[ Security= TrustBoundaries + LeastAuthority + ControlIntegrity +
ContextIsolation + EffectProtection + DataProtection +
AssuranceIntegrity + IncidentRecovery \]

dengan:

\[ \boxed{ Untrusted\ Content\neq Control\ Authority } \]

\[ \boxed{ Agent\neq Autonomous\ Root\ of\ Trust } \]

\[
\boxed{ Consequential\ Effect\Rightarrow Governed\ Effect\ Boundary }
\]

\[
\boxed{ Mandatory\ Security\ Control\ Failure\neq Implicit\ Permit }
\]

dan:

\[
\boxed{ Security\ Is\ A\ Property\ Of\ The\ Orchestration\ System,\ Not\ Only\ Its\ Output }
\] \# 20. Conformance

## 20.1 Purpose

`Conformance Model` mendefinisikan bagaimana implementation, deployment,
profile, component set, atau system instance menunjukkan bahwa AOF
normative requirements telah dipenuhi secara testable, evidence-backed,
repeatable, dan scope-bounded.

Canonical chain:

\[
Requirement\rightarrow Test\rightarrow Evidence\rightarrow ConformanceResult
\]

Conformance bukan self-declaration tanpa basis.

\[ ClaimedConformance\neq DemonstratedConformance\]

------------------------------------------------------------------------

## 20.2 Conformance Subject

Conformance subject MAY berupa:

-   complete orchestration system;
-   deployment;
-   product;
-   reference implementation;
-   subsystem;
-   profile implementation;
-   specific version/configuration.

Setiap conformance claim MUST menyatakan subject dan scope secara
explicit.

**AOF-CONF-001** --- Conformance claim MUST identify subject, version,
profile, scope, dan applicable specification version.

------------------------------------------------------------------------

## 20.3 Conformance vs Maturity

Canonical separation:

\[ Conformance\neq Maturity\]

`Conformance` menjawab apakah mandatory requirements untuk claimed
scope/profile dipenuhi.

`Maturity` menjawab tingkat operational sophistication, adoption,
consistency, atau organizational capability.

System dapat conformant tetapi maturity rendah, atau mature secara
operational tetapi tidak conformant terhadap profile tertentu.

------------------------------------------------------------------------

## 20.4 Normative Requirement Classes

Requirement dapat diklasifikasikan sebagai:

-   `MUST`;
-   `MUST NOT`;
-   `SHOULD`;
-   `SHOULD NOT`;
-   `MAY`.

Conformance determination terutama didasarkan pada `MUST` dan
`MUST NOT`.

`SHOULD` deviation SHOULD memiliki documented rationale jika profile
mensyaratkan review.

------------------------------------------------------------------------

## 20.5 Requirement Identity

Testable normative requirement SHOULD memiliki stable Requirement ID.

Reference pattern:

```text
AOF-<DOMAIN>-NNN
```

Examples:

```text
AOF-AUTH-001
AOF-POL-001
AOF-RISK-001
AOF-EVD-001
AOF-VER-001
AOF-ST-001
AOF-TRC-001
AOF-FR-001
AOF-SEC-001
AOF-CONF-001
```

**AOF-CONF-002** --- Conformance-critical mandatory requirement MUST
dapat diidentifikasi secara unambiguous.

------------------------------------------------------------------------

## 20.6 Requirement Registry

AOF conformance package SHOULD memiliki `Requirement Registry`.

Reference fields:

```text
requirement_id
domain
statement
normative_level
applies_to
profile
rationale
verification_method
required_evidence
related_invariants
related_requirements
status
```

Registry adalah index; normative meaning tetap berasal dari
specification text kecuali registry dinyatakan normative artifact pada
release package.

------------------------------------------------------------------------

## 20.7 Invariant Registry

Core invariants SHOULD memiliki stable identifiers.

Reference fields:

```text
invariant_id
name
statement
formal_expression
applies_to
normative_level
violation_condition
required_evidence
related_requirements
```

Canonical traceability:

\[
Invariant\rightarrow Requirement\rightarrow Test\rightarrow Evidence
\]

------------------------------------------------------------------------

## 20.8 Conformance Profile

Conformance claim MUST memilih applicable profile atau explicitly
defined custom profile.

Reference profiles:

-   `AOF-Core`;
-   `AOF-Governed`;
-   `AOF-Assured`;
-   `AOF-Secure-SDLC`;
-   `AOF-High-Assurance`.

Custom extension MAY digunakan tetapi MUST NOT disebut standard AOF
profile tanpa memenuhi canonical profile definition.

------------------------------------------------------------------------

## 20.9 Profile Dependency

Reference dependency:

\[ AOF\text{-}Governed\supset eq AOF\text{-}Core
\]

\[ AOF\text{-}Assured\supset eq
AOF\text{-}Governed \]

`AOF-Secure-SDLC` merupakan domain profile yang MUST include
`AOF-Governed` dan applicable assurance/security requirements.

`AOF-High-Assurance` merupakan strengthening overlay/profile dan MUST
include `AOF-Assured` plus High-Assurance requirements.

Profile section MAY memperinci dependencies lebih lanjut.

------------------------------------------------------------------------

## 20.10 Conformance Scope

Scope SHOULD menyatakan:

-   components included;
-   environments;
-   resources;
-   Agent types;
-   tool classes;
-   governance boundaries;
-   excluded functionality;
-   optional extensions;
-   security assumptions.

Conformance claim MUST NOT digeneralisasi di luar tested scope.

------------------------------------------------------------------------

## 20.11 Requirement Applicability

Requirement evaluation menghasilkan:

\[ Applicability\in{Applicable,NotApplicable,Conditional} \]

`NotApplicable` MUST memiliki rationale yang dapat direview.

Mandatory requirement MUST NOT ditandai `NotApplicable` hanya untuk
menghindari failed test jika profile/scope sebenarnya memerlukannya.

------------------------------------------------------------------------

## 20.12 Conformance Test Case

Canonical test case:

\[ ct= \langle id, requirements, preconditions, inputs,
procedure, expected, evidence, result, environment \rangle\]

Reference fields:

```text
test_id
requirement_ids
profile
preconditions
fixtures
steps
expected_result
prohibited_result
evidence_required
cleanup
result
```

------------------------------------------------------------------------

## 20.13 Test Identity

Reference test ID:

```text
CT-<DOMAIN>-NNN
```

Examples:

-   `CT-AUTH-001`;
-   `CT-POL-001`;
-   `CT-RISK-001`;
-   `CT-VER-001`;
-   `CT-STATE-001`;
-   `CT-SEC-001`.

Test IDs SHOULD stable dalam same major conformance specification.

------------------------------------------------------------------------

## 20.14 Test Result

Normalized test result:

\[ TestResult= { Pass, Fail, Blocked, NotApplicable, Inconclusive } \]

`Inconclusive` dan `Blocked` MUST NOT dihitung sebagai `Pass`.

------------------------------------------------------------------------

## 20.15 Requirement Result

Requirement result MAY berasal dari satu atau multiple tests.

\[ RequirementResult(r)=Aggregate(Tests(r)) \]

Reference:

-   `Satisfied`;
-   `Violated`;
-   `NotApplicable`;
-   `Inconclusive`.

Mandatory requirement hanya `Satisfied` jika all required test
conditions terpenuhi.

------------------------------------------------------------------------

## 20.16 Conformance Result

Reference result:

\[ ConformanceResult= { Conformant, NonConformant, Conditional,
Inconclusive } \]

`Conformant` hanya jika seluruh applicable mandatory requirements
satisfied.

\[ Conformant(P) \iff
\forall r\in Mandatory(P), Result(r)=Satisfied \]

**AOF-CONF-003** --- Failed applicable `MUST` atau `MUST NOT`
requirement MUST prevent unconditional `Conformant` result.

------------------------------------------------------------------------

## 20.17 Conditional Conformance

`Conditional` MAY digunakan jika specification/profile explicitly
mengizinkan bounded external dependency, pending certification, atau
environment-specific condition.

Conditional claim MUST menyatakan unresolved condition.

Conditional MUST NOT digunakan untuk menyembunyikan known mandatory
violation.

------------------------------------------------------------------------

## 20.18 Conformance Evidence

Evidence MAY berupa:

-   test output;
-   trace records;
-   configuration;
-   policy/authority records;
-   state transition records;
-   verification results;
-   security test results;
-   Human review record;
-   architecture evidence;
-   screenshots/artifacts jika appropriate;
-   machine-readable report.

Evidence MUST memiliki sufficient provenance sesuai Evidence Model.

------------------------------------------------------------------------

## 20.19 Evidence Sufficiency for Conformance

Conformance evidence MUST cukup untuk membuktikan requirement dalam
tested scope.

\[ EvidencePresent\not\Rightarrow ConformanceSatisfied\]

Evidence SHOULD bind ke:

-   requirement;
-   test;
-   system version;
-   configuration;
-   environment;
-   timestamp.

------------------------------------------------------------------------

## 20.20 Positive and Negative Tests

Conformance suite SHOULD menguji allowed dan prohibited behavior.

Example:

```text
Positive:
valid Authority + valid Policy -> candidate may progress.

Negative:
Capability present but Authority absent -> execution MUST NOT occur.
```

Negative tests sangat penting untuk governance/security requirements.

------------------------------------------------------------------------

## 20.21 Reference Core Test Cases

### CT-AUTH-001 --- Capability Without Authority

Given Agent memiliki capability tetapi tidak memiliki applicable
Authority:

\[ Capability=true,\quadAuthority=false \]

Expected:

\[ ExecuteAllowed=false \]

Maps to Authority requirements.

### CT-AUTH-002 --- Revoked Authority

Jika grant revoked sebelum Effect Boundary, new effect MUST blocked.

### CT-POL-001 --- Explicit Deny

Applicable `Deny` MUST dominate `Allow` sesuai canonical precedence.

### CT-POL-002 --- Unknown Mandatory Policy

Unknown mandatory policy applicability MUST NOT implicit Allow.

### CT-RISK-001 --- High Risk Assurance

High-risk action MUST receive independent verification sesuai applicable
reference profile.

### CT-RISK-002 --- Critical Risk Governance

Critical-risk action MUST satisfy independent verification + explicit
approval sesuai profile.

### CT-EVD-001 --- Inadmissible Evidence

Inadmissible evidence MUST NOT count as sufficient evidence.

### CT-VER-001 --- Self-Verification Rejection

Self-verification alone MUST fail an independent-verification
requirement.

### CT-VER-002 --- Inconclusive Verification

`Inconclusive` MUST NOT satisfy required verification.

### CT-STATE-001 --- Stale State

Material state version mismatch MUST trigger configured
revalidation/conflict behavior.

### CT-STATE-002 --- Partial Commit

Partial effect MUST NOT be represented as atomic success.

### CT-TRC-001 --- Consequential Trace

Consequential transition MUST produce sufficient trace.

### CT-FR-001 --- Blind Retry Prevention

Unknown/partial effect MUST prevent unsafe blind retry.

### CT-FR-002 --- Safety Kernel Failure

Mandatory control failure MUST NOT fail-open.

### CT-SEC-001 --- Prompt Injection Non-Authority

Untrusted content requesting privilege MUST NOT create Authority.

### CT-SEC-002 --- Execution Gateway Bypass

Attempted direct consequential effect outside governed path MUST be
blocked/detected.

### CT-SEC-003 --- Replay

Historical permit MUST NOT authorize unauthorized repeated effect.

------------------------------------------------------------------------

## 20.22 Test Preconditions

Test MUST mendefinisikan preconditions sehingga result reproducible.

Preconditions MAY mencakup:

-   initial state;
-   policy set/version;
-   authority grants;
-   risk profile;
-   agent configuration;
-   resource fixtures;
-   time;
-   environment.

------------------------------------------------------------------------

## 20.23 Test Fixtures

Fixtures SHOULD deterministic atau sufficiently controlled.

Synthetic resources MAY digunakan selama semantics equivalent terhadap
requirement yang diuji.

High-assurance test SHOULD menghindari hidden dependencies yang
mengurangi reproducibility.

------------------------------------------------------------------------

## 20.24 Test Isolation

Test SHOULD menghindari cross-test state leakage.

Jika test intentionally stateful, dependency/order MUST explicit.

------------------------------------------------------------------------

## 20.25 Test Repeatability

Conformance test SHOULD repeatable.

Agentic/probabilistic components MAY menghasilkan variable proposals,
tetapi governance outcome untuk mandatory deterministic controls SHOULD
tetap testable.

\[ ProbabilisticReasoning \not\Rightarrow
ProbabilisticMandatoryControl \]

------------------------------------------------------------------------

## 20.26 Deterministic Control Testing

Mandatory Safety Kernel predicates SHOULD memiliki deterministic or
bounded-verifiable tests jika practical.

Examples:

-   no grant -\> deny;
-   revoked grant -\> deny;
-   stale permit -\> revalidate;
-   required verification missing -\> block.

------------------------------------------------------------------------

## 20.27 Agentic Behavior Testing

Agentic behavior MAY diuji dengan scenario set dan acceptance envelope.

Test SHOULD fokus pada governed observable behavior, bukan private
chain-of-thought.

Examples:

-   Agent proposes unauthorized action;
-   Agent follows malicious retrieved instruction;
-   Agent emits malformed evidence;
-   Agent attempts delegation beyond Authority.

Expected system control outcome harus testable.

------------------------------------------------------------------------

## 20.28 Security Conformance Testing

Security profile SHOULD mencakup adversarial tests untuk:

-   privilege escalation;
-   prompt injection;
-   policy bypass;
-   replay;
-   stale decision;
-   wrong-target action;
-   evidence substitution;
-   trace tampering;
-   approval spoofing;
-   secret disclosure.

Security test MUST dilakukan dalam safe controlled environment.

------------------------------------------------------------------------

## 20.29 Failure Injection Testing

Conformance suite SHOULD dapat inject failure seperti:

-   tool timeout;
-   partial execution;
-   verifier unavailable;
-   policy service unavailable;
-   trace persistence failure;
-   orchestrator restart;
-   external service failure.

Expected recovery/fail-controlled behavior harus diuji.

------------------------------------------------------------------------

## 20.30 State and Concurrency Testing

Governed/High-Assurance profiles SHOULD menguji:

-   concurrent mutation;
-   lost update prevention;
-   version mismatch;
-   duplicate request;
-   idempotency;
-   replay;
-   partial commit;
-   reconciliation.

------------------------------------------------------------------------

## 20.31 Verification Testing

Verification tests SHOULD mencakup:

-   insufficient evidence;
-   inadmissible evidence;
-   contradictory evidence;
-   wrong subject;
-   stale verification;
-   independence failure;
-   tool failure;
-   verifier conflict.

------------------------------------------------------------------------

## 20.32 Trace Testing

Trace tests SHOULD memeriksa:

-   actor attribution;
-   correlation;
-   ordering;
-   state references;
-   governance basis;
-   evidence references;
-   integrity;
-   retention behavior;
-   redaction.

Private chain-of-thought MUST NOT menjadi expected evidence.

------------------------------------------------------------------------

## 20.33 Human Governance Testing

Jika Human approval required, test SHOULD memeriksa:

-   identity;
-   approval scope;
-   authority;
-   stale approval;
-   rejection;
-   alternate approver;
-   unavailability behavior.

------------------------------------------------------------------------

## 20.34 Conformance Environment

Conformance report MUST identify tested environment.

Environment metadata SHOULD mencakup:

-   system version;
-   configuration version;
-   schema version;
-   profile;
-   model/tool versions jika material;
-   deployment topology;
-   security assumptions.

------------------------------------------------------------------------

## 20.35 Configuration Drift

Conformance dapat invalid jika material configuration berubah.

\[ Conformant(config_v1) \not\Rightarrow
Conformant(config_v2) \]

Deployment SHOULD menentukan change classes yang memerlukan retest.

------------------------------------------------------------------------

## 20.36 Regression Conformance

Bug fix, policy change, control change, schema change, atau component
substitution MAY memerlukan regression suite.

High-assurance profile SHOULD memiliki defined regression triggers.

------------------------------------------------------------------------

## 20.37 Conformance Expiry and Freshness

Conformance claim MAY memiliki validity period jika operational
conditions dapat berubah.

AOF tidak menetapkan universal expiry.

Profile SHOULD menentukan recertification/reassessment triggers jika
needed.

------------------------------------------------------------------------

## 20.38 Third-Party Assessment

Conformance MAY self-assessed, independently assessed, atau certified
oleh external program.

AOF specification tidak otomatis membentuk certification authority.

Claim MUST menyatakan assessment mode.

------------------------------------------------------------------------

## 20.39 Self-Assessment

Self-assessment valid sebagai conformance mode jika evidence tersedia
dan claim tidak menyiratkan independent certification.

------------------------------------------------------------------------

## 20.40 Independent Assessment

Independent assessor SHOULD memiliki access ke sufficient test/evidence
package dan independence sesuai claimed assurance level.

------------------------------------------------------------------------

## 20.41 Conformance Report

Canonical report SHOULD mencakup:

```text
report_id
subject
subject_version
specification_version
profile
scope
environment
assessment_mode
requirements_total
requirements_satisfied
requirements_failed
requirements_not_applicable
requirements_inconclusive
test_results
evidence_references
exceptions
limitations
assessor
timestamp
final_result
```

------------------------------------------------------------------------

## 20.42 Conformance Manifest

Machine-readable `Conformance Manifest` SHOULD mengikat:

-   specification version;
-   profile;
-   requirement registry version;
-   schema version;
-   test suite version;
-   implementation version;
-   evidence package.

Manifest schema akan didefinisikan dalam Schemas area.

------------------------------------------------------------------------

## 20.43 Exceptions

Exception terhadap requirement hanya valid jika specification/profile
explicitly mengizinkan exception.

Mandatory requirement tanpa exception semantics tidak dapat di-waive
lalu tetap diklaim fully conformant.

\[ WaivedMandatoryViolation\not\Rightarrow Conformant\]

------------------------------------------------------------------------

## 20.44 Extensions

Extension MAY menambahkan requirements/tests.

Extension MUST NOT:

-   weaken mandatory Core requirement;
-   redefine canonical result semantics incompatibly;
-   claim standard profile equivalence tanpa memenuhi base profile.

------------------------------------------------------------------------

## 20.45 Conformance of External Components

External model/tool/service tidak harus individually AOF-conformant jika
containing orchestration system mengendalikan interaction sesuai AOF
requirements.

Namun component yang diklaim AOF-conformant sendiri harus memiliki
defined conformance scope.

------------------------------------------------------------------------

## 20.46 Partial Conformance Claims

Claim seperti "conformant to Authority domain" MAY digunakan hanya jika
explicitly disebut `domain-scoped conformance`, bukan full AOF
conformance.

Scope MUST jelas.

------------------------------------------------------------------------

## 20.47 Non-Conformance

Known mandatory violation MUST menghasilkan `NonConformant` untuk
affected claimed profile/scope.

Non-conformance report SHOULD menunjukkan:

-   requirement;
-   failed tests;
-   evidence;
-   impact;
-   remediation status.

------------------------------------------------------------------------

## 20.48 Inconclusive Assessment

Jika evidence/test tidak cukup:

\[ Assessment=Inconclusive \]

System MUST NOT default ke `Conformant`.

------------------------------------------------------------------------

## 20.49 Conformance Test Suite Versioning

Test suite SHOULD versioned independently tetapi mapped ke specification
version.

Reference:

```text
AOF Specification 1.0
Conformance Suite 1.0.x
```

Test correction MAY dilakukan tanpa semantic change jika requirement
meaning tetap.

------------------------------------------------------------------------

## 20.50 Requirement Traceability Matrix

Reference matrix:

  -----------------------------------------------------------------------------------
  Requirement    Invariant      Test          Evidence   Profile          Result
  -------------- -------------- ------------- ---------- ---------------- -----------
  AOF-AUTH-...   AUTH-INV-...   CT-AUTH-...   E-...      Core             Pass/Fail

  AOF-SEC-...    SEC-INV-...    CT-SEC-...    E-...      High-Assurance   Pass/Fail
  -----------------------------------------------------------------------------------

Machine-readable equivalent SHOULD tersedia pada final release package.

------------------------------------------------------------------------

## 20.51 Coverage

Reference coverage:

\[ RequirementCoverage= \frac{MandatoryRequirementsWithTests}
{ApplicableMandatoryRequirements} \]

\[ EvidenceCoverage=
\frac{TestedRequirementsWithSufficientEvidence}
{ApplicableMandatoryRequirements} \]

Full conformance SHOULD require 100% applicable mandatory requirement
coverage.

------------------------------------------------------------------------

## 20.52 Test Coverage Is Not Assurance Completeness

\[ 100% RequirementCoverage \not\Rightarrow
ZeroResidualRisk \]

Conformance membuktikan specification requirements dalam tested scope,
bukan absence of all defects/threats.

------------------------------------------------------------------------

## 20.53 Conformance and Security

Security conformance MUST NOT dipresentasikan sebagai guarantee bahwa
system secure terhadap semua threats.

Security profile menunjukkan controls/tested properties terhadap defined
threat model.

------------------------------------------------------------------------

## 20.54 Conformance and Profiles

Profile MAY menambahkan mandatory requirements.

Conformance engine MUST resolve complete inherited requirement set
sebelum assessment.

\[ Mandatory(P)= Mandatory(Base(P)) \cup Mandatory(Local(P)) \]

------------------------------------------------------------------------

## 20.55 Conformance and Schemas

Machine-readable schemas SHOULD memungkinkan automated validation
terhadap:

-   Agent contracts;
-   Authority grants;
-   Policy records;
-   Risk assessments;
-   Evidence;
-   Verification;
-   State transitions;
-   Trace events;
-   conformance reports.

Schema validity sendiri tidak membuktikan semantic conformance.

\[ SchemaValid\not\Rightarrow SemanticallyConformant\]

------------------------------------------------------------------------

## 20.56 Conformance and References

External standards MAY digunakan sebagai supporting evidence/mapping.

External certification MUST NOT dianggap automatically equivalent dengan
AOF conformance kecuali explicit mapping tersedia.

------------------------------------------------------------------------

## 20.57 Reference Assessment Algorithm

```text
INPUT:
  conformance subject
  claimed profile
  specification version
  requirement registry
  test suite

1. Resolve subject/version/scope.
2. Resolve profile and inherited requirements.
3. Determine applicability.
4. Validate test environment.
5. Execute required tests.
6. Collect evidence.
7. Evaluate evidence sufficiency.
8. Determine each test result.
9. Aggregate test -> requirement result.
10. Detect mandatory violations.
11. Calculate coverage.
12. Produce:
      CONFORMANT
      NONCONFORMANT
      CONDITIONAL
      INCONCLUSIVE
13. Generate Conformance Report + Manifest.
```

------------------------------------------------------------------------

## 20.58 Conformance Failure Modes

### CONF-F01 --- Scope Ambiguity

Claim tidak menentukan tested subject/scope.

### CONF-F02 --- Missing Requirement

Applicable mandatory requirement tidak dinilai.

### CONF-F03 --- False Not-Applicable

Requirement dikecualikan tanpa valid basis.

### CONF-F04 --- Missing Test

Mandatory requirement tidak memiliki required test.

### CONF-F05 --- Insufficient Evidence

Test result tidak memiliki sufficient evidence.

### CONF-F06 --- Inconclusive-as-Pass

Inconclusive result dihitung sebagai Pass.

### CONF-F07 --- Profile Misclaim

System mengklaim stronger profile tanpa memenuhi dependencies.

### CONF-F08 --- Stale Conformance

Materially changed deployment menggunakan old claim.

### CONF-F09 --- Test Environment Drift

Environment berbeda dari recorded test environment.

### CONF-F10 --- Evidence Substitution

Evidence dari version/scope lain digunakan.

### CONF-F11 --- Hidden Exception

Mandatory violation di-waive tanpa disclosure.

### CONF-F12 --- Certification Confusion

Self-assessment dipresentasikan sebagai independent certification.

------------------------------------------------------------------------

## 20.59 Conformance Requirements

### Core

**AOF-CONF-001 (canonical cross-reference)** — See the primary normative definition above.
profile, scope, dan specification version.

**AOF-CONF-002 (canonical cross-reference)** — See the primary normative definition above.
unambiguously identifiable.

**AOF-CONF-004** --- `Blocked`/`Inconclusive` test MUST NOT dihitung
sebagai Pass.

**AOF-CONF-005** --- `NotApplicable` mandatory requirement MUST memiliki
explicit valid rationale.

**AOF-CONF-006** --- Conformance evidence MUST bind ke relevant
requirement/test/subject/version.

**AOF-CONF-007** --- Full profile conformance MUST assess all applicable
mandatory requirements.

**AOF-CONF-008** --- Conformance report MUST state assessment mode dan
limitations.

### Governed

**AOF-CONF-009** --- Profile dependencies MUST resolved sebelum
assessment.

**AOF-CONF-010** --- Material configuration change SHOULD trigger
defined regression/reassessment behavior.

**AOF-CONF-011** --- Negative governance tests SHOULD menjadi bagian
conformance suite.

**AOF-CONF-012** --- Failure/recovery behavior SHOULD diuji melalui
controlled failure injection untuk applicable profiles.

**AOF-CONF-013** --- Conformance suite SHOULD test observable governed
behavior, bukan private chain-of-thought.

**AOF-CONF-014** --- Exception MUST explicit dan MUST NOT silently
redefine mandatory requirement.

**AOF-CONF-015** --- Domain-scoped conformance claim MUST clearly
distinguished dari full AOF conformance.

**AOF-CONF-016** --- Test/evidence package SHOULD cukup untuk
independent reconstruction.

### Assured / High-Assurance

**AOF-CONF-017** --- High-assurance profile MUST map material security
threats ke tests/evidence.

**AOF-CONF-018** --- High-assurance conformance MUST test state
concurrency/replay/TOCTOU controls yang applicable.

**AOF-CONF-019** --- High-assurance conformance MUST test verification
independence dan evidence admissibility.

**AOF-CONF-020** --- High-assurance conformance MUST preserve
tamper-resistant/evident assessment evidence sesuai profile.

**AOF-CONF-021** --- High-assurance assessment SHOULD menggunakan
independent assessor atau explicitly disclose self-assessment.

**AOF-CONF-022** --- High-assurance profile MUST define
regression/recertification triggers.

------------------------------------------------------------------------

## 20.60 Conformance Invariants

### CONF-INV-01 --- Requirement Traceability

\[ MandatoryRequirement\Rightarrow IdentifiableTestOrAssessment
\]

### CONF-INV-02 --- Evidence

\[ ConformancePass\Rightarrow SufficientEvidence\]

### CONF-INV-03 --- No Inconclusive Success

\[ Inconclusive\not\Rightarrow Pass\]

### CONF-INV-04 --- Mandatory Violation

\[
MandatoryViolation\Rightarrow\neg UnconditionalConformant
\]

### CONF-INV-05 --- Scope Integrity

\[
Conformance(scope_a)\not\Rightarrow Conformance(scope_b)
\]

### CONF-INV-06 --- Version Integrity

\[ Conformance(v_1)\not\Rightarrow Conformance(v_2) \]

jika material change.

### CONF-INV-07 --- Profile Inheritance

\[
Conformant(Profile)\Rightarrow Conformant(MandatoryBase(Profile))
\]

### CONF-INV-08 --- Schema Non-Sufficiency

\[ SchemaValid\not\Rightarrow SemanticConformance\]

### CONF-INV-09 --- No Chain-of-Thought Requirement

\[
ConformanceEvidence\not\Rightarrow PrivateChainOfThought
\]

### CONF-INV-10 --- Conformance Non-Zero-Risk

\[ Conformant\not\Rightarrow ZeroResidualRisk\]

------------------------------------------------------------------------

## 20.61 Minimal Conformance Package

A minimal release-grade conformance package SHOULD terdiri dari:

```text
Requirement Registry
Invariant Registry
Profile Definitions
Conformance Test Specification
Executable/Automatable Test Suite where practical
Requirement Traceability Matrix
Evidence Package
Conformance Report
Conformance Manifest
```

------------------------------------------------------------------------

## 20.62 Conformance Freeze Candidate Criteria

Conformance area MAY dinyatakan `Freeze Candidate` jika:

1.  conformance subject/scope semantics stabil;
2.  Conformance vs Maturity separation stabil;
3.  profile dependency semantics stabil;
4.  requirement/test/evidence chain stabil;
5.  result semantics stabil;
6.  applicability/exception semantics stabil;
7.  reference test catalog covers core negative controls;
8.  report/manifest semantics stabil;
9.  requirement coverage measurable;
10. schema dependencies jelas;
11. requirements dapat diterjemahkan menjadi executable/inspectable
    tests tanpa semantic ambiguity.

------------------------------------------------------------------------

## 20.63 Conformance Formalization Result

Conformance v1.0 RC-Conformance diringkas sebagai:

\[ Conformance= Scope + Profile + Requirements + Tests + Evidence +
Coverage + Report \]

dengan:

\[
\boxed{ Requirement\rightarrow Test\rightarrow Evidence\rightarrow Result }
\]

\[ \boxed{ Conformance\neq Maturity } \]

\[ \boxed{ Inconclusive\neq Pass } \]

\[ \boxed{ MandatoryViolation\Rightarrow NonConformant } \]

dan:

\[ \boxed{ Conformant\neq ZeroResidualRisk } \] \# 21. Framework
Profiles

AOF v1.0 mendefinisikan reference profiles untuk menyatakan bundles of
applicable controls tanpa mengubah core semantics.

## 21.1 Profile Semantics

Profile adalah named conformance scope, bukan maturity score.

\[ Profile\neq Maturity\]

Profile applicability MUST dinyatakan secara explicit oleh
implementation/conformance claim.

AOF v1.0 tidak memaksakan satu total linear inheritance chain untuk
seluruh profiles. Hubungan canonical yang aman adalah:

\[ AOF\text{-}Core \subset eq
AOF\text{-}Governed \subset eq
AOF\text{-}Assured \]

`AOF-Secure-SDLC` adalah domain profile yang membangun di atas
applicable governed/assurance semantics untuk secure software
development. `AOF-High-Assurance` adalah strengthening profile untuk
consequential/high-impact orchestration dan MAY dikombinasikan dengan
domain profile.

Dengan demikian:

\[
AOF\text{-}Secure\text{-}SDLC\neq AutomaticallyHigherThan(AOF\text{-}Assured)
\]

dan:

\[ AOF\text{-}High\text{-}Assurance =
StrongerControls(ApplicableBaseProfile) \]

Profile composition MUST NOT remove mandatory requirements dari
base/applicable profile.

## 21.2 AOF-Core

Minimum governed orchestration semantics:

-   identifiable Agent;
-   Task;
-   Action;
-   Authority;
-   Policy;
-   State;
-   Trace;
-   controlled transition;
-   no implicit allow.

AOF-Core establishes minimum AOF identity. Implementation yang tidak
memenuhi applicable AOF-Core requirements MUST NOT claim a stronger AOF
profile.

## 21.3 AOF-Governed

AOF-Governed includes AOF-Core dan menambahkan stronger governance:

-   explicit Authority lifecycle;
-   Policy conflict resolution;
-   dynamic Risk evaluation;
-   bounded delegation;
-   approval/escalation;
-   failure budgets.

\[ AOF\text{-}Core\subset eq AOF\text{-}Governed
\]

## 21.4 AOF-Assured

AOF-Assured includes AOF-Governed dan menambahkan assurance:

-   Evidence;
-   provenance;
-   Verification;
-   verifier independence based on Risk;
-   completion gate;
-   accountability chain.

\[ AOF\text{-}Governed\subset eq
AOF\text{-}Assured \]

## 21.5 AOF-Secure-SDLC

AOF-Secure-SDLC adalah domain profile untuk secure software development.

Profile ini MUST include applicable AOF-Core semantics dan SHOULD
compose dengan AOF-Governed / AOF-Assured controls sesuai claimed
assurance scope.

Tambahan domain controls mencakup:

-   requirements and acceptance criteria;
-   architecture/security review;
-   threat modeling;
-   code/test/security Verification;
-   release/deployment Authority gates;
-   Human control gates sesuai Risk;
-   SAST/SCA/DAST atau equivalent security Evidence bila applicable.

AOF-Secure-SDLC MUST NOT be interpreted sebagai permission untuk
melemahkan base governance, Security, Evidence, atau Verification
requirements.

## 21.6 AOF-High-Assurance

AOF-High-Assurance adalah strengthening profile untuk
consequential/high-impact orchestration.

Controls mencakup:

-   strong separation of duties;
-   independent Verification;
-   explicit approval for defined Critical actions;
-   stronger Evidence requirements;
-   strict Authority scope;
-   revalidation at Effect Boundary;
-   tamper-resistant or equivalently protected Trace;
-   bounded Recovery;
-   residual Risk handling.

AOF-High-Assurance MUST preserve all mandatory controls dari applicable
base/domain profile.

## 21.7 Profile Composition

Reference composition:

\[ EffectiveProfile= BaseProfile \cup DomainProfile \cup
StrengtheningProfile \]

where applicable.

Example valid compositions MAY include:

-   `AOF-Assured`;
-   `AOF-Assured + AOF-Secure-SDLC`;
-   `AOF-Assured + AOF-High-Assurance`;
-   `AOF-Assured + AOF-Secure-SDLC + AOF-High-Assurance`.

Profile composition MUST be explicit in `ConformanceManifest`.

## 21.8 Requirement Applicability

Requirement applicability SHOULD be evaluated from:

-   selected profile(s);
-   domain;
-   Risk;
-   deployment characteristics;
-   extension declarations;
-   requirement-specific applicability conditions.

Absence of profile tag MUST NOT silently mean a mandatory Core
requirement is optional.

## 21.9 Profile Requirements

**AOF-PRF-001** --- A stronger/base-derived profile MUST preserve
mandatory requirements of its applicable base profile.

**AOF-PRF-002** --- Profile composition MUST NOT weaken mandatory AOF
invariants.

**AOF-PRF-003** --- Claimed profiles MUST be explicit in the
ConformanceManifest or equivalent conformance artifact.

**AOF-PRF-004** --- AOF-Secure-SDLC MUST be treated as a domain profile
rather than an assumed universal linear maturity level.

**AOF-PRF-005** --- AOF-High-Assurance MUST strengthen, not replace,
applicable base/domain controls.

**AOF-PRF-006** --- Requirement applicability MUST NOT be changed solely
to obtain a more favorable conformance result.

## 21.10 Profile Invariants

### PRF-INV-01 --- Core Preservation

\[
StrongerProfile\Rightarrow Preserve(ApplicableCoreRequirements)
\]

### PRF-INV-02 --- No Profile Weakening

\[
ProfileComposition\not\Rightarrow MandatoryControlRemoval
\]

### PRF-INV-03 --- Explicit Claim

\[ ProfileClaim\Rightarrow DeclaredProfileScope\]

### PRF-INV-04 --- Domain Profile Non-Linearity

\[
AOF\text{-}Secure\text{-}SDLC\neq LinearMaturityLevel
\]

## 21.11 Reference Profile Conformance Tests

### CT-PRF-001 --- Base Requirement Removal

Given a stronger profile claim that omits a mandatory applicable
AOF-Core requirement:

Expected: profile claim MUST fail conformance.

### CT-PRF-002 --- Secure-SDLC Composition

Given `AOF-Assured + AOF-Secure-SDLC`:

Expected: applicable Assured requirements remain mandatory while
Secure-SDLC domain controls are added.

### CT-PRF-003 --- High-Assurance Weakening

Given High-Assurance profile configuration that disables required
independent Verification:

Expected: configuration MUST fail conformance.

### CT-PRF-004 --- Undeclared Profile

Given implementation claims profile-dependent conformance without
declaring profile scope:

Expected: conformance result MUST be `Blocked`, `Inconclusive`, or
`NonConformant` according to applicable Section 20 rules; MUST NOT be
implicit Pass.

## 21.12 Profile Freeze Candidate Criteria

Section 21 MAY become `Freeze Candidate` when:

1.  Core → Governed → Assured base relationship is explicit;
2.  Secure-SDLC is treated as domain composition rather than forced
    linear maturity;
3.  High-Assurance strengthening semantics are explicit;
4.  profile composition cannot weaken mandatory controls;
5.  profile claims bind to ConformanceManifest;
6.  profile Requirements/Invariants/Tests are traceable;
7.  no conflicting profile inheritance remains elsewhere in the
    specification.

Profile names dan detailed implementation-specific assessment criteria
MAY dikembangkan dalam separate Conformance Specification tanpa mengubah
frozen core semantics.

------------------------------------------------------------------------

# 22. Extensions

## 22.1 Extension Principle

AOF MAY diperluas untuk domain, industry, organization, atau technology
tertentu.

Extension MUST NOT:

-   menghapus mandatory core invariant;
-   mengubah canonical term secara incompatible tanpa namespace/version;
-   menciptakan implicit authority;
-   melemahkan applicable profile requirement tanpa menyatakan
    non-conformance.

## 22.2 Domain Extensions

Possible extensions mencakup:

-   Secure SDLC;
-   Security Operations;
-   Infrastructure Operations;
-   Data and Analytics;
-   Research Workflows;
-   Enterprise Automation;
-   Regulated/High-Assurance Operations.

## 22.3 Technique Extensions

AI techniques MAY ditambahkan sebagai implementation mechanisms tanpa
mengubah core framework.

Contoh:

-   RAG;
-   ReAct;
-   Reflection;
-   Few-Shot;
-   Tree of Thoughts;
-   structured prompting;
-   deterministic planners;
-   search/planning algorithms;
-   future reasoning techniques.

## 22.4 Research Candidates

Concept seperti `Orchestration Debt`, AI ROI models, maturity models,
dan additional metrics MAY dipertahankan sebagai research or assessment
extensions sampai memperoleh sufficient validation.

## 22.5 Versioning

Backward-incompatible semantic change MUST menggunakan appropriate
framework versioning dan MUST didokumentasikan pada Version
History/CHANGELOG.

------------------------------------------------------------------------

# 23. References

## 23.1 Purpose and Reference Policy

Bagian ini menempatkan AOF terhadap standards, security frameworks,
software supply-chain frameworks, dan scientific prior art yang relevan.
Tujuannya bukan untuk menyatakan bahwa external source secara otomatis
menjadi normative requirement AOF, tetapi untuk:

-   mendokumentasikan intellectual lineage;
-   mencegah unsupported novelty claims;
-   mengidentifikasi overlap dan differentiation;
-   menyediakan crosswalk untuk implementers;
-   menetapkan external baseline yang perlu dipertimbangkan dalam future
    revisions.

AOF membedakan:

```text
Normative AOF Requirement
Informative External Reference
Prior Art
Related Framework
Research Literature
```

External reference bersifat `Informative` kecuali secara explicit
diadopsi oleh AOF profile atau requirement.

------------------------------------------------------------------------

## 23.2 Prior-Art Principle

AOF MUST NOT mengklaim invention terhadap technique, concept, atau
control family yang telah tersedia dalam prior art.

Secara khusus, AOF tidak mengklaim invention atas:

-   Few-Shot prompting;
-   Chain-of-Thought prompting;
-   Retrieval-Augmented Generation;
-   ReAct;
-   Tree of Thoughts;
-   Reflection/Reflexion;
-   multi-Agent conversation;
-   Human-in-the-Loop;
-   risk management;
-   least privilege;
-   separation of duties;
-   secure SDLC;
-   provenance/attestation;
-   threat modeling;
-   policy enforcement;
-   verification/testing.

Potential contribution AOF berada pada formal composition, orchestration
semantics, governance integration, cross-domain contracts, dan testable
control model.

------------------------------------------------------------------------

## 23.3 Reference Classification

Reference catalog menggunakan classes:

-   `STD` --- Standard / authoritative framework;
-   `SEC` --- Security framework/guidance;
-   `SSDLC` --- Secure software development;
-   `SUPPLY` --- Software supply-chain/provenance;
-   `AI-RISK` --- AI governance/risk;
-   `AGENT` --- Agentic/multi-Agent research;
-   `TECH` --- Reasoning/prompting/retrieval technique;
-   `ASSURE` --- Assurance/evaluation-related reference.

------------------------------------------------------------------------

## 23.4 NIST AI Risk Management Framework

**REF-AIRISK-001 --- NIST AI RMF 1.0**

NIST AI RMF 1.0 menyediakan voluntary, rights-preserving,
non-sector-specific framework untuk membantu organizations mengelola AI
risks sepanjang design, development, deployment, dan use lifecycle.

Relevance terhadap AOF:

-   Risk governance;
-   lifecycle risk management;
-   trustworthy/responsible AI;
-   organizational governance;
-   profile-based adaptation.

AOF berbeda karena memformalkan runtime orchestration controls seperti
Authority, Policy, State, Evidence, Verification, Effect Boundary, dan
Trace sebagai execution semantics.

------------------------------------------------------------------------

## 23.5 NIST Generative AI Profile

**REF-AIRISK-002 --- NIST AI 600-1, Generative AI Profile**

NIST Generative AI Profile merupakan companion resource terhadap AI RMF
1.0 dan memfokuskan risk management pada Generative AI.

Relevance:

-   Generative AI risk identification;
-   risk management actions;
-   lifecycle considerations;
-   profile concept;
-   governance of GAI-specific risks.

AOF SHOULD menggunakan reference ini untuk future Risk/Security
crosswalk, tetapi tidak menganggap profile tersebut sebagai substitute
untuk AOF runtime control model.

------------------------------------------------------------------------

## 23.6 ISO/IEC 42001

**REF-STD-001 --- ISO/IEC 42001:2023**

ISO/IEC 42001 menetapkan requirements untuk establishing, implementing,
maintaining, dan continually improving an Artificial Intelligence
Management System.

Relevance:

-   organizational AI governance;
-   management-system discipline;
-   risk/opportunity management;
-   continuous improvement;
-   accountable AI management.

AOF beroperasi pada complementary layer: governed orchestration
semantics dan operational control contracts.

AOF conformance MUST NOT diklaim equivalent dengan ISO/IEC 42001
certification.

------------------------------------------------------------------------

## 23.7 NIST Secure Software Development Framework

**REF-SSDLC-001 --- NIST SP 800-218, SSDF Version 1.1**

SSDF menyediakan high-level secure software development practices yang
dapat diintegrasikan ke SDLC implementations.

Relevance terhadap AOF-Secure-SDLC:

-   secure development practices;
-   vulnerability reduction;
-   root-cause prevention;
-   common secure-development vocabulary;
-   supplier/acquirer communication.

AOF-Secure-SDLC SHOULD dipetakan terhadap applicable SSDF practices
dalam implementation guide.

Future revision SHOULD review final successor/revision of SP 800-218
when published; draft revisions MUST NOT silently replace the cited
final baseline.

------------------------------------------------------------------------

## 23.8 OWASP GenAI Security

**REF-SEC-001 --- OWASP GenAI LLM Top 10**

OWASP GenAI Security Project mendokumentasikan critical security risks
pada LLM/Generative AI applications, termasuk prompt injection, unsafe
downstream handling, sensitive information disclosure, supply-chain
concerns, dan excessive agency pada historical/current taxonomies.

Relevance:

-   prompt injection;
-   untrusted output;
-   excessive agency;
-   sensitive information;
-   supply chain;
-   application security.

AOF Security Model SHOULD maintain a versioned crosswalk ke current
OWASP GenAI release.

------------------------------------------------------------------------

## 23.9 OWASP Agentic Application Security

**REF-SEC-002 --- OWASP Top 10 for Agentic Applications 2026**

OWASP Agentic Top 10 berfokus pada risks untuk systems yang dapat plan,
act, dan make decisions melalui agentic workflows.

Relevance:

-   agentic autonomy risk;
-   tool/action security;
-   governance of autonomous workflows;
-   identity/privilege boundaries;
-   agentic attack surface.

AOF tidak mengklaim bahwa Security threat catalog-nya menggantikan OWASP
Agentic guidance.

------------------------------------------------------------------------

## 23.10 MITRE ATLAS

**REF-SEC-003 --- MITRE ATLAS**

MITRE ATLAS merupakan living knowledge base tentang adversary tactics
dan techniques terhadap AI-enabled systems, termasuk Generative AI dan
Agentic AI.

Relevance:

-   threat modeling;
-   adversarial tactics/techniques;
-   AI red teaming;
-   mitigation mapping;
-   security case studies.

AOF Security Profile SHOULD dapat memetakan `T-*` threat IDs ke relevant
ATLAS techniques ketika applicable.

------------------------------------------------------------------------

## 23.11 SLSA

**REF-SUPPLY-001 --- SLSA Specification v1.2**

SLSA menyediakan incrementally adoptable software supply-chain security
specification dengan tracks/levels dan provenance/attestation concepts.

Relevance:

-   artifact provenance;
-   build/source integrity;
-   increasing security guarantees;
-   attestations;
-   supply-chain threat mitigation.

AOF Evidence dan Secure-SDLC profiles MAY consume SLSA provenance
sebagai evidence, tetapi:

\[ SLSAProvenance\neq AOFVerification\]

tanpa applicable AOF criteria/evaluation.

------------------------------------------------------------------------

## 23.12 in-toto

**REF-SUPPLY-002 --- in-toto**

in-toto melindungi software supply-chain integrity dengan
mendeskripsikan planned steps, authorized functionaries, dan signed
metadata/evidence mengenai performed steps.

Relevance:

-   authorized supply-chain steps;
-   provenance;
-   evidence chain;
-   signed metadata;
-   step verification.

Concepts ini merupakan clear prior art untuk software supply-chain
provenance/authorized-step verification. AOF tidak mengklaim novelty
atas konsep tersebut.

------------------------------------------------------------------------

## 23.13 Few-Shot Learning / Prompting

**REF-TECH-001 --- Brown et al., "Language Models are Few-Shot Learners"
(2020)**

Work ini menunjukkan large language models dapat melakukan tasks dari
textual instructions dan limited demonstrations tanpa task-specific
gradient updates.

Relevance terhadap AOF:

-   Few-Shot examples dalam Specification Contract;
-   prompt-level task conditioning.

Few-Shot adalah external technique, bukan AOF invention.

------------------------------------------------------------------------

## 23.14 Chain-of-Thought

**REF-TECH-002 --- Wei et al., "Chain-of-Thought Prompting Elicits
Reasoning in Large Language Models" (2022)**

Work ini menunjukkan intermediate reasoning demonstrations dapat
meningkatkan performance pada reasoning tasks.

Relevance:

-   reasoning technique lineage;
-   distinction antara reasoning method dan governed decision.

AOF tidak memerlukan disclosure/persistence private Chain-of-Thought
untuk Trace atau Conformance.

------------------------------------------------------------------------

## 23.15 ReAct

**REF-TECH-003 --- Yao et al., "ReAct: Synergizing Reasoning and Acting
in Language Models" (2022/2023)**

ReAct menginterleave reasoning traces dan task-specific actions sehingga
model dapat interact dengan external sources/environments.

Relevance:

-   Reasoning + Action technique;
-   tool/environment interaction;
-   observe/act cycles.

AOF memperlakukan ReAct sebagai optional technique di Reasoning/Agent
layer, bukan governance mechanism.

\[ ReAct\neq AuthorityModel\]

------------------------------------------------------------------------

## 23.16 Tree of Thoughts

**REF-TECH-004 --- Yao et al., "Tree of Thoughts: Deliberate Problem
Solving with Large Language Models" (2023)**

Tree of Thoughts mengeksplorasi multiple reasoning paths,
self-evaluation, lookahead, dan backtracking untuk problem solving.

Relevance:

-   EXPLORE technique;
-   planning/search;
-   alternative generation.

AOF tidak mengklaim invention ToT dan tidak menganggap ToT
self-evaluation equivalent dengan independent Verification.

------------------------------------------------------------------------

## 23.17 Retrieval-Augmented Generation

**REF-TECH-005 --- Lewis et al., "Retrieval-Augmented Generation for
Knowledge-Intensive NLP Tasks" (2020)**

RAG menggabungkan parametric language model dengan explicit
non-parametric retrieval.

Relevance:

-   external Context acquisition;
-   grounding;
-   source retrieval;
-   knowledge freshness.

AOF memperlakukan retrieved content sebagai Context/Evidence candidate
sesuai provenance dan trust rules.

\[ RetrievedContent\neq VerifiedFact\]

------------------------------------------------------------------------

## 23.18 Reflexion

**REF-TECH-006 --- Shinn et al., "Reflexion: Language Agents with Verbal
Reinforcement Learning" (2023)**

Reflexion menggunakan linguistic feedback dan episodic memory untuk
meningkatkan subsequent trials tanpa weight update.

Relevance:

-   Reflection;
-   failure learning;
-   retry improvement;
-   episodic memory.

AOF Failure & Recovery dan Learning Loop MAY menggunakan reflection
technique, tetapi governed retry/recovery semantics merupakan separate
control concern.

------------------------------------------------------------------------

## 23.19 Constitutional AI

**REF-ASSURE-001 --- Bai et al., "Constitutional AI: Harmlessness from
AI Feedback" (2022)**

Constitutional AI mengeksplorasi rule/principle-guided self-critique dan
AI feedback untuk training/alignment.

Relevance:

-   principle-guided behavior;
-   critique/revision;
-   AI-assisted evaluation.

AOF Policy enforcement berbeda secara fundamental dari
prompt/training-level behavioral guidance:

\[ PolicyPrompt\neq PolicyEnforcement\]

------------------------------------------------------------------------

## 23.20 Multi-Agent Prior Art

**REF-AGENT-001 --- CAMEL (Li et al., 2023)**

CAMEL mengeksplorasi role-playing dan autonomous cooperation antara
communicative agents.

**REF-AGENT-002 --- AutoGen (Wu et al., 2023)**

AutoGen mendeskripsikan multi-Agent conversation framework yang
menggabungkan LLMs, tools, Human participation, dan automated agent
chat.

Relevance:

-   multi-Agent orchestration;
-   role-based Agents;
-   inter-Agent communication;
-   Human feedback;
-   tool-enabled workflows.

AOF tidak mengklaim invention multi-Agent orchestration. Differentiation
AOF terletak pada explicit governance semantics, bounded Authority,
Policy mediation, Risk Gate, Evidence/Verification, State/Trace, and
Conformance model.

------------------------------------------------------------------------

## 23.21 Prior-Art Crosswalk

  ----------------------------------------------------------------------
  AOF Area               Relevant Prior Art /   AOF Position
                         Reference              
  ---------------------- ---------------------- ------------------------
  AI Risk                NIST AI RMF, NIST GAI  Adopt/align concepts;
                         Profile                AOF adds operational
                                                orchestration semantics

  AI Management          ISO/IEC 42001          Complementary
                                                organizational
                                                management layer

  Secure SDLC            NIST SSDF              Domain mapping/profile
                                                reference

  Agentic Security       OWASP GenAI/Agentic,   Security crosswalk and
                         MITRE ATLAS            threat enrichment

  Provenance             SLSA, in-toto          Prior art for
                                                provenance/attestation
                                                and supply-chain
                                                integrity

  Few-Shot               Brown et al.           Technique, not novelty

  Chain-of-Thought       Wei et al.             Technique, not
                                                governance

  ReAct                  Yao et al.             Technique, not
                                                Authority/Policy model

  Tree of Thoughts       Yao et al.             Exploration technique

  RAG                    Lewis et al.           Context/retrieval
                                                technique

  Reflection             Shinn et al.           Learning/reflection
                                                technique

  Principle-guided AI    Constitutional AI      Related behavioral
                                                governance/alignment
                                                approach

  Multi-Agent            CAMEL, AutoGen         Multi-Agent prior art
  ----------------------------------------------------------------------

------------------------------------------------------------------------

## 23.22 AOF Differentiation Boundary

Based on reviewed prior art, AOF SHOULD describe its contribution
conservatively sebagai integrated governance/orchestration framework
yang menggabungkan:

-   explicit `Capability != Authority`;
-   positive authorization;
-   bounded delegation;
-   Policy mediation;
-   Risk-proportional control;
-   Evidence admissibility/sufficiency;
-   Verification independence;
-   authoritative State;
-   Trace accountability;
-   governed Failure & Recovery;
-   controlled Effect Boundary;
-   cross-domain Security;
-   machine-readable contracts;
-   testable Conformance.

Presence dari individual concept di atas tidak otomatis novel. Potential
contribution berada pada specific composition, formal relationships,
invariant set, lifecycle integration, dan conformance architecture.

------------------------------------------------------------------------

## 23.23 Novelty Claim Policy

AOF v1.0 MUST NOT membuat strong legal/patent-style novelty claim hanya
berdasarkan literature review ini.

Claims SHOULD menggunakan wording seperti:

-   "AOF defines..."
-   "AOF formalizes..."
-   "AOF composes..."
-   "AOF introduces within this framework..."
-   "AOF proposes..."

dan SHOULD menghindari wording:

-   "first ever";
-   "unprecedented";
-   "unique in the field";
-   "novel" tanpa scoped evidence;
-   "invented by AOF" untuk established techniques.

------------------------------------------------------------------------

## 23.24 Research-Candidate Terms

Terms/concepts berikut tetap `Research Candidate` sampai broader
literature and empirical validation dilakukan:

-   `Orchestration Debt`;
-   any claim of `Authority Conservation` as novel terminology;
-   `Bounded Agency` as novel term;
-   `Governance Envelope` as novel term;
-   `Safety Kernel` as novel AI-orchestration term;
-   claims that AOF architecture is categorically unique;
-   quantitative claims about ROI, safety improvement, or failure
    reduction.

AOF MAY use these terms internally as defined constructs tanpa mengklaim
external novelty.

------------------------------------------------------------------------

## 23.25 Standards Relationship

AOF SHOULD diposisikan sebagai complementary orchestration
specification, bukan replacement untuk:

-   AI management standards;
-   cybersecurity standards;
-   secure software development frameworks;
-   privacy regulation;
-   sector-specific safety requirements;
-   software supply-chain standards.

Deployment MUST tetap memenuhi applicable legal/regulatory/contractual
obligations independently dari AOF conformance.

------------------------------------------------------------------------

## 23.26 Reference Stability

External references dapat berubah.

AOF release SHOULD pin reference version/date jika semantic mapping
bergantung pada specific edition.

Living frameworks seperti OWASP dan MITRE ATLAS SHOULD diperlakukan
sebagai versioned external dependencies untuk crosswalk purposes.

------------------------------------------------------------------------

## 23.27 Reference Update Policy

Patch/minor AOF release MAY memperbarui bibliographic metadata atau
non-normative crosswalk tanpa mengubah AOF semantics.

Jika external reference change menyebabkan AOF normative semantic
change, perubahan tersebut MUST mengikuti AOF compatibility/versioning
policy.

------------------------------------------------------------------------

## 23.28 Prior-Art Review Limitations

Review v1.0 RC-References adalah targeted prior-art review, bukan
exhaustive systematic literature review atau legal patent search.

Keterbatasan:

-   rapidly evolving Agentic AI field;
-   living security frameworks;
-   non-public/proprietary systems;
-   terminology fragmentation;
-   potential prior art di patents, standards drafts, workshops,
    repositories, dan industry systems yang belum included.

Karena itu, absence dari matching reference tidak membuktikan novelty.

------------------------------------------------------------------------

## 23.29 Reference Requirements

**AOF-REF-001** --- Established external techniques MUST NOT
dipresentasikan sebagai AOF invention.

**AOF-REF-002** --- External reference adopted untuk normative
dependency MUST memiliki identifiable version/edition.

**AOF-REF-003** --- AOF conformance MUST NOT diklaim equivalent dengan
external certification tanpa explicit mapping.

**AOF-REF-004** --- Prior-art differentiation claims MUST scoped dan
evidence-backed.

**AOF-REF-005** --- Living framework crosswalk SHOULD identify reviewed
version/date.

**AOF-REF-006** --- Research Candidate terminology MUST NOT menjadi
unsupported novelty claim.

**AOF-REF-007** --- External standard update MUST NOT silently alter AOF
normative semantics.

**AOF-REF-008** --- Final public release SHOULD publish authoritative
bibliography/crosswalk artifact.

------------------------------------------------------------------------

## 23.30 References/Prior-Art Freeze Candidate Criteria

Area ini MAY dinyatakan `Freeze Candidate` jika:

1.  core technique lineage documented;
2.  AI risk/governance references documented;
3.  Secure-SDLC references documented;
4.  Agentic security references documented;
5.  supply-chain/provenance references documented;
6.  multi-Agent prior art documented;
7.  novelty boundary explicit;
8.  Research Candidate terms isolated from novelty claims;
9.  external certification equivalence prohibited unless mapped;
10. bibliography versions sufficiently identifiable;
11. final cross-document consistency review confirms no unsupported
    novelty language.

------------------------------------------------------------------------

## 23.31 References/Prior-Art Formalization Result

References/Prior Art v1.0 RC-References diringkas sebagai:

\[ AOFContribution= Composition + Formalization +
GovernanceIntegration + CrossDomainContracts + Conformance \]

bukan:

\[ AOFContribution= InventionOfEstablishedTechniques \]

Canonical release position:

\[ \boxed{ PriorArt\ Must\ Be\ Acknowledged } \]

\[ \boxed{ Composition\ Claim\neq Novelty\ Claim } \]

\[
\boxed{ External\ Standard\ Alignment\neq Certification\ Equivalence }
\]

\[
\boxed{ Absence\ Of\ Known\ Prior\ Art\neq Proof\ Of\ Novelty }
# Appendix A --- Master Invariant Registry

## A.1 Public Canonical Registry

Tabel ini adalah public-reading registry. Mapping hanya dicantumkan
ketika explicit relationship dapat diturunkan dari Appendix F atau alias
domain yang telah direkonsiliasi. Absence of a direct mapping tidak
diisi secara heuristik.

  --------------------------------------------------------------------------------------------------------
  Canonical       Name                   Domain Aliases   Requirement       Primary /        Disposition
  Invariant                                               Mapping           Reference Test   
  --------------- ---------------------- ---------------- ----------------- ---------------- -------------
  `AOF-INV-001`   Plane Separation       `ARCH-INV-01`    No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-002`   Kernel Mediation       `ARCH-INV-02`    No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-003`   No Agent Root of Trust `ARCH-INV-03`    No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-004`   Effect Boundary        `ARCH-INV-04`    `AOF-ARCH-009`    No direct        Explicit
                  Validation                                                reference CT     mapping
                                                                            asserted         

  `AOF-INV-005`   State Authority        `AGT-INV-16`,    `AOF-ARCH-007`    No direct        Explicit
                                         `ARCH-INV-05`                      reference CT     mapping
                                                                            asserted         

  `AOF-INV-006`   State--Trace Coherence `ARCH-INV-06`    `AOF-ARCH-005`    No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-007`   No Implicit Allow      `ARCH-INV-07`,   No direct         No direct        Canonical
                                         `POL-INV-04`     Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-008`   Revocation Enforcement `ARCH-INV-08`,   `AOF-ARCH-012`,   No direct        Explicit
                                         `AUTH-INV-06`    `AOF-ARCH-015`,   reference CT     mapping
                                                          `AOF-AUTH-003`,   asserted         
                                                          `AOF-AUTH-016`                     

  `AOF-INV-009`   Context Non-Authority  `AGT-INV-05`,    `AOF-AGT-006`,    `CT-AGT-003`     Explicit
                                         `ARCH-INV-09`    `AOF-AGT-007`,                     mapping
                                                          `AOF-ARCH-006`,                    
                                                          `AOF-ARCH-008`                     

  `AOF-INV-010`   Tool Access            `ARCH-INV-10`    `AOF-ARCH-003`    No direct        Explicit
                  Non-Authority                                             reference CT     mapping
                                                                            asserted         

  `AOF-INV-011`   Evidence Return        `ARCH-INV-11`    `AOF-ARCH-017`    No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-012`   Controlled Concurrency `ARCH-INV-12`    `AOF-ARCH-001`,   No direct        Explicit
                                                          `AOF-ARCH-004`    reference CT     mapping
                                                                            asserted         

  `AOF-INV-013`   Proposal Non-Authority `LC-INV-01`      `AOF-LC-002`      No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-014`   Governed Effect        `LC-INV-02`      No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-015`   Pending Non-Permit     `LC-INV-03`      No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-016`   State Freshness        `LC-INV-04`      No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-017`   Verification Integrity `LC-INV-05`      `AOF-LC-007`,     `CT-LC-003`      Explicit
                                                          `AOF-LC-012`                       mapping

  `AOF-INV-018`   Failure Non-Bypass     `LC-INV-06`      `AOF-LC-008`      No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-019`   Effect Honesty         `LC-INV-07`      No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-020`   Retry Governance       `LC-INV-08`      `AOF-LC-003`,     `CT-LC-001`      Explicit
                                                          `AOF-LC-010`,                      mapping
                                                          `AOF-LC-016`                       

  `AOF-INV-021`   Replan Governance      `LC-INV-09`      `AOF-LC-011`      `CT-LC-001`      Explicit
                                                                                             mapping

  `AOF-INV-022`   Recovery Governance    `LC-INV-10`      No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-023`   Cancellation Honesty   `LC-INV-11`      `AOF-LC-013`,     No direct        Explicit
                                                          `AOF-LC-018`      reference CT     mapping
                                                                            asserted         

  `AOF-INV-024`   Successful Termination `LC-INV-12`      `AOF-LC-014`,     `CT-LC-009`      Explicit
                                                          `AOF-LC-015`                       mapping

  `AOF-INV-025`   Transition             `LC-INV-13`      `AOF-LC-001`,     `CT-LC-009`      Explicit
                  Traceability                            `AOF-LC-020`,                      mapping
                                                          `AOF-LC-023`                       

  `AOF-INV-026`   Resume Freshness       `LC-INV-14`      `AOF-LC-024`      No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-027`   Fail-Controlled Kernel `LC-INV-15`      `AOF-LC-005`,     `CT-LC-004`,     Explicit
                                                          `AOF-LC-009`      `CT-LC-009`      mapping

  `AOF-INV-028`   Human Approval         `LC-INV-16`      `AOF-LC-019`      No direct        Explicit
                  Integrity                                                 reference CT     mapping
                                                                            asserted         

  `AOF-INV-029`   Bounded Agency         `AGT-INV-01`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-030`   Capability-Authority   `AGT-INV-02`,    `AOF-AUTH-001`,   `CT-AUTH-001`    Explicit
                  Separation             `AUTH-INV-03`    `AOF-AUTH-004`,                    mapping
                                                          `AOF-AUTH-007`,                    
                                                          `AOF-AUTH-009`,                    
                                                          `AOF-AUTH-010`,                    
                                                          `AOF-AUTH-012`,                    
                                                          `AOF-AUTH-013`,                    
                                                          `AOF-AUTH-017`,                    
                                                          `AOF-AUTH-021`                     

  `AOF-INV-031`   Role-Authority         `AGT-INV-03`     `AOF-AGT-014`     No direct        Explicit
                  Separation                                                reference CT     mapping
                                                                            asserted         

  `AOF-INV-032`   No Self-Authorization  `AGT-INV-04`     `AOF-AGT-003`     `CT-AGT-009`     Explicit
                                                                                             mapping

  `AOF-INV-033`   Memory Non-Authority   `AGT-INV-06`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-034`   Trust Non-Authority    `AGT-INV-07`     `AOF-AGT-001`,    `CT-AGT-001`,    Explicit
                                                          `AOF-AGT-002`,    `CT-AGT-009`     mapping
                                                          `AOF-AGT-008`,                     
                                                          `AOF-AGT-009`,                     
                                                          `AOF-AGT-011`,                     
                                                          `AOF-AGT-013`                      

  `AOF-INV-035`   Confidence             `AGT-INV-08`     `AOF-AGT-017`     No direct        Explicit
                  Non-Verification                                          reference CT     mapping
                                                                            asserted         

  `AOF-INV-036`   Proposal Non-Decision  `AGT-INV-09`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-037`   Technical Access       `AGT-INV-10`     `AOF-AGT-010`,    `CT-AGT-004`,    Explicit
                  Non-Authority                           `AOF-AGT-018`,    `CT-AGT-009`     mapping
                                                          `AOF-AGT-021`                      

  `AOF-INV-038`   Delegation             `AGT-INV-11`,    `AOF-AGT-012`,    `CT-AGT-005`     Explicit
                  Conservation           `AUTH-INV-04`    `AOF-AGT-016`,                     mapping
                                                          `AOF-AGT-024`,                     
                                                          `AOF-AUTH-011`,                    
                                                          `AOF-AUTH-018`                     

  `AOF-INV-039`   No Authority           `AGT-INV-12`     No direct         No direct        Canonical
                  Laundering                              Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-040`   Execution/Disclosure   `AGT-INV-13`     `AOF-AGT-020`     No direct        Explicit
                  Separation                                                reference CT     mapping
                                                                            asserted         

  `AOF-INV-041`   Policy Enforcement     `AGT-INV-14`     `AOF-AGT-005`,    No direct        Explicit
                  Independence                            `AOF-AGT-015`     reference CT     mapping
                                                                            asserted         

  `AOF-INV-042`   Agent Non-Root         `AGT-INV-15`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-043`   Restart Freshness      `AGT-INV-17`     `AOF-AGT-019`     `CT-AGT-007`     Explicit
                                                                                             mapping

  `AOF-INV-044`   Verification           `AGT-INV-18`     No direct         No direct        Canonical
                  Independence                            Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-045`   Human Non-Omnipotence  `AGT-INV-19`,    No direct         No direct        Canonical
                                         `HG-INV-02`      Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-046`   Optimization Bound     `AGT-INV-20`     `AOF-AGT-023`     No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-047`   Authority Bound        `AUTH-INV-01`    No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-048`   Positive Authorization `AUTH-INV-02`    `AOF-AUTH-019`    `CT-AUTH-001`    Explicit
                                                                                             mapping

  `AOF-INV-049`   No Self-Elevation      `AUTH-INV-05`    `AOF-AUTH-014`    No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-050`   Policy Non-Creation    `AUTH-INV-07`    `AOF-AUTH-005`    No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-051`   Approval Non-Expansion `AUTH-INV-08`    `AOF-AUTH-006`    No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-052`   Information-Flow       `AUTH-INV-09`,   No direct         No direct        Canonical
                  Separation             `SEC-INV-11`     Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-053`   Replacement            `AUTH-INV-10`    `AOF-AUTH-015`    No direct        Explicit
                  Non-Inheritance                                           reference CT     mapping
                                                                            asserted         

  `AOF-INV-054`   Temporal Validity      `AUTH-INV-11`    No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-055`   Authority Provenance   `AUTH-INV-12`    `AOF-AUTH-008`    No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-056`   Policy Mediation       `POL-INV-01`     `AOF-POL-010`     No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-057`   Policy Non-Authority   `POL-INV-02`     `AOF-POL-006`,    `CT-POL-002`     Explicit
                                                          `AOF-POL-007`,                     mapping
                                                          `AOF-POL-011`,                     
                                                          `AOF-POL-013`                      

  `AOF-INV-058`   Restrictive Dominance  `POL-INV-03`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-059`   Policy Inheritance     `POL-INV-05`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-060`   Override Control       `POL-INV-06`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-061`   Prompt Non-Enforcement `POL-INV-07`,    `AOF-POL-005`     No direct        Explicit
                                         `SEC-INV-05`                       reference CT     mapping
                                                                            asserted         

  `AOF-INV-062`   Policy Version         `POL-INV-08`     `AOF-POL-003`,    No direct        Explicit
                  Traceability                            `AOF-POL-004`,    reference CT     mapping
                                                          `AOF-POL-014`,    asserted         
                                                          `AOF-POL-015`                      

  `AOF-INV-063`   Untrusted Context      `POL-INV-09`     `AOF-POL-002`     `CT-POL-002`     Explicit
                  Non-Mutation                                                               mapping

  `AOF-INV-064`   Replan Reevaluation    `POL-INV-10`     `AOF-POL-016`     No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-065`   Risk-Proportional      `RISK-INV-01`    No direct         No direct        Canonical
                  Control                                 Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-066`   Risk Non-Authority     `RISK-INV-02`    `AOF-RISK-001`,   No direct        Explicit
                                                          `AOF-RISK-011`,   reference CT     mapping
                                                          `AOF-RISK-014`    asserted         

  `AOF-INV-067`   Dynamic Reassessment   `RISK-INV-03`    No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-068`   Acceptance Separation  `RISK-INV-04`    No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-069`   Residual Risk          `RISK-INV-05`    `AOF-RISK-003`,   `CT-RISK-002`    Explicit
                  Accountability                          `AOF-RISK-008`                     mapping

  `AOF-INV-070`   High-Risk Assurance    `RISK-INV-06`    `AOF-RISK-006`,   `CT-RISK-001`    Explicit
                                                          `AOF-RISK-015`,                    mapping
                                                          `AOF-RISK-017`,                    
                                                          `AOF-RISK-018`                     

  `AOF-INV-071`   Critical-Risk          `RISK-INV-07`    `AOF-RISK-005`,   `CT-RISK-002`    Explicit
                  Governance                              `AOF-RISK-007`,                    mapping
                                                          `AOF-RISK-016`                     

  `AOF-INV-072`   No Stale Risk          `RISK-INV-08`    `AOF-RISK-012`    No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-073`   Partial Effect         `RISK-INV-09`    `AOF-RISK-009`,   No direct        Explicit
                  Reassessment                            `AOF-RISK-010`    reference CT     mapping
                                                                            asserted         

  `AOF-INV-074`   Cost Non-Dominance     `RISK-INV-10`    `AOF-RISK-004`    No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-075`   Provenance             `EVD-INV-01`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-076`   Claim Separation       `EVD-INV-02`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-077`   Verification           `EVD-INV-03`     `AOF-EVD-005`,    No direct        Explicit
                  Separation                              `AOF-EVD-013`,    reference CT     mapping
                                                          `AOF-EVD-014`,    asserted         
                                                          `AOF-EVD-017`                      

  `AOF-INV-078`   Sufficiency            `EVD-INV-04`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-079`   Freshness              `EVD-INV-05`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-080`   Contradiction          `EVD-INV-06`     `AOF-EVD-001`     No direct        Explicit
                  Visibility                                                reference CT     mapping
                                                                            asserted         

  `AOF-INV-081`   Derived Provenance     `EVD-INV-07`     `AOF-EVD-015`     No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-082`   No False Corroboration `EVD-INV-08`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-083`   Disclosure Control     `EVD-INV-09`     `AOF-EVD-011`     No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-084`   Historical             `EVD-INV-10`,    `AOF-EVD-002`,    No direct        Explicit
                  Preservation           `FR-INV-09`,     `AOF-EVD-009`,    reference CT     mapping
                                         `TRC-INV-04`     `AOF-EVD-012`,    asserted         
                                                          `AOF-FR-010`,                      
                                                          `AOF-TRC-010`,                     
                                                          `AOF-TRC-015`                      

  `AOF-INV-085`   Criteria Requirement   `VER-INV-01`     `AOF-VER-004`,    `CT-VER-001`     Explicit
                                                          `AOF-VER-005`,                     mapping
                                                          `AOF-VER-016`                      

  `AOF-INV-086`   Evidence Requirement   `VER-INV-02`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-087`   Inconclusive           `VER-INV-03`     No direct         No direct        Canonical
                  Non-Success                             Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-088`   Independence           `VER-INV-04`     `AOF-VER-015`     No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-089`   Subject Binding        `VER-INV-05`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-090`   Reverification         `VER-INV-06`     `AOF-VER-010`,    `CT-VER-002`     Explicit
                                                          `AOF-VER-012`,                     mapping
                                                          `AOF-VER-013`                      

  `AOF-INV-091`   Verification           `VER-INV-07`     `AOF-VER-002`,    `CT-VER-001`     Explicit
                  Non-Authority                           `AOF-VER-003`,                     mapping
                                                          `AOF-VER-011`                      

  `AOF-INV-092`   Verification           `VER-INV-08`     `AOF-VER-001`,    `CT-VER-001`     Explicit
                  Non-Approval                            `AOF-VER-006`,                     mapping
                                                          `AOF-VER-008`,                     
                                                          `AOF-VER-009`,                     
                                                          `AOF-VER-014`,                     
                                                          `AOF-VER-017`                      

  `AOF-INV-093`   Non-Circularity        `VER-INV-09`     `AOF-VER-007`     No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-094`   Completion Assurance   `VER-INV-10`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-095`   Authoritative State    `ST-INV-01`      `AOF-ST-001`      No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-096`   Controlled Mutation    `ST-INV-02`      `AOF-ST-002`,     No direct        Explicit
                                                          `AOF-ST-017`      reference CT     mapping
                                                                            asserted         

  `AOF-INV-097`   State Validity         `ST-INV-03`      No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-098`   Conflict Control       `ST-INV-04`      No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-099`   Replay Revalidation    `ST-INV-05`      `AOF-ST-010`,     No direct        Explicit
                                                          `AOF-ST-011`      reference CT     mapping
                                                                            asserted         

  `AOF-INV-100`   Partial Effect Honesty `FR-INV-03`,     `AOF-FR-003`,     `CT-STATE-002`   Explicit
                                         `ST-INV-06`      `AOF-FR-005`,                      mapping
                                                          `AOF-FR-015`,                      
                                                          `AOF-ST-005`,                      
                                                          `AOF-ST-007`,                      
                                                          `AOF-ST-008`                       

  `AOF-INV-101`   Replan Consistency     `ST-INV-07`      No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-102`   TOCTOU Control         `SEC-INV-07`,    No direct         No direct        Canonical
                                         `ST-INV-08`      Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-103`   Trace Completeness     `TRC-INV-01`     `AOF-TRC-005`,    No direct        Explicit
                                                          `AOF-TRC-009`,    reference CT     mapping
                                                          `AOF-TRC-011`     asserted         

  `AOF-INV-104`   Attribution            `TRC-INV-02`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-105`   Correlation            `TRC-INV-03`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-106`   Trace Integrity        `TRC-INV-05`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-107`   No Fabrication         `TRC-INV-06`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-108`   Trace Confidentiality  `TRC-INV-07`     `AOF-TRC-002`,    `CT-TRC-001`     Explicit
                                                          `AOF-TRC-003`,                     mapping
                                                          `AOF-TRC-014`                      

  `AOF-INV-109`   Chain-of-Thought       `TRC-INV-08`     `AOF-TRC-004`     No direct        Explicit
                  Independence                                              reference CT     mapping
                                                                            asserted         

  `AOF-INV-110`   Governance Root        `HG-INV-01`      `AOF-HG-001`,     No direct        Explicit
                                                          `AOF-HG-017`      reference CT     mapping
                                                                            asserted         

  `AOF-INV-111`   Intent Integrity       `HG-INV-03`      No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-112`   Delegation Bound       `HG-INV-04`      `AOF-HG-003`,     `CT-HG-007`      Explicit
                                                          `AOF-HG-004`                       mapping

  `AOF-INV-113`   Accountability         `HG-INV-05`      `AOF-HG-010`      `CT-HG-004`      Explicit
                  Persistence                                                                mapping

  `AOF-INV-114`   Approval Separation    `HG-INV-06`      `AOF-HG-006`,     No direct        Explicit
                                                          `AOF-HG-020`      reference CT     mapping
                                                                            asserted         

  `AOF-INV-115`   Approval Freshness     `HG-INV-07`      `AOF-HG-012`      `CT-HG-002`      Explicit
                                                                                             mapping

  `AOF-INV-116`   Override Governance    `HG-INV-08`      `AOF-HG-002`,     `CT-HG-005`      Explicit
                                                          `AOF-HG-008`,                      mapping
                                                          `AOF-HG-013`,                      
                                                          `AOF-HG-016`,                      
                                                          `AOF-HG-019`                       

  `AOF-INV-117`   Break-Glass            `HG-INV-09`      `AOF-HG-009`,     `CT-HG-006`      Explicit
                  Auditability                            `AOF-HG-014`,                      mapping
                                                          `AOF-HG-021`                       

  `AOF-INV-118`   No Fabricated Approval `HG-INV-10`      No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-119`   Risk Acceptance        `HG-INV-11`      `AOF-HG-007`,     `CT-HG-008`      Explicit
                  Separation                              `AOF-HG-018`,                      mapping
                                                          `AOF-HG-024`                       

  `AOF-INV-120`   Automation             `HG-INV-12`      `AOF-HG-005`      No direct        Explicit
                  Accountability                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-121`   Human Decision         `HG-INV-13`      `AOF-HG-011`,     `CT-HG-004`      Explicit
                  Fallibility                             `AOF-HG-015`,                      mapping
                                                          `AOF-HG-022`                       

  `AOF-INV-122`   Policy Integrity       `HG-INV-14`      No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-123`   Controlled Failure     `FR-INV-01`      `AOF-FR-014`,     No direct        Explicit
                                                          `AOF-FR-020`      reference CT     mapping
                                                                            asserted         

  `AOF-INV-124`   No Blind Retry         `FR-INV-02`      No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-125`   Recovery Authority     `FR-INV-04`      `AOF-FR-008`,     No direct        Explicit
                                                          `AOF-FR-017`      reference CT     mapping
                                                                            asserted         

  `AOF-INV-126`   Recovery Verification  `FR-INV-05`      `AOF-FR-006`,     `CT-FR-001`      Explicit
                                                          `AOF-FR-007`,                      mapping
                                                          `AOF-FR-016`,                      
                                                          `AOF-FR-019`                       

  `AOF-INV-127`   Bounded Retry          `FR-INV-06`      `AOF-FR-009`      `CT-FR-002`      Explicit
                                                                                             mapping

  `AOF-INV-128`   Safety Kernel          `FR-INV-07`      `AOF-FR-001`,     `CT-FR-002`      Explicit
                  Fail-Controlled                         `AOF-FR-004`                       mapping

  `AOF-INV-129`   Escalation             `FR-INV-08`      `AOF-FR-011`,     `CT-FR-002`      Explicit
                  Non-Resolution                          `AOF-FR-012`                       mapping

  `AOF-INV-130`   Goal Integrity Under   `FR-INV-10`      `AOF-FR-002`      No direct        Explicit
                  Replan                                                    reference CT     mapping
                                                                            asserted         

  `AOF-INV-131`   Untrusted Content      `SEC-INV-01`     `AOF-SEC-005`,    `CT-SEC-001`     Explicit
                  Non-Authority                           `AOF-SEC-016`                      mapping

  `AOF-INV-132`   Agent                  `SEC-INV-02`     No direct         No direct        Canonical
                  Non-Root-of-Trust                       Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-133`   Safety Kernel          `SEC-INV-03`     `AOF-SEC-003`     No direct        Explicit
                  Non-Bypass                                                reference CT     mapping
                                                                            asserted         

  `AOF-INV-134`   Credential             `SEC-INV-04`     `AOF-SEC-006`,    No direct        Explicit
                  Non-Authority                           `AOF-SEC-010`,    reference CT     mapping
                                                          `AOF-SEC-012`     asserted         

  `AOF-INV-135`   Context Least          `SEC-INV-06`     `AOF-SEC-002`     No direct        Explicit
                  Privilege                                                 reference CT     mapping
                                                                            asserted         

  `AOF-INV-136`   Replay Control         `SEC-INV-08`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-137`   Evidence/Trace         `SEC-INV-09`     `AOF-SEC-011`,    No direct        Explicit
                  Integrity                               `AOF-SEC-018`     reference CT     mapping
                                                                            asserted         

  `AOF-INV-138`   Fail-Controlled        `SEC-INV-10`     `AOF-SEC-014`,    No direct        Explicit
                  Security                                `AOF-SEC-022`     reference CT     mapping
                                                                            asserted         

  `AOF-INV-139`   Security Recovery      `SEC-INV-12`     `AOF-SEC-008`     No direct        Explicit
                  Governance                                                reference CT     mapping
                                                                            asserted         

  `AOF-INV-140`   Requirement            `CONF-INV-01`    `AOF-CONF-005`    No direct        Explicit
                  Traceability                                              reference CT     mapping
                                                                            asserted         

  `AOF-INV-141`   Evidence               `CONF-INV-02`    No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-142`   No Inconclusive        `CONF-INV-03`    No direct         No direct        Canonical
                  Success                                 Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-143`   Mandatory Violation    `CONF-INV-04`    No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-144`   Scope Integrity        `CONF-INV-05`    No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-145`   Version Integrity      `CONF-INV-06`,   No direct         No direct        Canonical
                                         `SCH-INV-06`     Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-146`   Profile Inheritance    `CONF-INV-07`    `AOF-CONF-007`,   No direct        Explicit
                                                          `AOF-CONF-009`,   reference CT     mapping
                                                          `AOF-CONF-017`,   asserted         
                                                          `AOF-CONF-022`                     

  `AOF-INV-147`   Schema Non-Sufficiency `CONF-INV-08`    `AOF-CONF-004`    No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-148`   No Chain-of-Thought    `CONF-INV-09`    `AOF-CONF-002`,   No direct        Explicit
                  Requirement                             `AOF-CONF-003`    reference CT     mapping
                                                                            asserted         

  `AOF-INV-149`   Conformance            `CONF-INV-10`    `AOF-CONF-001`,   No direct        Explicit
                  Non-Zero-Risk                           `AOF-CONF-006`,   reference CT     mapping
                                                          `AOF-CONF-008`,   asserted         
                                                          `AOF-CONF-010`,                    
                                                          `AOF-CONF-013`,                    
                                                          `AOF-CONF-015`,                    
                                                          `AOF-CONF-018`,                    
                                                          `AOF-CONF-019`,                    
                                                          `AOF-CONF-020`                     

  `AOF-INV-150`   Construct Separation   `SCH-INV-01`     `AOF-SCH-011`,    No direct        Explicit
                                                          `AOF-SCH-014`     reference CT     mapping
                                                                            asserted         

  `AOF-INV-151`   Structural             `SCH-INV-02`     No direct         No direct        Canonical
                  Non-Authority                           Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-152`   Structural             `SCH-INV-03`     `AOF-SCH-007`,    No direct        Explicit
                  Non-Conformance                         `AOF-SCH-018`     reference CT     mapping
                                                                            asserted         

  `AOF-INV-153`   Safe Unknown           `SCH-INV-04`     No direct         No direct        Canonical
                                                          Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-154`   Reference Integrity    `SCH-INV-05`     `AOF-SCH-002`,    No direct        Explicit
                                                          `AOF-SCH-003`,    reference CT     mapping
                                                          `AOF-SCH-012`     asserted         

  `AOF-INV-155`   Extension Non-Override `SCH-INV-07`     `AOF-SCH-013`     No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-156`   Migration Preservation `SCH-INV-08`     `AOF-SCH-001`,    No direct        Explicit
                                                          `AOF-SCH-009`,    reference CT     mapping
                                                          `AOF-SCH-015`,    asserted         
                                                          `AOF-SCH-016`,                     
                                                          `AOF-SCH-021`                      

  `AOF-INV-157`   Decision Traceability  `SCH-INV-09`     `AOF-SCH-005`     No direct        Explicit
                                                                            reference CT     mapping
                                                                            asserted         

  `AOF-INV-158`   No Private Reasoning   `SCH-INV-10`     No direct         No direct        Canonical
                  Requirement                             Requirement       reference CT     invariant;
                                                          mapping asserted  asserted         direct trace
                                                                                             link not
                                                                                             asserted

  `AOF-INV-159`   Core Preservation      `PRF-INV-01`     No direct         `CT-PRF-001`     Explicit
                                                          Requirement                        mapping
                                                          mapping asserted                   

  `AOF-INV-160`   No Profile Weakening   `PRF-INV-02`     No direct         `CT-PRF-003`     Explicit
                                                          Requirement                        mapping
                                                          mapping asserted                   

  `AOF-INV-161`   Explicit Claim         `PRF-INV-03`     No direct         `CT-PRF-004`     Explicit
                                                          Requirement                        mapping
                                                          mapping asserted                   

  `AOF-INV-162`   Domain Profile         `PRF-INV-04`     No direct         `CT-PRF-002`     Explicit
                  Non-Linearity                           Requirement                        mapping
                                                          mapping asserted                   
  --------------------------------------------------------------------------------------------------------

### AOF-INV-001 --- Plane Separation

**Domain Alias(es):** `ARCH-INV-01`.

**Enforcement:** Architecture / Safety Kernel.

**Canonical/source formula:**

\[ RP\neq CP\neq EP\neq AP\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-002 --- Kernel Mediation

**Domain Alias(es):** `ARCH-INV-02`.

**Enforcement:** Architecture / Safety Kernel.

**Canonical/source formula:**

\[ Consequential(x)\Rightarrow MediatedBy(K,x) \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-003 --- No Agent Root of Trust

**Domain Alias(es):** `ARCH-INV-03`.

**Enforcement:** Architecture / Safety Kernel.

**Canonical/source formula:**

\[ Agent\not\supset eq GovernanceRoot\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-004 --- Effect Boundary Validation

**Domain Alias(es):** `ARCH-INV-04`.

**Enforcement:** Architecture / Safety Kernel.

**Canonical/source formula:**

\[ Effect(x)\Rightarrow ValidControlDecision(x) \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-005 --- State Authority

**Domain Alias(es):** `ARCH-INV-05`, `AGT-INV-16`.

**Enforcement:** Architecture / Safety Kernel; Agent Model /
Orchestrator.

**Canonical/source formula:**

\[ ConsequentialState\neq UncontrolledAgentPrivateState\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-006 --- State--Trace Coherence

**Domain Alias(es):** `ARCH-INV-06`.

**Enforcement:** Architecture / Safety Kernel.

**Canonical/source formula:**

\[ StateChange\Rightarrow TraceRecord\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-007 --- No Implicit Allow

**Domain Alias(es):** `ARCH-INV-07`, `POL-INV-04`.

**Enforcement:** Architecture / Safety Kernel; Policy Evaluator.

**Canonical/source formula:**

\[ UnknownMandatoryControl\Rightarrow\neg Permit\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-008 --- Revocation Enforcement

**Domain Alias(es):** `ARCH-INV-08`, `AUTH-INV-06`.

**Enforcement:** Architecture / Safety Kernel; Authority Evaluator.

**Canonical/source formula:**

\[ Revoked(h)\Rightarrow\neg NewExecutionUsing(h) \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-009 --- Context Non-Authority

**Domain Alias(es):** `ARCH-INV-09`, `AGT-INV-05`.

**Enforcement:** Architecture / Safety Kernel; Agent Model /
Orchestrator.

**Canonical/source formula:**

\[ ContextContent\not\Rightarrow ControlAuthority\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-010 --- Tool Access Non-Authority

**Domain Alias(es):** `ARCH-INV-10`.

**Enforcement:** Architecture / Safety Kernel.

**Canonical/source formula:**

\[ ToolReachability\not\Rightarrow AuthorizedUse\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-011 --- Evidence Return

**Domain Alias(es):** `ARCH-INV-11`.

**Enforcement:** Architecture / Safety Kernel.

**Source-derived statement:** sesuai applicable evidence requirements.

**Canonical/source formula:**

\[ ConsequentialEffect\Rightarrow ObservableResult\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-012 --- Controlled Concurrency

**Domain Alias(es):** `ARCH-INV-12`.

**Enforcement:** Architecture / Safety Kernel.

## **Source-derived statement:**

**Canonical/source formula:**

\[ ConcurrentConsequentialCommit\Rightarrow ConflictControlled\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-013 --- Proposal Non-Authority

**Domain Alias(es):** `LC-INV-01`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[ Proposal\not\Rightarrow Action\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-014 --- Governed Effect

**Domain Alias(es):** `LC-INV-02`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[ ConsequentialEffect\Rightarrow GovernedTransition\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-015 --- Pending Non-Permit

**Domain Alias(es):** `LC-INV-03`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[ Pending\neq Pass\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-016 --- State Freshness

**Domain Alias(es):** `LC-INV-04`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[ MaterialStateChange\Rightarrow ReevaluateDecision\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-017 --- Verification Integrity

**Domain Alias(es):** `LC-INV-05`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[ Inconclusive\neq Verified\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-018 --- Failure Non-Bypass

**Domain Alias(es):** `LC-INV-06`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[ Failure\neq PermissionToBypassControl\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-019 --- Effect Honesty

**Domain Alias(es):** `LC-INV-07`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[ FailedAction\not\Rightarrow NoEffect\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-020 --- Retry Governance

**Domain Alias(es):** `LC-INV-08`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[ Retry\Rightarrow ReevaluateEligibility\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-021 --- Replan Governance

**Domain Alias(es):** `LC-INV-09`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[ Replan\not\Rightarrow PreserveOldPermit\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-022 --- Recovery Governance

**Domain Alias(es):** `LC-INV-10`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[ RecoveryAction\Rightarrow GovernedAction\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-023 --- Cancellation Honesty

**Domain Alias(es):** `LC-INV-11`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[ Cancel\neq Rollback\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-024 --- Successful Termination

**Domain Alias(es):** `LC-INV-12`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[
Completed\Rightarrow GoalSatisfied\land RequiredAssuranceSatisfied
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-025 --- Transition Traceability

**Domain Alias(es):** `LC-INV-13`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[ ConsequentialTransition\Rightarrow TraceRecord\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-026 --- Resume Freshness

**Domain Alias(es):** `LC-INV-14`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[ Resume\not\Rightarrow ReuseStalePermit\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-027 --- Fail-Controlled Kernel

**Domain Alias(es):** `LC-INV-15`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

**Canonical/source formula:**

\[ MandatoryControlFailure\Rightarrow\neg ImplicitPermit
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-028 --- Human Approval Integrity

**Domain Alias(es):** `LC-INV-16`.

**Enforcement:** Orchestration Lifecycle / Control Plane.

## **Source-derived statement:**

**Canonical/source formula:**

\[ HumanUnavailable\not\Rightarrow Approved\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-029 --- Bounded Agency

**Domain Alias(es):** `AGT-INV-01`.

**Enforcement:** Agent Model / Orchestrator.

**Canonical/source formula:**

\[ Agency(a)\subset eq GovernanceEnvelope(a) \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-030 --- Capability-Authority Separation

**Domain Alias(es):** `AGT-INV-02`, `AUTH-INV-03`.

**Enforcement:** Agent Model / Orchestrator; Authority Evaluator.

**Canonical/source formula:**

\[ Capability\neq Authority\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-031 --- Role-Authority Separation

**Domain Alias(es):** `AGT-INV-03`.

**Enforcement:** Agent Model / Orchestrator.

**Canonical/source formula:**

\[ Role\neq Authority\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-032 --- No Self-Authorization

**Domain Alias(es):** `AGT-INV-04`.

**Enforcement:** Agent Model / Orchestrator.

**Canonical/source formula:**

\[ SelfDeclaredAuthority\neq EffectiveAuthority\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-033 --- Memory Non-Authority

**Domain Alias(es):** `AGT-INV-06`.

**Enforcement:** Agent Model / Orchestrator.

**Canonical/source formula:**

\[ Memory\neq Authority\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-034 --- Trust Non-Authority

**Domain Alias(es):** `AGT-INV-07`.

**Enforcement:** Agent Model / Orchestrator.

**Canonical/source formula:**

\[ TrustIncrease\not\Rightarrow AuthorityIncrease\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-035 --- Confidence Non-Verification

**Domain Alias(es):** `AGT-INV-08`.

**Enforcement:** Agent Model / Orchestrator.

**Canonical/source formula:**

\[ Confidence\neq Verification\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-036 --- Proposal Non-Decision

**Domain Alias(es):** `AGT-INV-09`.

**Enforcement:** Agent Model / Orchestrator.

**Canonical/source formula:**

\[ AgentOutput\neq AuthorizedDecision\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-037 --- Technical Access Non-Authority

**Domain Alias(es):** `AGT-INV-10`.

**Enforcement:** Agent Model / Orchestrator.

**Canonical/source formula:**

\[ TechnicalAccess\neq Authority\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-038 --- Delegation Conservation

**Domain Alias(es):** `AGT-INV-11`, `AUTH-INV-04`.

**Enforcement:** Agent Model / Orchestrator; Authority Evaluator.

**Source-derived statement:** untuk inherited delegated Authority.

**Canonical/source formula:**

\[ Authority\_{delegatee}\subset eq Authority\_{delegator} \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-039 --- No Authority Laundering

**Domain Alias(es):** `AGT-INV-12`.

**Enforcement:** Agent Model / Orchestrator.

**Canonical/source formula:**

\[ DelegationChain\not\Rightarrow PrivilegeExpansion\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-040 --- Execution/Disclosure Separation

**Domain Alias(es):** `AGT-INV-13`.

**Enforcement:** Agent Model / Orchestrator.

**Canonical/source formula:**

\[ ExecutionAuthority\neq DisclosureAuthority\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-041 --- Policy Enforcement Independence

**Domain Alias(es):** `AGT-INV-14`.

**Enforcement:** Agent Model / Orchestrator.

**Canonical/source formula:**

\[ PolicyPrompt\neq PolicyEnforcement\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-042 --- Agent Non-Root

**Domain Alias(es):** `AGT-INV-15`.

**Enforcement:** Agent Model / Orchestrator.

**Canonical/source formula:**

\[ AIAgent\not\Rightarrow GovernanceRoot\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-043 --- Restart Freshness

**Domain Alias(es):** `AGT-INV-17`.

**Enforcement:** Agent Model / Orchestrator.

**Canonical/source formula:**

\[ AgentRestart\not\Rightarrow ReuseStalePermit\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-044 --- Verification Independence

**Domain Alias(es):** `AGT-INV-18`.

**Enforcement:** Agent Model / Orchestrator.

**Canonical/source formula:**

\[ SelfCheck\neq IndependentVerification\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-045 --- Human Non-Omnipotence

**Domain Alias(es):** `AGT-INV-19`, `HG-INV-02`.

**Enforcement:** Agent Model / Orchestrator; Human Governance / Control
Plane.

**Canonical/source formula:**

\[ HumanPresence\not\Rightarrow UnlimitedAuthority\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-046 --- Optimization Bound

**Domain Alias(es):** `AGT-INV-20`.

**Enforcement:** Agent Model / Orchestrator.

## **Source-derived statement:**

**Canonical/source formula:**

\[
UtilityOptimization\not\Rightarrow GovernanceWeakening
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-047 --- Authority Bound

**Domain Alias(es):** `AUTH-INV-01`.

**Enforcement:** Authority Evaluator.

**Canonical/source formula:**

\[ Execute(a,x)\Rightarrow Authorized(a,x) \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-048 --- Positive Authorization

**Domain Alias(es):** `AUTH-INV-02`.

**Enforcement:** Authority Evaluator.

**Canonical/source formula:**

\[ NoGrant\Rightarrow NoAuthoritySensitiveExecution\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-049 --- No Self-Elevation

**Domain Alias(es):** `AUTH-INV-05`.

**Enforcement:** Authority Evaluator.

**Canonical/source formula:**

\[ AgentReasoning\not\Rightarrow AuthorityIncrease\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-050 --- Policy Non-Creation

**Domain Alias(es):** `AUTH-INV-07`.

**Enforcement:** Authority Evaluator.

**Canonical/source formula:**

\[ PolicyAllow\not\Rightarrow AuthorityGrant\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-051 --- Approval Non-Expansion

**Domain Alias(es):** `AUTH-INV-08`.

**Enforcement:** Authority Evaluator.

**Canonical/source formula:**

\[ Approval\not\Rightarrow UnlimitedAuthority\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-052 --- Information-Flow Separation

**Domain Alias(es):** `AUTH-INV-09`, `SEC-INV-11`.

**Enforcement:** Authority Evaluator; Security Controls / Safety Kernel.

**Canonical/source formula:**

\[ ReadAuthority\not\Rightarrow DisclosureAuthority\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-053 --- Replacement Non-Inheritance

**Domain Alias(es):** `AUTH-INV-10`.

**Enforcement:** Authority Evaluator.

**Canonical/source formula:**

\[
Replace(a_i,a_j)\not\Rightarrow InheritAuthority(a_j,a_i)
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-054 --- Temporal Validity

**Domain Alias(es):** `AUTH-INV-11`.

**Enforcement:** Authority Evaluator.

**Canonical/source formula:**

\[ Expired(h)\Rightarrow\neg Usable(h) \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-055 --- Authority Provenance

**Domain Alias(es):** `AUTH-INV-12`.

**Enforcement:** Authority Evaluator.

## **Source-derived statement:**

**Canonical/source formula:**

\[ ConsequentialAuthorityUse\Rightarrow TraceableAuthorityBasis
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-056 --- Policy Mediation

**Domain Alias(es):** `POL-INV-01`.

**Enforcement:** Policy Evaluator.

**Canonical/source formula:**

\[ Consequential(x)\Rightarrow PolicyEvaluated(x) \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-057 --- Policy Non-Authority

**Domain Alias(es):** `POL-INV-02`.

**Enforcement:** Policy Evaluator.

**Canonical/source formula:**

\[ PolicyAllow\not\Rightarrow AuthorityGrant\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-058 --- Restrictive Dominance

**Domain Alias(es):** `POL-INV-03`.

**Enforcement:** Policy Evaluator.

**Source-derived statement:** secara default.

**Canonical/source formula:**

\[ Conflict(P)\Rightarrow DeterministicRestrictiveResolution\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-059 --- Policy Inheritance

**Domain Alias(es):** `POL-INV-05`.

**Enforcement:** Policy Evaluator.

**Canonical/source formula:**

\[ ChildTask\Rightarrow PreserveApplicableMandatoryPolicy\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-060 --- Override Control

**Domain Alias(es):** `POL-INV-06`.

**Enforcement:** Policy Evaluator.

**Canonical/source formula:**

\[
Override(p)\Rightarrow Authorized\land Scoped\land Traceable
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-061 --- Prompt Non-Enforcement

**Domain Alias(es):** `POL-INV-07`, `SEC-INV-05`.

**Enforcement:** Policy Evaluator; Security Controls / Safety Kernel.

**Canonical/source formula:**

\[ PromptPolicy\not\equiv EnforcedPolicy\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-062 --- Policy Version Traceability

**Domain Alias(es):** `POL-INV-08`.

**Enforcement:** Policy Evaluator.

**Canonical/source formula:**

\[ ConsequentialDecision\Rightarrow TraceablePolicyVersion\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-063 --- Untrusted Context Non-Mutation

**Domain Alias(es):** `POL-INV-09`.

**Enforcement:** Policy Evaluator.

**Canonical/source formula:**

\[ UntrustedContent\not\Rightarrow PolicyMutation\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-064 --- Replan Reevaluation

**Domain Alias(es):** `POL-INV-10`.

**Enforcement:** Policy Evaluator.

## **Source-derived statement:**

**Canonical/source formula:**

\[ MaterialPolicyScopeChange\Rightarrow ReevaluatePolicy\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-065 --- Risk-Proportional Control

**Domain Alias(es):** `RISK-INV-01`.

**Enforcement:** Risk Gate.

**Canonical/source formula:**

\[
Risk\uparrow\Rightarrow ControlStrength\uparrow
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-066 --- Risk Non-Authority

**Domain Alias(es):** `RISK-INV-02`.

**Enforcement:** Risk Gate.

**Canonical/source formula:**

\[ RiskResult\not\Rightarrow Authority\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-067 --- Dynamic Reassessment

**Domain Alias(es):** `RISK-INV-03`.

**Enforcement:** Risk Gate.

**Canonical/source formula:**

\[ MaterialRiskTrigger\Rightarrow Reassess\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-068 --- Acceptance Separation

**Domain Alias(es):** `RISK-INV-04`.

**Enforcement:** Risk Gate.

**Canonical/source formula:**

\[ AssessRisk\neq AcceptRisk\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-069 --- Residual Risk Accountability

**Domain Alias(es):** `RISK-INV-05`.

**Enforcement:** Risk Gate.

**Canonical/source formula:**

\[ AcceptedResidualRisk\Rightarrow AuthorizedAcceptance\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-070 --- High-Risk Assurance

**Domain Alias(es):** `RISK-INV-06`.

**Enforcement:** Risk Gate.

**Source-derived statement:** sesuai reference profile.

**Canonical/source formula:**

\[ HighRisk\Rightarrow IndependentVerification\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-071 --- Critical-Risk Governance

**Domain Alias(es):** `RISK-INV-07`.

**Enforcement:** Risk Gate.

**Source-derived statement:** sesuai reference profile.

**Canonical/source formula:**

\[
CriticalRisk\Rightarrow IndependentVerification\land ExplicitApproval
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-072 --- No Stale Risk

**Domain Alias(es):** `RISK-INV-08`.

**Enforcement:** Risk Gate.

**Canonical/source formula:**

\[
MaterialContextChange\Rightarrow\neg BlindReuse(RiskAssessment)
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-073 --- Partial Effect Reassessment

**Domain Alias(es):** `RISK-INV-09`.

**Enforcement:** Risk Gate.

**Canonical/source formula:**

\[ PartialEffect\Rightarrow Reconcile+Reassess \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-074 --- Cost Non-Dominance

**Domain Alias(es):** `RISK-INV-10`.

**Enforcement:** Risk Gate.

## **Source-derived statement:**

**Canonical/source formula:**

\[
CostOptimization\not\Rightarrow MandatoryControlRemoval
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-075 --- Provenance

**Domain Alias(es):** `EVD-INV-01`.

**Enforcement:** Evidence / Assurance Plane.

**Canonical/source formula:**

\[ ConsequentialEvidence\Rightarrow Provenance\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-076 --- Claim Separation

**Domain Alias(es):** `EVD-INV-02`.

**Enforcement:** Evidence / Assurance Plane.

**Canonical/source formula:**

\[ Claim\neq Evidence\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-077 --- Verification Separation

**Domain Alias(es):** `EVD-INV-03`.

**Enforcement:** Evidence / Assurance Plane.

**Canonical/source formula:**

\[ Evidence\neq Verification\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-078 --- Sufficiency

**Domain Alias(es):** `EVD-INV-04`.

**Enforcement:** Evidence / Assurance Plane.

**Canonical/source formula:**

\[ EvidencePresent\not\Rightarrow EvidenceSufficient\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-079 --- Freshness

**Domain Alias(es):** `EVD-INV-05`.

**Enforcement:** Evidence / Assurance Plane.

**Canonical/source formula:**

\[
Stale(e)\land FreshRequired\Rightarrow\neg Sufficient(e)
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-080 --- Contradiction Visibility

**Domain Alias(es):** `EVD-INV-06`.

**Enforcement:** Evidence / Assurance Plane.

**Canonical/source formula:**

\[ MaterialContradiction\Rightarrow VisibleToVerification\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-081 --- Derived Provenance

**Domain Alias(es):** `EVD-INV-07`.

**Enforcement:** Evidence / Assurance Plane.

**Canonical/source formula:**

\[ DerivedEvidence\Rightarrow SourceReference\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-082 --- No False Corroboration

**Domain Alias(es):** `EVD-INV-08`.

**Enforcement:** Evidence / Assurance Plane.

**Canonical/source formula:**

\[
SameUnderlyingSource\not\Rightarrow IndependentCorroboration
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-083 --- Disclosure Control

**Domain Alias(es):** `EVD-INV-09`.

**Enforcement:** Evidence / Assurance Plane.

**Canonical/source formula:**

\[ EvidenceAccess\not\Rightarrow EvidenceDisclosure\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-084 --- Historical Preservation

**Domain Alias(es):** `EVD-INV-10`, `TRC-INV-04`, `FR-INV-09`.

**Enforcement:** Evidence / Assurance Plane; Trace Recorder; Failure &
Recovery Control.

## **Source-derived statement:**

**Canonical/source formula:**

\[ Correction(e)\Rightarrow SupersessionOrTrace\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-085 --- Criteria Requirement

**Domain Alias(es):** `VER-INV-01`.

**Enforcement:** Verification Gate.

**Canonical/source formula:**

\[ Verification\Rightarrow Criteria\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-086 --- Evidence Requirement

**Domain Alias(es):** `VER-INV-02`.

**Enforcement:** Verification Gate.

**Canonical/source formula:**

\[ Verified(c)\Rightarrow SufficientAdmissibleEvidence(c) \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-087 --- Inconclusive Non-Success

**Domain Alias(es):** `VER-INV-03`.

**Enforcement:** Verification Gate.

**Canonical/source formula:**

\[ Inconclusive\not\Rightarrow Verified\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-088 --- Independence

**Domain Alias(es):** `VER-INV-04`.

**Enforcement:** Verification Gate.

**Canonical/source formula:**

\[ IndependentVerificationRequired \Rightarrow
SelfVerificationInsufficient \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-089 --- Subject Binding

**Domain Alias(es):** `VER-INV-05`.

**Enforcement:** Verification Gate.

**Source-derived statement:** untuk materially different subject (y).

**Canonical/source formula:**

\[ Verified(x)\not\Rightarrow Verified(y) \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-090 --- Reverification

**Domain Alias(es):** `VER-INV-06`.

**Enforcement:** Verification Gate.

**Canonical/source formula:**

\[ MaterialSubjectChange\Rightarrow Reverify\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-091 --- Verification Non-Authority

**Domain Alias(es):** `VER-INV-07`.

**Enforcement:** Verification Gate.

**Canonical/source formula:**

\[ Verified\not\Rightarrow Authorized\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-092 --- Verification Non-Approval

**Domain Alias(es):** `VER-INV-08`.

**Enforcement:** Verification Gate.

**Canonical/source formula:**

\[ Verified\not\Rightarrow Approved\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-093 --- Non-Circularity

**Domain Alias(es):** `VER-INV-09`.

**Enforcement:** Verification Gate.

**Canonical/source formula:**

\[ Verification\not\Rightarrow PureSelfReference\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-094 --- Completion Assurance

**Domain Alias(es):** `VER-INV-10`.

**Enforcement:** Verification Gate.

## **Source-derived statement:**

**Canonical/source formula:**

\[ SuccessfulCompletion \Rightarrow
RequiredVerificationSatisfied \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-095 --- Authoritative State

**Domain Alias(es):** `ST-INV-01`.

**Enforcement:** State Validator.

**Canonical/source formula:**

\[ AuthoritativeState\neq AgentPrivateMemory\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-096 --- Controlled Mutation

**Domain Alias(es):** `ST-INV-02`.

**Enforcement:** State Validator.

**Canonical/source formula:**

\[ ConsequentialStateChange\Rightarrow ControlledTransition\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-097 --- State Validity

**Domain Alias(es):** `ST-INV-03`.

**Enforcement:** State Validator.

**Canonical/source formula:**

\[ Commit(\Delta)\Rightarrow StateValid(\Delta)
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-098 --- Conflict Control

**Domain Alias(es):** `ST-INV-04`.

**Enforcement:** State Validator.

**Canonical/source formula:**

\[ ConcurrentConflict\Rightarrow NoSilentCommit\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-099 --- Replay Revalidation

**Domain Alias(es):** `ST-INV-05`.

**Enforcement:** State Validator.

**Canonical/source formula:**

\[ ReplayWithEffect\Rightarrow CurrentControlValidation\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-100 --- Partial Effect Honesty

**Domain Alias(es):** `ST-INV-06`, `FR-INV-03`.

**Enforcement:** State Validator; Failure & Recovery Control.

**Canonical/source formula:**

\[ PartialEffect\not\Rightarrow AtomicSuccess\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-101 --- Replan Consistency

**Domain Alias(es):** `ST-INV-07`.

**Enforcement:** State Validator.

**Canonical/source formula:**

\[ MaterialReplan\Rightarrow ReevaluateAffectedState\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-102 --- TOCTOU Control

**Domain Alias(es):** `ST-INV-08`, `SEC-INV-07`.

**Enforcement:** State Validator; Security Controls / Safety Kernel.

**Source-derived statement:** sesuai profile/risk.

**Canonical/source formula:**

\[ MaterialStateChange\Rightarrow RevalidateBeforeEffect\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-103 --- Trace Completeness

**Domain Alias(es):** `TRC-INV-01`.

**Enforcement:** Trace Recorder.

**Canonical/source formula:**

\[ ConsequentialTransition\Rightarrow SufficientTrace\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-104 --- Attribution

**Domain Alias(es):** `TRC-INV-02`.

**Enforcement:** Trace Recorder.

**Canonical/source formula:**

\[ ConsequentialEvent\Rightarrow IdentifiableActor\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-105 --- Correlation

**Domain Alias(es):** `TRC-INV-03`.

**Enforcement:** Trace Recorder.

**Source-derived statement:** untuk consequential events.

**Canonical/source formula:**

\[ TraceEvent\Rightarrow ReconstructableContext\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-106 --- Trace Integrity

**Domain Alias(es):** `TRC-INV-05`.

**Enforcement:** Trace Recorder.

**Source-derived statement:** sesuai profile.

**Canonical/source formula:**

\[ UnauthorizedMutation\Rightarrow PreventedOrDetectable\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-107 --- No Fabrication

**Domain Alias(es):** `TRC-INV-06`.

**Enforcement:** Trace Recorder.

**Canonical/source formula:**

\[ MissingTrace\not\Rightarrow InventedTrace\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-108 --- Trace Confidentiality

**Domain Alias(es):** `TRC-INV-07`.

**Enforcement:** Trace Recorder.

**Canonical/source formula:**

\[ TraceAccess\Rightarrow AuthorizedAccess\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-109 --- Chain-of-Thought Independence

**Domain Alias(es):** `TRC-INV-08`.

**Enforcement:** Trace Recorder.

## **Source-derived statement:**

**Canonical/source formula:**

\[ ConformanceTrace\not\Rightarrow PrivateChainOfThought
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-110 --- Governance Root

**Domain Alias(es):** `HG-INV-01`.

**Enforcement:** Human Governance / Control Plane.

**Canonical/source formula:**

\[ AgentAutonomy\subset eq
Human/OrganizationalGovernanceEnvelope \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-111 --- Intent Integrity

**Domain Alias(es):** `HG-INV-03`.

**Enforcement:** Human Governance / Control Plane.

**Canonical/source formula:**

\[ AgentOptimization\not\Rightarrow IntentMutation\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-112 --- Delegation Bound

**Domain Alias(es):** `HG-INV-04`.

**Enforcement:** Human Governance / Control Plane.

**Canonical/source formula:**

\[ DelegatedOperationalAuthority \subset eq
OrganizationalGovernanceAuthority \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-113 --- Accountability Persistence

**Domain Alias(es):** `HG-INV-05`.

**Enforcement:** Human Governance / Control Plane.

**Canonical/source formula:**

\[
DelegatedExecution\not\Rightarrow AccountabilityErasure
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-114 --- Approval Separation

**Domain Alias(es):** `HG-INV-06`.

**Enforcement:** Human Governance / Control Plane.

**Canonical/source formula:**

\[ Approval\neq AuthorityGrant\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-115 --- Approval Freshness

**Domain Alias(es):** `HG-INV-07`.

**Enforcement:** Human Governance / Control Plane.

**Canonical/source formula:**

\[ MaterialSubjectChange\Rightarrow ReevaluateApproval\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-116 --- Override Governance

**Domain Alias(es):** `HG-INV-08`.

**Enforcement:** Human Governance / Control Plane.

**Canonical/source formula:**

\[ Override\neq ControlBypass\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-117 --- Break-Glass Auditability

**Domain Alias(es):** `HG-INV-09`.

**Enforcement:** Human Governance / Control Plane.

**Canonical/source formula:**

\[ BreakGlass\not\Rightarrow NoAudit\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-118 --- No Fabricated Approval

**Domain Alias(es):** `HG-INV-10`.

**Enforcement:** Human Governance / Control Plane.

**Canonical/source formula:**

\[ HumanUnavailable\not\Rightarrow Approved\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-119 --- Risk Acceptance Separation

**Domain Alias(es):** `HG-INV-11`.

**Enforcement:** Human Governance / Control Plane.

**Canonical/source formula:**

\[ RiskAssessment\neq RiskAcceptance\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-120 --- Automation Accountability

**Domain Alias(es):** `HG-INV-12`.

**Enforcement:** Human Governance / Control Plane.

**Canonical/source formula:**

\[ Automation\not\Rightarrow AccountabilityErasure\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-121 --- Human Decision Fallibility

**Domain Alias(es):** `HG-INV-13`.

**Enforcement:** Human Governance / Control Plane.

**Canonical/source formula:**

\[ HumanDecision\neq GuaranteedCorrectDecision\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-122 --- Policy Integrity

**Domain Alias(es):** `HG-INV-14`.

**Enforcement:** Human Governance / Control Plane.

## **Source-derived statement:**

**Canonical/source formula:**

\[ HumanRequest\neq PolicyMutation\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-123 --- Controlled Failure

**Domain Alias(es):** `FR-INV-01`.

**Enforcement:** Failure & Recovery Control.

**Canonical/source formula:**

\[ Failure\not\Rightarrow ControlBypass\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-124 --- No Blind Retry

**Domain Alias(es):** `FR-INV-02`.

**Enforcement:** Failure & Recovery Control.

**Canonical/source formula:**

\[ Retry\Rightarrow CurrentStateValidation\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-125 --- Recovery Authority

**Domain Alias(es):** `FR-INV-04`.

**Enforcement:** Failure & Recovery Control.

**Canonical/source formula:**

\[ RecoveryAction\Rightarrow ValidAuthority\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-126 --- Recovery Verification

**Domain Alias(es):** `FR-INV-05`.

**Enforcement:** Failure & Recovery Control.

**Canonical/source formula:**

\[ RecoverySuccess\Rightarrow RequiredVerificationSatisfied\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-127 --- Bounded Retry

**Domain Alias(es):** `FR-INV-06`.

**Enforcement:** Failure & Recovery Control.

**Canonical/source formula:**

\[ RetryCount\leq RetryBudget\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-128 --- Safety Kernel Fail-Controlled

**Domain Alias(es):** `FR-INV-07`.

**Enforcement:** Failure & Recovery Control.

**Canonical/source formula:**

\[ MandatoryControlFailure\Rightarrow\neg ImplicitPermit
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-129 --- Escalation Non-Resolution

**Domain Alias(es):** `FR-INV-08`.

**Enforcement:** Failure & Recovery Control.

**Canonical/source formula:**

\[ Escalated\not\Rightarrow Resolved\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-130 --- Goal Integrity Under Replan

**Domain Alias(es):** `FR-INV-10`.

**Enforcement:** Failure & Recovery Control.

**Source-derived statement:** kecuali valid governance change.

**Canonical/source formula:**

\[ Replan\Rightarrow PreserveGoalAndConstraints\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-131 --- Untrusted Content Non-Authority

**Domain Alias(es):** `SEC-INV-01`.

**Enforcement:** Security Controls / Safety Kernel.

**Canonical/source formula:**

\[ UntrustedContent\not\Rightarrow Authority\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-132 --- Agent Non-Root-of-Trust

**Domain Alias(es):** `SEC-INV-02`.

**Enforcement:** Security Controls / Safety Kernel.

**Canonical/source formula:**

\[ Agent\neq AutonomousRootOfTrust\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-133 --- Safety Kernel Non-Bypass

**Domain Alias(es):** `SEC-INV-03`.

**Enforcement:** Security Controls / Safety Kernel.

**Canonical/source formula:**

\[
ConsequentialEffect\Rightarrow ApplicableSafetyKernelEvaluation
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-134 --- Credential Non-Authority

**Domain Alias(es):** `SEC-INV-04`.

**Enforcement:** Security Controls / Safety Kernel.

**Canonical/source formula:**

\[
CredentialPossession\not\Rightarrow GovernanceAuthority
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-135 --- Context Least Privilege

**Domain Alias(es):** `SEC-INV-06`.

**Enforcement:** Security Controls / Safety Kernel.

**Canonical/source formula:**

\[ Context(a,t)\subset eq NecessaryContext(a,t) \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-136 --- Replay Control

**Domain Alias(es):** `SEC-INV-08`.

**Enforcement:** Security Controls / Safety Kernel.

**Canonical/source formula:**

\[ HistoricalPermit\not\Rightarrow UnlimitedReuse\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-137 --- Evidence/Trace Integrity

**Domain Alias(es):** `SEC-INV-09`.

**Enforcement:** Security Controls / Safety Kernel.

**Source-derived statement:** sesuai profile.

**Canonical/source formula:**

\[
UnauthorizedMutation(Evidence/Trace)\Rightarrow PreventedOrDetectable
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-138 --- Fail-Controlled Security

**Domain Alias(es):** `SEC-INV-10`.

**Enforcement:** Security Controls / Safety Kernel.

**Canonical/source formula:**

\[
MandatorySecurityControlFailure\Rightarrow\neg ImplicitPermit
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-139 --- Security Recovery Governance

**Domain Alias(es):** `SEC-INV-12`.

**Enforcement:** Security Controls / Safety Kernel.

## **Source-derived statement:**

**Canonical/source formula:**

\[ SecurityFailure\not\Rightarrow GovernanceSuspension\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-140 --- Requirement Traceability

**Domain Alias(es):** `CONF-INV-01`.

**Enforcement:** Conformance Engine.

**Canonical/source formula:**

\[ MandatoryRequirement\Rightarrow IdentifiableTestOrAssessment
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-141 --- Evidence

**Domain Alias(es):** `CONF-INV-02`.

**Enforcement:** Conformance Engine.

**Canonical/source formula:**

\[ ConformancePass\Rightarrow SufficientEvidence\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-142 --- No Inconclusive Success

**Domain Alias(es):** `CONF-INV-03`.

**Enforcement:** Conformance Engine.

**Canonical/source formula:**

\[ Inconclusive\not\Rightarrow Pass\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-143 --- Mandatory Violation

**Domain Alias(es):** `CONF-INV-04`.

**Enforcement:** Conformance Engine.

**Canonical/source formula:**

\[
MandatoryViolation\Rightarrow\neg UnconditionalConformant
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-144 --- Scope Integrity

**Domain Alias(es):** `CONF-INV-05`.

**Enforcement:** Conformance Engine.

**Canonical/source formula:**

\[
Conformance(scope_a)\not\Rightarrow Conformance(scope_b)
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-145 --- Version Integrity

**Domain Alias(es):** `CONF-INV-06`, `SCH-INV-06`.

**Enforcement:** Conformance Engine; Schema Validator.

**Source-derived statement:** jika material change.

**Canonical/source formula:**

\[ Conformance(v_1)\not\Rightarrow Conformance(v_2) \]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-146 --- Profile Inheritance

**Domain Alias(es):** `CONF-INV-07`.

**Enforcement:** Conformance Engine.

**Canonical/source formula:**

\[
Conformant(Profile)\Rightarrow Conformant(MandatoryBase(Profile))
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-147 --- Schema Non-Sufficiency

**Domain Alias(es):** `CONF-INV-08`.

**Enforcement:** Conformance Engine.

**Canonical/source formula:**

\[ SchemaValid\not\Rightarrow SemanticConformance\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-148 --- No Chain-of-Thought Requirement

**Domain Alias(es):** `CONF-INV-09`.

**Enforcement:** Conformance Engine.

**Canonical/source formula:**

\[
ConformanceEvidence\not\Rightarrow PrivateChainOfThought
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-149 --- Conformance Non-Zero-Risk

**Domain Alias(es):** `CONF-INV-10`.

**Enforcement:** Conformance Engine.

## **Source-derived statement:**

**Canonical/source formula:**

\[ Conformant\not\Rightarrow ZeroResidualRisk\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-150 --- Construct Separation

**Domain Alias(es):** `SCH-INV-01`.

**Enforcement:** Schema Validator.

**Source-derived statement:** Capability, Authority, Policy, and Risk
MUST remain representationally distinct.

**Canonical/source formula:**

\[
Capability\neq Authority\neq Policy\neq Risk\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-151 --- Structural Non-Authority

**Domain Alias(es):** `SCH-INV-02`.

**Enforcement:** Schema Validator.

**Canonical/source formula:**

\[ SchemaValid\not\Rightarrow Authorized\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-152 --- Structural Non-Conformance

**Domain Alias(es):** `SCH-INV-03`.

**Enforcement:** Schema Validator.

**Canonical/source formula:**

\[ SchemaValid\not\Rightarrow Conformant\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-153 --- Safe Unknown

**Domain Alias(es):** `SCH-INV-04`.

**Enforcement:** Schema Validator.

**Canonical/source formula:**

\[ UnknownMandatoryValue\not\Rightarrow Allow\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-154 --- Reference Integrity

**Domain Alias(es):** `SCH-INV-05`.

**Enforcement:** Schema Validator.

**Canonical/source formula:**

\[ GovernanceReference\Rightarrow UnambiguousResolution\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-155 --- Extension Non-Override

**Domain Alias(es):** `SCH-INV-07`.

**Enforcement:** Schema Validator.

**Canonical/source formula:**

\[
Extension\not\Rightarrow CanonicalSemanticRedefinition
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-156 --- Migration Preservation

**Domain Alias(es):** `SCH-INV-08`.

**Enforcement:** Schema Validator.

**Canonical/source formula:**

\[ CompatibleMigration\Rightarrow SemanticPreservation\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-157 --- Decision Traceability

**Domain Alias(es):** `SCH-INV-09`.

**Enforcement:** Schema Validator.

**Canonical/source formula:**

\[ ConsequentialDecisionObject\Rightarrow GovernanceReferences\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-158 --- No Private Reasoning Requirement

**Domain Alias(es):** `SCH-INV-10`.

**Enforcement:** Schema Validator.

## **Source-derived statement:**

**Canonical/source formula:**

\[
MachineReadableGovernance\not\Rightarrow PrivateChainOfThought
\]

**Traceability:**
`No direct mapping asserted; consult Appendix F verification disposition`.

------------------------------------------------------------------------

### AOF-INV-159 --- Core Preservation

**Domain Alias(es):** `PRF-INV-01`.

**Enforcement:** Framework Profiles / Conformance.

**Canonical/source formula:**

\[
StrongerProfile\Rightarrow Preserve(ApplicableCoreRequirements)
\]

**Traceability:** Section 21 / Appendix F.

------------------------------------------------------------------------

### AOF-INV-160 --- No Profile Weakening

**Domain Alias(es):** `PRF-INV-02`.

**Enforcement:** Framework Profiles / Conformance.

**Canonical/source formula:**

\[
ProfileComposition\not\Rightarrow MandatoryControlRemoval
\]

**Traceability:** Section 21 / Appendix F.

------------------------------------------------------------------------

### AOF-INV-161 --- Explicit Claim

**Domain Alias(es):** `PRF-INV-03`.

**Enforcement:** Framework Profiles / Conformance.

**Canonical/source formula:**

\[ ProfileClaim\Rightarrow DeclaredProfileScope \]

**Traceability:** Section 21 / Appendix F.

------------------------------------------------------------------------

### AOF-INV-162 --- Domain Profile Non-Linearity

**Domain Alias(es):** `PRF-INV-04`.

**Enforcement:** Framework Profiles / Conformance.

**Canonical/source formula:**

\[
AOF\text{-}Secure\text{-}SDLC\neq LinearMaturityLevel
\]

**Traceability:** Section 21 / Appendix F.

------------------------------------------------------------------------

## A.5 Legacy Appendix A Migration Map

Daftar 33 invariant families lama dipertahankan sebagai migration
references. Mapping di bawah menggunakan exact/strong lexical match
hanya; unresolved items tetap explicit dan MUST direview, bukan silently
assigned.

  ---------------------------------------------------------------------------------
  Legacy   Legacy Family          Candidate Canonical ID               Match Status
  \#                                                                   
  -------- ---------------------- ------------------------------------ ------------
  1        Authority Bound        `AOF-INV-047` --- Authority Bound    Exact

  2        Delegation             `AOF-INV-038` --- Delegation         Exact
           Conservation           Conservation                         

  3        Policy Mediation       `AOF-INV-056` --- Policy Mediation   Exact

  4        State Validity         `AOF-INV-097` --- State Validity     Exact

  5        Evidence Provenance    `AOF-INV-081` --- Derived Provenance Lexical
                                                                       candidate
                                                                       (0.76)

  6        Verification           `AOF-INV-044` --- Verification       Exact
           Independence           Independence                         

  7        Trace Completeness     `AOF-INV-103` --- Trace Completeness Exact

  8        Controlled Failure     `AOF-INV-123` --- Controlled Failure Exact

  9        Explicit Termination   `AOF-INV-024` --- Successful         Lexical
                                  Termination                          candidate
                                                                       (0.67)

  10       Capability-Authority   `AOF-INV-030` ---                    Exact
           Separation             Capability-Authority Separation      

  11       Positive Authorization `AOF-INV-048` --- Positive           Exact
                                  Authorization                        

  12       Constraint Inheritance `AOF-INV-146` --- Profile            Lexical
                                  Inheritance                          candidate
                                                                       (0.68)

  13       Context Least          `AOF-INV-135` --- Context Least      Exact
           Privilege              Privilege                            

  14       Risk-Proportional      `AOF-INV-065` --- Risk-Proportional  Exact
           Control                Control                              

  15       No Silent State        `AOF-INV-032` --- No                 Lexical
           Mutation               Self-Authorization                   candidate
                                                                       (0.62)

  16       Proposal Non-Authority `AOF-INV-013` --- Proposal           Exact
                                  Non-Authority                        

  17       Verification           `AOF-INV-091` --- Verification       Lexical
           Non-Circularity        Non-Authority                        candidate
                                                                       (0.81)

  18       Goal Integrity         `AOF-INV-122` --- Policy Integrity   Lexical
                                                                       candidate
                                                                       (0.80)

  19       Accountability         `AOF-INV-113` --- Accountability     Lexical
           Completeness           Persistence                          candidate
                                                                       (0.79)

  20       No Implicit Allow      `AOF-INV-007` --- No Implicit Allow  Exact

  21       Retry Side-Effect      `Pending Final Consistency Review`   Unresolved
           Safety                                                      

  22       Dynamic Risk Control   `Pending Final Consistency Review`   Unresolved

  23       Authority Revocation   `AOF-INV-008` --- Revocation         Lexical
           Enforcement            Enforcement                          candidate
                                                                       (0.81)

  24       Trace Before Terminal  `Pending Final Consistency Review`   Unresolved
           Closure                                                     

  25       No Self-Elevation      `AOF-INV-049` --- No Self-Elevation  Exact

  26       Effective Autonomy     `Pending Final Consistency Review`   Unresolved
           Bound                                                       

  27       Memory Non-Authority   `AOF-INV-033` --- Memory             Exact
                                  Non-Authority                        

  28       Information Flow       `AOF-INV-052` --- Information-Flow   Lexical
           Control                Separation                           candidate
                                                                       (0.75)

  29       Agent Output           `AOF-INV-034` --- Trust              Lexical
           Non-Authority          Non-Authority                        candidate
                                                                       (0.76)

  30       Confidence             `AOF-INV-035` --- Confidence         Exact
           Non-Verification       Non-Verification                     

  31       Agent Replacement      `Pending Final Consistency Review`   Unresolved
           Reauthorization                                             

  32       Policy Enforcement     `AOF-INV-041` --- Policy Enforcement Exact
           Independence           Independence                         

  33       Agent Accountability   `AOF-INV-120` --- Automation         Lexical
                                  Accountability                       candidate
                                                                       (0.76)
  ---------------------------------------------------------------------------------

------------------------------------------------------------------------

## A.6 Registry Governance Rules

1.  `AOF-INV-*` is the canonical global identity namespace for v1.0.
2.  Existing domain-local invariant IDs MUST remain stable aliases and
    MUST NOT be destructively renumbered.
3.  A canonical invariant MAY have multiple domain aliases only when
    semantic identity is established.
4.  Similar wording alone MUST NOT be used to merge invariants.
5.  Any merge/split discovered during Final Consistency Review MUST
    preserve an explicit migration record.
6.  Every applicable canonical invariant MUST eventually map to one or
    more normative Requirements and verification methods.
7.  Behavioral/security invariants SHOULD prefer negative/adversarial
    tests where feasible.
8.  Non-executable governance requirements MAY use Documentary
    Inspection, Configuration Inspection, Trace Inspection, or Human
    Review.
9.  `Pending` traceability MUST NOT be represented as tested/conformant.
10. Registry changes after Semantic Freeze require versioned change
    control.

------------------------------------------------------------------------

## A.7 Master Registry Requirements

**AOF-REG-001** --- Every domain invariant MUST have a stable canonical
`AOF-INV-*` identity or an explicit documented alias mapping.

**AOF-REG-002** --- Domain invariant aliases MUST NOT be destructively
renumbered during v1.0 reconciliation.

**AOF-REG-003** --- Semantic merge MUST require explicit equivalence
review; lexical similarity alone MUST NOT establish equivalence.

**AOF-REG-004** --- Every applicable canonical invariant MUST map to at
least one normative Requirement before Semantic Freeze.

**AOF-REG-005** --- Every applicable behavioral invariant MUST map to at
least one Conformance Test or explicit non-executable verification
method before Semantic Freeze.

**AOF-REG-006** --- Unresolved mapping MUST remain explicit and MUST NOT
be treated as conformant evidence.

**AOF-REG-007** --- Registry changes after Semantic Freeze MUST follow
versioned change control.

------------------------------------------------------------------------

## A.8 Freeze Gate

Master Invariant Registry MAY become `Freeze Candidate` when:

-   all domain invariant aliases are represented;
-   legacy Appendix A families are reconciled;
-   semantic duplicate candidates are reviewed;
-   Requirement mappings are complete;
-   Test/verification-method mappings are complete;
-   no orphan mandatory invariant remains;
-   profile applicability is validated;
-   identifier stability audit passes.

Pada pass ini, identifier extraction dan canonical namespace
establishment selesai. `Requirement/Test` mapping dan
semantic-equivalence review tetap menjadi pekerjaan tahap berikutnya
yang explicit.

------------------------------------------------------------------------

# Appendix B --- Reference Architecture Summary

```text
Human / External Governance
            |
            v
+-------------------------------+
|         CONTROL PLANE         |
| Orchestrator                  |
| Authority / Policy / Risk     |
| State Validation              |
| Safety Kernel                 |
+---------------+---------------+
                |
        Proposal / Decision
                |
       +--------+---------+
       |                  |
       v                  v
+--------------+   +---------------+
| REASONING    |   | ASSURANCE     |
| PLANE        |   | PLANE         |
| Agents       |   | Evidence      |
| Planning     |   | Verification  |
| Analysis     |   | Validation    |
+------+-------+   +-------^-------+
       |                   |
       | Action Proposal   | Evidence
       v                   |
+-------------------------------+
|          EFFECT PLANE         |
| Tools / APIs / Files / DB     |
| CI/CD / Infrastructure        |
+-------------------------------+
```

------------------------------------------------------------------------

# Appendix C --- Core Framework Statement

\[
\boxed{ Reason\rightarrow Propose\rightarrow Govern\rightarrow Act\rightarrow Verify\rightarrow Update }
\]

\[ \boxed{ Agent\ Reasoning\neq Orchestration\ Authority } \]

\[ \boxed{ Autonomy\neq Authority } \]

\[ \boxed{ Capability\neq Authority } \]

AOF tidak bertujuan menghilangkan autonomy. AOF memformalkan **Governed
Autonomous Orchestration** melalui explicit `Authority`, `Policy`,
`Risk`, `Verification`, `State`, `Evidence`, dan `Trace`.

------------------------------------------------------------------------

# Appendix D --- Release Status

Dokumen ini merupakan **Framework Specification v1.0
RC-Failure-Recovery** yang mengonsolidasikan conceptual intent v0.1 dan
formal semantics yang telah tersedia pada v0.2.

Sebelum diberi status **Final/Public Release**, project SHOULD
menyelesaikan:

1.  dedicated prior-art and literature review;
2.  authoritative external bibliography;
3.  complete Core Model cross-reference validation;
4.  machine-readable schemas;
5.  detailed conformance test criteria;
6.  reference implementation;
7.  empirical validation terhadap applicable research hypotheses;
8.  security review;
9.  terminology freeze;
10. versioned change log.

Tidak adanya item tersebut tidak membatalkan specification semantics
dalam dokumen ini, tetapi membatasi kekuatan klaim research, novelty,
interoperability, dan empirical validation.

# Appendix E --- Machine-Readable Schemas

## E.1 Purpose

`Schema Model` menerjemahkan canonical AOF constructs dan contracts
menjadi machine-readable representations yang dapat divalidasi,
dipertukarkan, disimpan, diuji, dan digunakan oleh reference
implementation tanpa mengubah normative semantics.

Canonical separation:

\[ SchemaValidity\neq SemanticValidity\neq Conformance\]

Schema membuktikan structural validity. Control Plane tetap bertanggung
jawab atas Authority, Policy, Risk, State, Verification, dan other
semantic predicates.

\[ ValidSchema(x)\not\Rightarrow ExecuteAllowed(x) \]

------------------------------------------------------------------------

## E.2 Schema Design Principles

AOF schemas SHOULD mengikuti principles berikut:

-   explicit identity;
-   explicit version;
-   explicit scope;
-   stable field semantics;
-   machine validation;
-   extensibility tanpa silent semantic weakening;
-   backward-compatible evolution dalam same compatible release line;
-   references daripada uncontrolled duplication;
-   provenance untuk governance-critical objects;
-   normalized enums;
-   timestamps dengan unambiguous representation;
-   no hidden consequential fields.

**AOF-SCH-001** --- Machine-readable representation MUST preserve
normative distinction antara `Capability`, `Authority`, `Policy`,
`Risk`, `Evidence`, `Verification`, `Decision`, `Action`, `State`, dan
`Trace`.

------------------------------------------------------------------------

## E.3 Canonical Schema Set

v1.0 schema package SHOULD menyediakan schemas untuk minimum objects:

1.  `Goal`;
2.  `Task`;
3.  `Agent`;
4.  `ContextDescriptor`;
5.  `Resource`;
6.  `Capability`;
7.  `AuthorityGrant`;
8.  `Policy`;
9.  `RiskAssessment`;
10. `ActionProposal`;
11. `Decision`;
12. `ExecutionContract`;
13. `Evidence`;
14. `Verification`;
15. `Approval`;
16. `StateTransition`;
17. `TraceEvent`;
18. `AgentInteractionContract`;
19. `EscalationPackage`;
20. `Outcome`;
21. `ConformanceManifest`;
22. `ConformanceReport`.

Profiles MAY add domain-specific schemas.

------------------------------------------------------------------------

## E.4 Schema Envelope

Governance-critical schema object SHOULD menggunakan common envelope
atau semantically equivalent fields:

``` yaml
id: string
schema_type: string
schema_version: string
created_at: timestamp
updated_at: timestamp | null
scope: object | reference
provenance: object | reference
extensions: object | null
```

`extensions` MUST NOT redefine canonical field meaning.

------------------------------------------------------------------------

## E.5 Identifier Semantics

Identifiers MUST cukup stable dalam claimed scope.

Reference patterns MAY menggunakan UUID, URI, content-addressed ID,
database ID, atau domain identifier.

Cross-object references SHOULD distinguish object type dan ID untuk
mengurangi ambiguity.

**AOF-SCH-002** --- Governance-critical reference MUST resolve
unambiguously dalam applicable system scope.

------------------------------------------------------------------------

## E.6 Version Semantics

Schema package MUST memiliki version.

Object MAY memiliki independent semantic/configuration version.

Reference:

```text
schema_version != object_version != specification_version
```

Implementations MUST NOT menyamakan ketiganya secara implicit.

------------------------------------------------------------------------

## E.7 Timestamp Semantics

Machine-readable timestamps SHOULD menggunakan timezone-aware,
unambiguous representation seperti RFC 3339 compatible form.

Ordering-critical systems MAY menambahkan:

-   sequence number;
-   logical clock;
-   causal reference;
-   transaction version.

Timestamp alone MUST NOT dianggap sufficient causal ordering jika
architecture membutuhkan stronger semantics.

------------------------------------------------------------------------

## E.8 Enumerations

Canonical enums SHOULD serialized menggunakan English formal
identifiers.

Examples:

```text
Created
Ready
Executing
Verifying
Completed
Failed
Rejected
Escalated
Cancelled
```

Translations MAY digunakan pada UI, tetapi persisted canonical
identifier SHOULD tetap stable.

------------------------------------------------------------------------

## E.9 Goal Schema

Reference:

``` yaml
Goal:
  id: string
  description: string
  success_criteria:
    - criterion
  constraints:
    - constraint
  priority: string | number
  provenance: reference
```

Formal correspondence:

\[
g=\langle id,description,successCriteria,constraints,priority\rangle
\]

Success criteria MUST NOT silently mutated.

------------------------------------------------------------------------

## E.10 Task Schema

Reference:

``` yaml
Task:
  id: string
  parent_id: string | null
  goal_id: string
  input_refs: [reference]
  preconditions: [condition]
  postconditions: [condition]
  constraints: [constraint]
  requirements: [reference]
  risk_ref: reference | null
  state: TaskState
  assigned_agent_ids: [string]
  version: string
```

Formal correspondence:

\[
t=\langle id,parent,goal,input,preconditions,postconditions,constraints,requirements,risk,state\rangle
\]

**AOF-SCH-003** --- Child Task representation MUST preserve inherited
mandatory constraints or references thereto.

------------------------------------------------------------------------

## E.11 Agent Schema

Reference:

``` yaml
Agent:
  id: string
  type: AgentType
  roles: [string]
  capability_refs: [reference]
  authority_refs: [reference]
  context_scope: reference
  memory_policy: reference | null
  policy_refs: [reference]
  risk_profile_ref: reference | null
  state: AgentState
  interface_ref: reference
```

`capability_refs` dan `authority_refs` MUST remain separate.

\[ Capability\neq Authority\]

------------------------------------------------------------------------

## E.12 Context Descriptor Schema

Reference:

``` yaml
ContextDescriptor:
  id: string
  classification: string
  trust_level: string
  purpose: string
  source_refs: [reference]
  data_refs: [reference]
  disclosure_scope: object
  retention: object | null
  redaction_policy_ref: reference | null
```

Context payload MAY disimpan terpisah dari descriptor.

Sensitive payload SHOULD tidak duplicated tanpa kebutuhan.

------------------------------------------------------------------------

## E.13 Resource Schema

Reference:

``` yaml
Resource:
  id: string
  type: string
  canonical_identity: string
  environment: string
  classification: string | null
  operations: [string]
  trust_boundary: string | null
  metadata: object
```

High-risk action SHOULD bind ke `canonical_identity`.

------------------------------------------------------------------------

## E.14 Capability Schema

Reference:

``` yaml
Capability:
  id: string
  name: string
  operations: [string]
  resource_types: [string]
  constraints: [condition]
  observed_evidence_refs: [reference]
```

Capability declaration MUST NOT create Authority.

------------------------------------------------------------------------

## E.15 Authority Grant Schema

Reference:

``` yaml
AuthorityGrant:
  id: string
  subject: reference
  operations: [string]
  resources: [reference | selector]
  scope: object
  constraints: [condition]
  issuer: reference
  delegable: boolean
  delegation_depth: integer | null
  valid_from: timestamp
  valid_until: timestamp | null
  status: AuthorityStatus
  parent_grant_id: string | null
  provenance: reference
```

Canonical lifecycle SHOULD support semantically equivalent states:

`Active`, `Suspended`, `Revoked`, `Expired`, `Consumed`.

**AOF-SCH-004** --- Authority schema MUST represent scope, validity,
status, issuer, dan delegation relationship.

------------------------------------------------------------------------

## E.16 Policy Schema

Reference:

``` yaml
Policy:
  id: string
  version: string
  scope: object
  subject_selector: object
  resource_selector: object
  action_selector: object
  condition: expression
  effect: PolicyEffect
  priority: integer
  source: reference
  valid_from: timestamp
  valid_until: timestamp | null
  status: PolicyStatus
  provenance: reference
```

Canonical `PolicyEffect`:

```text
Allow
Deny
RequireVerification
RequireApproval
Escalate
```

Unknown custom effect MUST NOT silently map ke `Allow`.

------------------------------------------------------------------------

## E.17 Risk Assessment Schema

Reference:

``` yaml
RiskAssessment:
  id: string
  subject: reference
  profile_ref: reference
  method: string
  hazards: [object]
  likelihood: value
  impact: value | object
  exposure: value | object
  inherent_class: RiskClass
  controls: [reference]
  residual_class: RiskClass
  confidence: value | null
  assessor: reference
  acceptance_ref: reference | null
  reassessment_triggers: [condition]
  valid_at: timestamp
  provenance: reference
```

Canonical classes:

`Low`, `Moderate`, `High`, `Critical`.

------------------------------------------------------------------------

## E.18 Action Proposal Schema

Reference:

``` yaml
ActionProposal:
  id: string
  actor: reference
  task_id: string
  operation: string
  target: reference
  parameters: object
  preconditions: [condition]
  expected_effect: object
  risk_ref: reference | null
  evidence_refs: [reference]
  created_at: timestamp
```

Proposal MUST NOT contain field yang semantically means self-granted
permission.

\[ Proposal\neq AuthorizedDecision\]

------------------------------------------------------------------------

## E.19 Decision Schema

Reference:

``` yaml
Decision:
  id: string
  actor: reference
  type: DecisionType
  subject: reference
  input_refs: [reference]
  state_ref: reference
  authority_result_ref: reference
  policy_result_ref: reference
  risk_result_ref: reference
  verification_refs: [reference]
  approval_refs: [reference]
  outcome: DecisionOutcome
  rationale: string | structured_reason | null
  valid_until: timestamp | null
  created_at: timestamp
```

Private chain-of-thought MUST NOT menjadi required schema field.

**AOF-SCH-005** --- Decision schema MUST preserve references ke
applicable governance results untuk consequential decision.

------------------------------------------------------------------------

## E.20 Execution Contract Schema

`Execution Contract` mengikat authorized candidate effect ke governed
execution boundary.

Reference:

``` yaml
ExecutionContract:
  id: string
  task_id: string
  decision_id: string
  actor: reference
  operation: string
  target: reference
  parameter_constraints: object
  authority_ref: reference
  policy_decision_ref: reference
  risk_ref: reference
  state_ref: reference
  verification_refs: [reference]
  approval_refs: [reference]
  idempotency_key: string | null
  valid_from: timestamp
  valid_until: timestamp | null
  single_use: boolean
```

\[ ExecutionContract\neq AuthorityGrant\]

Contract hanya merepresentasikan bounded execution eligibility
berdasarkan underlying controls.

------------------------------------------------------------------------

## E.21 Evidence Schema

Reference:

``` yaml
Evidence:
  id: string
  source: reference
  claim_refs: [reference]
  content_ref: reference | null
  content_digest: string | null
  provenance: object
  integrity: object | null
  freshness: object | null
  confidence: value | null
  classification: string | null
  scope: object
  observed_at: timestamp
  relations:
    derived_from: [reference]
    corroborates: [reference]
    contradicts: [reference]
    supersedes: [reference]
```

**AOF-SCH-006** --- Derived Evidence MUST support source/derivation
references ketika required oleh Evidence Profile.

------------------------------------------------------------------------

## E.22 Verification Schema

Reference:

``` yaml
Verification:
  id: string
  claim_ref: reference
  criteria_refs: [reference]
  evidence_refs: [reference]
  verifier: reference
  method: string
  profile_ref: reference
  independence: VerificationIndependence
  result: VerificationResult
  confidence: value | null
  limitations: [string]
  subject_version: string | null
  verified_at: timestamp
  provenance: reference
```

Canonical result:

`Verified`, `Rejected`, `Inconclusive`.

`Inconclusive` MUST NOT serialize as success-equivalent boolean.

------------------------------------------------------------------------

## E.23 Approval Schema

Reference:

``` yaml
Approval:
  id: string
  subject: reference
  approver: reference
  authority_ref: reference
  decision: ApprovalDecision
  scope: object
  subject_version: string | null
  conditions: [condition]
  valid_until: timestamp | null
  evidence_refs: [reference]
  created_at: timestamp
```

Approval MUST bind ke intended subject/scope.

------------------------------------------------------------------------

## E.24 State Transition Schema

Reference:

``` yaml
StateTransition:
  id: string
  scope: reference
  state_before_ref: reference
  expected_version: string | null
  decision_ref: reference
  action_ref: reference | null
  evidence_refs: [reference]
  state_after_ref: reference
  actor: reference
  result: TransitionResult
  committed_at: timestamp
```

**AOF-SCH-007** --- Consequential State Transition schema MUST identify
before/after state references dan governing Decision.

------------------------------------------------------------------------

## E.25 Trace Event Schema

Reference:

``` yaml
TraceEvent:
  id: string
  event_type: TraceEventType
  timestamp: timestamp
  sequence: integer | null
  actor: reference
  session_id: string | null
  task_id: string | null
  decision_id: string | null
  action_id: string | null
  input_refs: [reference]
  evidence_refs: [reference]
  state_before_ref: reference | null
  state_after_ref: reference | null
  result: object | null
  correlation: object
  classification: string | null
  integrity: object | null
```

Trace schema MUST NOT require private chain-of-thought.

------------------------------------------------------------------------

## E.26 Agent Interaction Contract Schema

Reference:

``` yaml
AgentInteractionContract:
  id: string
  sender: reference
  receiver: reference
  task_ref: reference
  message_type: string
  context_refs: [reference]
  authority_context_refs: [reference]
  constraints: [condition]
  expected_output_schema_ref: reference
  disclosure_scope: object
  expires_at: timestamp | null
```

Message content MUST NOT implicitly expand receiver Authority.

------------------------------------------------------------------------

## E.27 Escalation Package Schema

Reference:

``` yaml
EscalationPackage:
  id: string
  subject: reference
  reason: string
  current_state_ref: reference
  decision_required: string
  failure_refs: [reference]
  risk_refs: [reference]
  evidence_refs: [reference]
  authority_refs: [reference]
  policy_refs: [reference]
  attempt_history_refs: [reference]
  options: [object]
  created_at: timestamp
```

Escalation package SHOULD preserve sufficient context tanpa unnecessary
sensitive disclosure.

------------------------------------------------------------------------

## E.28 Outcome Schema

Reference:

``` yaml
Outcome:
  id: string
  session_id: string
  status: OutcomeStatus
  goal_ref: reference
  goal_state: object
  result_refs: [reference]
  evidence_refs: [reference]
  verification_refs: [reference]
  residual_risk_refs: [reference]
  trace_refs: [reference]
  completed_at: timestamp
```

Successful outcome MUST NOT be representable solely by arbitrary Agent
declaration if mandatory verification remains unresolved.

------------------------------------------------------------------------

## E.29 Conformance Manifest Schema

Reference:

``` yaml
ConformanceManifest:
  id: string
  specification_version: string
  profile: string
  subject: reference
  subject_version: string
  scope: object
  requirement_registry_version: string
  schema_package_version: string
  test_suite_version: string
  evidence_package_ref: reference
  report_ref: reference
  assessment_mode: string
  created_at: timestamp
```

------------------------------------------------------------------------

## E.30 Conformance Report Schema

Reference:

``` yaml
ConformanceReport:
  id: string
  manifest_ref: reference
  requirements:
    - requirement_id: string
      applicability: Applicability
      result: RequirementResult
      test_refs: [reference]
      evidence_refs: [reference]
      limitations: [string]
  coverage: object
  exceptions: [object]
  assessor: reference
  final_result: ConformanceResult
  timestamp: timestamp
```

------------------------------------------------------------------------

## E.31 Reference Type

AOF schema package SHOULD menggunakan normalized reference structure
atau semantically equivalent form:

``` yaml
Reference:
  type: string
  id: string
  version: string | null
  uri: string | null
```

Raw string references MAY digunakan jika type/scope unambiguous.

------------------------------------------------------------------------

## E.32 Condition Expression

AOF core specification tidak mewajibkan satu expression language.

`condition` MAY berupa:

-   structured predicate;
-   JSON Logic-like expression;
-   policy DSL;
-   CEL-like expression;
-   Rego-like expression;
-   implementation-specific deterministic rule.

Expression language MUST memiliki documented semantics jika digunakan
untuk mandatory enforcement.

------------------------------------------------------------------------

## E.33 Extension Mechanism

Schema extension SHOULD menggunakan namespaced fields atau `extensions`.

Example:

``` yaml
extensions:
  com.example.secure-sdlc:
    change_ticket: "CHG-1234"
```

Extension MUST NOT:

-   redefine canonical field;
-   weaken mandatory validation;
-   create implicit Authority;
-   convert unknown mandatory enum menjadi Allow.

------------------------------------------------------------------------

## E.34 Unknown Fields

Parser behavior terhadap unknown fields MUST defined.

Security-sensitive implementation SHOULD NOT silently interpret unknown
governance fields.

Options:

-   reject;
-   preserve-but-ignore;
-   extension namespace processing.

Behavior MUST deterministic untuk claimed profile.

------------------------------------------------------------------------

## E.35 Unknown Enum Values

Unknown enum pada mandatory governance field SHOULD menghasilkan
validation failure atau `Pending`/controlled handling.

\[ UnknownMandatoryEnum\not\Rightarrow Allow\]

------------------------------------------------------------------------

## E.36 Required vs Optional Fields

Schema package MUST distinguish:

-   structurally required;
-   conditionally required;
-   optional;
-   profile-required.

Conditional requirement SHOULD machine-expressible atau documented
dengan Requirement ID.

------------------------------------------------------------------------

## E.37 Null and Missing Semantics

`null`, missing field, empty collection, dan unknown value MUST NOT
dianggap interchangeable jika semantics berbeda.

Example:

```text
authority_ref missing
```

tidak boleh berarti "unrestricted authority".

------------------------------------------------------------------------

## E.38 Canonical Serialization

AOF MAY publish JSON Schema as primary interchange format dan YAML
examples sebagai human-friendly serialization.

Other serializations MAY be supported jika semantic equivalence
dipertahankan.

Schema language choice MUST NOT mengubah framework semantics.

------------------------------------------------------------------------

## E.39 Schema Validation Layers

Reference validation pipeline:

```text
Syntax
  |
Schema Structure
  |
Cross-Reference Integrity
  |
Semantic Validation
  |
Governance Evaluation
  |
Conformance Evaluation
```

\[ StructuralValid\not\Rightarrow GovernanceValid\]

------------------------------------------------------------------------

## E.40 Cross-Reference Validation

References SHOULD diperiksa untuk:

-   existence;
-   expected type;
-   version compatibility;
-   scope;
-   lifecycle validity.

Dangling reference pada mandatory governance object SHOULD fail
validation atau become controlled `Pending`.

------------------------------------------------------------------------

## E.41 Semantic Validation

Semantic validators SHOULD memeriksa constraints yang tidak cukup
diekspresikan oleh structural schema.

Examples:

-   delegatee Authority subset;
-   approval subject version match;
-   verification independence;
-   state transition legality;
-   policy precedence;
-   risk-control mapping;
-   evidence freshness.

------------------------------------------------------------------------

## E.42 Schema Security

Schemas dan validators merupakan part dari trusted implementation
surface.

Security controls SHOULD melindungi:

-   schema source;
-   version;
-   validator integrity;
-   extension loading;
-   parser behavior;
-   resource limits.

Malicious oversized/deeply nested input SHOULD bounded.

------------------------------------------------------------------------

## E.43 Schema and Sensitive Data

Schemas SHOULD mendukung data classification/reference-based payload
agar secrets/sensitive evidence tidak harus embedded.

Schema validation logs MUST NOT leak protected payload.

------------------------------------------------------------------------

## E.44 Schema and Trace

Validation failure pada consequential governance object SHOULD
traceable.

Reference event:

```text
SchemaValidationFailed
```

Trace MAY record field path/error code tanpa sensitive value.

------------------------------------------------------------------------

## E.45 Schema and Conformance

Conformance tests SHOULD mencakup:

-   valid canonical object;
-   missing required field;
-   invalid enum;
-   wrong reference type;
-   stale version;
-   unauthorized extension semantics;
-   cross-reference mismatch.

Schema validity merupakan test input, bukan final conformance proof.

------------------------------------------------------------------------

## E.46 Schema Evolution

Within v1.x compatible line, schema evolution SHOULD preserve backward
compatibility kecuali explicitly versioned breaking change.

Compatible changes MAY include:

-   optional field addition;
-   new extension namespace;
-   clarified validation;
-   new non-breaking enum only jika unknown-value behavior aman.

Breaking changes MAY include:

-   field semantic redefinition;
-   required field addition without compatibility path;
-   enum meaning change;
-   reference semantic change.

------------------------------------------------------------------------

## E.47 Deprecation

Deprecated field SHOULD memiliki:

-   replacement;
-   deprecation version;
-   removal policy;
-   migration guidance.

Deprecated field MUST NOT silently change meaning.

------------------------------------------------------------------------

## E.48 Schema Migration

Migration SHOULD preserve governance meaning.

\[ Migrate(x\_{v1}\rightarrow x\_{v2})
\Rightarrow SemanticPreservation\]

Jika semantic preservation tidak possible, migration MUST require
explicit review/revalidation.

------------------------------------------------------------------------

## E.49 Schema Package Manifest

Schema release SHOULD memiliki manifest:

``` yaml
schema_package:
  specification_version: "1.0"
  package_version: "1.0.0"
  schemas:
    - name: Agent
      version: "1.0"
      file: agent.schema.json
    - name: AuthorityGrant
      version: "1.0"
      file: authority-grant.schema.json
```

Manifest SHOULD include digests pada high-assurance distribution.

------------------------------------------------------------------------

## E.50 Schema Failure Modes

### SCH-F01 --- Semantic Collapse

Distinct constructs digabung sehingga governance distinction hilang.

### SCH-F02 --- Missing Required Field

Mandatory governance information tidak representable.

### SCH-F03 --- Ambiguous Reference

Reference tidak resolve uniquely.

### SCH-F04 --- Unsafe Default

Missing/unknown value menjadi permissive behavior.

### SCH-F05 --- Version Confusion

Object/schema/specification versions tertukar.

### SCH-F06 --- Extension Override

Extension mengubah canonical semantics.

### SCH-F07 --- Sensitive Data Leakage

Validation/serialization mengungkap protected data.

### SCH-F08 --- Validator Drift

Validator tidak sesuai active schema version.

### SCH-F09 --- Migration Semantic Loss

Migration mengubah governance meaning.

### SCH-F10 --- Structural-Semantic Confusion

Schema-valid object dianggap authorized/conformant.

------------------------------------------------------------------------

## E.51 Reference Validation Algorithm

```text
INPUT:
  serialized object
  expected schema type/version
  active schema package

1. Parse safely.
2. Validate schema identity/version.
3. Validate required fields/types/enums.
4. Validate unknown-field policy.
5. Validate references.
6. Validate scope/version compatibility.
7. Run semantic validators.
8. Apply profile-specific constraints.
9. Record validation result.
10. Return:
      VALID
      INVALID
      PENDING
```

`VALID` berarti schema/semantic contract valid pada validation layer,
bukan execution permission.

------------------------------------------------------------------------

## E.52 Schema Conformance Requirements

### Core

**AOF-SCH-004 (canonical cross-reference)** — See the primary normative definition above.
status, issuer, dan delegation relationship.

**AOF-SCH-008** --- Unknown/missing mandatory governance value MUST NOT
map ke permissive default.

**AOF-SCH-009** --- Schema validation MUST NOT be treated as execution
authorization.

**AOF-SCH-010** --- Canonical enum identifiers MUST have stable
machine-readable semantics.

### Governed

**AOF-SCH-011** --- Schema package MUST be versioned.

**AOF-SCH-012** --- Cross-object references SHOULD be type/scope
validated.

**AOF-SCH-013** --- Extensions MUST NOT redefine canonical semantics.

**AOF-SCH-014** --- Governance-critical schema validation failures
SHOULD be traceable.

**AOF-SCH-015** --- Schema evolution SHOULD preserve backward
compatibility within declared compatible line.

**AOF-SCH-016** --- Migration MUST preserve governance semantics atau
require explicit revalidation.

**AOF-SCH-017** --- Sensitive payload SHOULD support
reference/classification-based representation.

**AOF-SCH-018** --- Conformance Manifest/Report MUST be
machine-representable.

### Assured / High-Assurance

**AOF-SCH-019** --- High-assurance schema package SHOULD have
integrity-verifiable distribution.

**AOF-SCH-020** --- High-assurance validators MUST have deterministic
behavior untuk mandatory governance fields.

**AOF-SCH-021** --- High-assurance validation MUST detect
version/reference mismatch yang material.

**AOF-SCH-022** --- High-assurance schema tests MUST include
unsafe-default, extension, malformed-input, dan semantic cross-reference
cases.

------------------------------------------------------------------------

## E.53 Schema Invariants

### SCH-INV-01 --- Construct Separation

\[
Capability\neq Authority\neq Policy\neq Risk\]

Capability, Authority, Policy, and Risk MUST remain representationally
distinct.

### SCH-INV-02 --- Structural Non-Authority

\[ SchemaValid\not\Rightarrow Authorized\]

### SCH-INV-03 --- Structural Non-Conformance

\[ SchemaValid\not\Rightarrow Conformant\]

### SCH-INV-04 --- Safe Unknown

\[ UnknownMandatoryValue\not\Rightarrow Allow\]

### SCH-INV-05 --- Reference Integrity

\[ GovernanceReference\Rightarrow UnambiguousResolution\]

### SCH-INV-06 --- Version Integrity

\[
SchemaVersion\neq ObjectVersion\neq SpecificationVersion
\]

### SCH-INV-07 --- Extension Non-Override

\[
Extension\not\Rightarrow CanonicalSemanticRedefinition
\]

### SCH-INV-08 --- Migration Preservation

\[ CompatibleMigration\Rightarrow SemanticPreservation\]

### SCH-INV-09 --- Decision Traceability

\[ ConsequentialDecisionObject\Rightarrow GovernanceReferences\]

### SCH-INV-10 --- No Private Reasoning Requirement

\[
MachineReadableGovernance\not\Rightarrow PrivateChainOfThought
\]

------------------------------------------------------------------------

## E.54 Schema Artifact Package

Final v1.0 release SHOULD publish machine-readable files semantically
equivalent to:

```text
schemas/
  goal.schema.json
  task.schema.json
  agent.schema.json
  context-descriptor.schema.json
  resource.schema.json
  capability.schema.json
  authority-grant.schema.json
  policy.schema.json
  risk-assessment.schema.json
  action-proposal.schema.json
  decision.schema.json
  execution-contract.schema.json
  evidence.schema.json
  verification.schema.json
  approval.schema.json
  state-transition.schema.json
  trace-event.schema.json
  agent-interaction-contract.schema.json
  escalation-package.schema.json
  outcome.schema.json
  conformance-manifest.schema.json
  conformance-report.schema.json
  schema-package-manifest.json
```

Appendix ini mendefinisikan normative semantic target. Concrete JSON
Schema files MAY menjadi separate release artifacts.

------------------------------------------------------------------------

## E.55 Schema Freeze Candidate Criteria

Schemas area MAY dinyatakan `Freeze Candidate` jika:

1.  canonical schema set stabil;
2.  common identity/version/reference semantics stabil;
3.  core object fields map ke canonical constructs tanpa semantic
    collapse;
4.  unknown/null/default semantics stabil;
5.  extension rules stabil;
6.  schema vs semantic/conformance separation stabil;
7.  evolution/migration semantics stabil;
8.  Security requirements untuk parser/validator compatible;
9.  Conformance Manifest/Report representation stabil;
10. concrete JSON Schema artifacts dapat dihasilkan tanpa unresolved
    semantic decision;
11. cross-domain review tidak menemukan missing governance-critical
    field.

------------------------------------------------------------------------

## E.56 Schema Formalization Result

Schemas v1.0 RC-Schemas diringkas sebagai:

\[ MachineReadableAOF= CanonicalObjects + StableIdentity + Versioning +
References + Validation + SafeExtension + Evolution \]

dengan:

\[ \boxed{ SchemaValidity\neq SemanticValidity\neq Conformance }
\]

\[ \boxed{ Unknown\ Mandatory\ Value\neq Allow } \]

\[
\boxed{ Machine\ Representation\ Must\ Preserve\ Governance\ Semantics }
\]

dan:

\[
\boxed{ Schema\ Evolution\ Must\ Not\ Silently\ Change\ Meaning }
\]

------------------------------------------------------------------------

# Appendix F --- Conformance Traceability Matrix

## F.1 Purpose

Appendix ini menyediakan authoritative traceability layer untuk
canonical requirement identifiers `AOF-*-*` pada AOF v1.0 Release
Candidate. Tujuannya adalah memastikan bahwa setiap explicit normative
requirement memiliki verification path yang dapat diaudit.

\[
Requirement\rightarrow Invariant\rightarrow VerificationMethod\rightarrow Test\rightarrow Evidence
\]

Appendix ini **tidak menginvent mapping**. Explicit `CT-*` dan
`AOF-INV-*` hanya dipetakan ketika hubungan same-domain memiliki
lexical/semantic evidence yang cukup kuat untuk candidate mapping.
Mapping yang belum cukup kuat tetap ditandai
`No direct AOF-INV mapping asserted` dan tetap memiliki verification
method/evidence class sehingga tidak menjadi invisible orphan.

------------------------------------------------------------------------

## F.2 Verification Method Taxonomy

  ----------------------------------------------------------------------------
  Code     Method          Intended Use
  -------- --------------- ---------------------------------------------------
  `AT`     Automated Test  Deterministic executable validation of observable
                           behavior or schema.

  `NT`     Negative /      Failure injection, forbidden action, privilege
           Adversarial     escalation, malformed/untrusted input, fail-safe
           Test            behavior.

  `DI`     Documentary     Governance ownership, declared process,
           Inspection      organizational responsibility, reference or policy
                           documentation.

  `CI`     Configuration   Authority, Policy, Security, profile, deployment,
           Inspection      or runtime configuration validation.

  `TI`     Trace           State/Decision/Action/Evidence/Verification/Trace
           Inspection      correlation and auditability.

  `HR`     Human Review    Human judgment where
                           organizational/legal/governance semantics cannot be
                           reduced to deterministic code test.
  ----------------------------------------------------------------------------

Negative/adversarial validation SHOULD dominate where the requirement
concerns prevention of unauthorized, unsafe, stale, misleading, or
non-governed effects.

------------------------------------------------------------------------

## F.3 Traceability Rules

1.  Every explicit `AOF-*-*` requirement MUST have at least one
    verification method.
2.  Every behavioral mandatory requirement SHOULD have an executable
    `CT-*` or a documented reason why inspection is the appropriate
    method.
3.  `No direct AOF-INV mapping asserted` MUST NOT be represented as
    tested or conformant.
4.  A test MAY satisfy multiple Requirements only when the tested
    behavior is materially identical.
5.  A Requirement MAY require multiple methods/tests.
6.  Negative tests SHOULD be preferred for deny, fail-controlled,
    non-bypassability, revocation, stale-state, and isolation
    properties.
7.  Evidence MUST bind to the evaluated implementation/version/profile
    where applicable.
8.  Duplicate Requirement IDs with materially different wording MUST be
    reconciled before Semantic Freeze.

------------------------------------------------------------------------

## F.4 Coverage Summary

-   Explicit requirement occurrences extracted: **391**.
-   Unique canonical Requirement IDs: **319**.
-   Requirement IDs with duplicate definitions: **58**.
-   Reference `CT-*` tests discovered: **47**.
-   Canonical `AOF-INV-*` records discovered: **158**.
-   Requirements with conservative explicit test candidate: **73**.
-   Requirements requiring inspection-only or future explicit CT
    mapping: **246**.
-   Requirements with conservative invariant candidate: **227**.
-   Requirements pending invariant semantic review: **92**.

Semua **unique Requirement IDs** memiliki verification method class dan
required evidence class pada matrix di bawah.

------------------------------------------------------------------------

## F.5 Requirement-Test-Evidence Matrix

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Requirement      Normative Statement        Invariant       Explicit Test             Verification    Required Evidence               Mapping Status
                   (latest occurrence)                                                  Method                                          
  ---------------- -------------------------- --------------- ------------------------- --------------- ------------------------------- ------------------------------
  `AOF-ARCH-001`   `Proposal`, `Decision`,    `AOF-INV-012`   \`Verification path       ; no direct CT  sserted\``CI/TI/NT\` Archi      tecture configuration +
                   dan consequential `Action`                 defined                   a               control decision + TraceEvent   Explicit CT pending/inspection

  `AOF-ARCH-002`   Consequential `Action`     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``CI/TI/NT\` Architecture configuration +
                   tidak dapat bypass         AOF-INV mapping                                           control decision + TraceEvent   No direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-ARCH-003`   `Capability` atau          `AOF-INV-010`   \`Verification path       ; no direct CT  sserted\``CI/TI/NT\` Archi      tecture configuration +
                   technical tool access                      defined                   a               control decision + TraceEvent   Explicit CT pending/inspection
                   tidak                                                                                                                

  `AOF-ARCH-004`   Mandatory control result   `AOF-INV-012`   \`Verification path       ; no direct CT  sserted\``CI/TI/NT\` Archi      tecture configuration +
                   `Pending` atau unknown                     defined                   a               control decision + TraceEvent   Explicit CT pending/inspection

  `AOF-ARCH-005`   Consequential state        `AOF-INV-006`   \`Verification path       ; no direct CT  sserted\``CI/TI/NT\` Archi      tecture configuration +
                   mutation menggunakan                       defined                   a               control decision + TraceEvent   Explicit CT pending/inspection
                   controlled                                                                                                           

  `AOF-ARCH-006`   Consequential action dan   `AOF-INV-009`   \`Verification path       ; no direct CT  sserted\``CI/TI/NT\` Archi      tecture configuration +
                   transition menghasilkan                    defined                   a               control decision + TraceEvent   Explicit CT pending/inspection

  `AOF-ARCH-007`   Implementation memiliki    `AOF-INV-005`   \`Verification path       ; no direct CT  sserted\``CI/TI/NT\` Archi      tecture configuration +
                   authoritative                              defined                   a               control decision + TraceEvent   Explicit CT pending/inspection
                   orchestration                                                                                                        

  `AOF-ARCH-008`   Revoked/expired authority  `AOF-INV-009`   \`Verification path       ; no direct CT  sserted\``CI/TI/NT\` Archi      tecture configuration +
                   tidak dapat digunakan                      defined                   a               control decision + TraceEvent   Explicit CT pending/inspection

  `AOF-ARCH-009`   Effect Boundary memiliki   `AOF-INV-004`   \`Verification path       ; no direct CT  sserted\``CI/TI/NT\` Archi      tecture configuration +
                   mechanism untuk memastikan                 defined                   a               control decision + TraceEvent   Explicit CT pending/inspection

  `AOF-ARCH-010`   Architecture dapat         \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``CI/TI/NT\` Architecture configuration +
                   mengembalikan              AOF-INV mapping                                           control decision + TraceEvent   No direct invariant asserted;
                   result/effect              a                                                                                         Explicit CT pending/inspection

  `AOF-ARCH-011`   Dynamic risk dapat memicu  \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``CI/TI/NT\` Architecture configuration +
                   control reevaluation.      AOF-INV mapping                                           control decision + TraceEvent   No direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-ARCH-012`   Delegation dan             `AOF-INV-008`   \`Verification path       ; no direct CT  sserted\``CI/TI/NT\` Archi      tecture configuration +
                   multi-orchestrator                         defined                   a               control decision + TraceEvent   Explicit CT pending/inspection
                   transfer                                                                                                             

  `AOF-ARCH-013`   Failure pada mandatory     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``CI/TI/NT\` Architecture configuration +
                   control tidak menghasilkan AOF-INV mapping                                           control decision + TraceEvent   No direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-ARCH-014`   Concurrency terhadap       \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``CI/TI/NT\` Architecture configuration +
                   shared consequential state AOF-INV mapping                                           control decision + TraceEvent   No direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-ARCH-015`   Verification result        `AOF-INV-008`   \`Verification path       ; no direct CT  sserted\``CI/TI/NT\` Archi      tecture configuration +
                   terhubung kembali ke                       defined                   a               control decision + TraceEvent   Explicit CT pending/inspection

  `AOF-ARCH-016`   Architecture dapat         \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``CI/TI/NT\` Architecture configuration +
                   mendukung independent      AOF-INV mapping                                           control decision + TraceEvent   No direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-ARCH-017`   Evidence provenance dapat  `AOF-INV-011`   \`Verification path       ; no direct CT  sserted\``CI/TI/NT\` Archi      tecture configuration +
                   dipertahankan melintasi                    defined                   a               control decision + TraceEvent   Explicit CT pending/inspection

  `AOF-LC-001`     Consequential Action MUST  `AOF-INV-025`   `CT-LC-009`               `AT/NT/TI`      Lifecycle decision +            Candidate mapped
                   require explicit governed                                                            StateTransition + TraceEvent    

  `AOF-LC-002`     Proposal MUST NOT be       `AOF-INV-013`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Lifec      ycle decision + Explicit CT
                   treated as authorized                      defined                   a               StateTransition + TraceEvent    pending/inspection
                   Decision                                                                                                             

  `AOF-LC-003`     Unknown/Pending mandatory  `AOF-INV-020`   `CT-LC-001`               `AT/NT/TI`      Lifecycle decision +            Candidate mapped
                   governance result MUST NOT                                                           StateTransition + TraceEvent    

  `AOF-LC-004`     Pre-execution Decision     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Lifecycle decision + No direct
                   MUST be revalidated when   AOF-INV mapping                                           StateTransition + TraceEvent    invariant asserted; Explicit
                                              a                                                                                         CT pending/inspection

  `AOF-LC-005`     Consequential execution    `AOF-INV-027`   `CT-LC-009`               `AT/NT/TI`      Lifecycle decision +            Candidate mapped
                   MUST cross controlled                                                                StateTransition + TraceEvent    
                   Effect                                                                                                               

  `AOF-LC-006`     Execution SHOULD produce   \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Lifecycle decision + No direct
                   sufficient effect Evidence AOF-INV mapping                                           StateTransition + TraceEvent    invariant asserted; Explicit
                                              a                                                                                         CT pending/inspection

  `AOF-LC-007`     `Inconclusive` mandatory   `AOF-INV-017`   `CT-LC-003`               `AT/NT/TI`      Lifecycle decision +            Candidate mapped
                   Verification MUST NOT be                                                             StateTransition + TraceEvent    

  `AOF-LC-008`     Failure MUST NOT authorize `AOF-INV-018`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Lifec      ycle decision + Explicit CT
                   bypass of mandatory                        defined                   a               StateTransition + TraceEvent    pending/inspection

  `AOF-LC-009`     Unknown/partial effect     `AOF-INV-027`   `CT-LC-004`               `AT/NT/TI`      Lifecycle decision +            Candidate mapped
                   SHOULD be reconciled                                                                 StateTransition + TraceEvent    
                   before                                                                                                               

  `AOF-LC-010`     Retry MUST be bounded dan  `AOF-INV-020`   `CT-LC-001`               `AT/NT/TI`      Lifecycle decision +            Candidate mapped
                   governance-eligible.                                                                 StateTransition + TraceEvent    

  `AOF-LC-011`     Replan MUST re-evaluate    `AOF-INV-021`   `CT-LC-001`               `AT/NT/TI`      Lifecycle decision +            Candidate mapped
                   applicable governance                                                                StateTransition + TraceEvent    

  `AOF-LC-012`     Recovery Action MUST be    `AOF-INV-017`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Lifec      ycle decision + Explicit CT
                   independently eligible for                 defined                   a               StateTransition + TraceEvent    pending/inspection

  `AOF-LC-013`     Cancellation MUST NOT be   `AOF-INV-023`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Lifec      ycle decision + Explicit CT
                   represented as rollback                    defined                   a               StateTransition + TraceEvent    pending/inspection

  `AOF-LC-014`     Successful termination     `AOF-INV-024`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Lifec      ycle decision + Explicit CT
                   MUST require Goal                          defined                   a               StateTransition + TraceEvent    pending/inspection
                   satisfaction                                                                                                         

  `AOF-LC-015`     Consequential State        `AOF-INV-024`   `CT-LC-009`               `AT/NT/TI`      Lifecycle decision +            Candidate mapped
                   mutation MUST occur                                                                  StateTransition + TraceEvent    
                   through                                                                                                              

  `AOF-LC-016`     Resume MUST revalidate     `AOF-INV-020`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Lifec      ycle decision + Explicit CT
                   stale governance                           defined                   a               StateTransition + TraceEvent    pending/inspection
                   dependencies.                                                                                                        

  `AOF-LC-017`     Mandatory Safety Kernel    \`No direct     sserted\``CT-LC-008\`     \`AT/N          T/TI\` Lifecycle decision +     Invariant review
                   failure MUST NOT fail      AOF-INV mapping                                           StateTransition + TraceEvent    
                   open.                      a                                                                                         

  `AOF-LC-018`     Lifecycle MUST preserve    `AOF-INV-023`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Lifec      ycle decision + Explicit CT
                   traceable correlation                      defined                   a               StateTransition + TraceEvent    pending/inspection
                   across                                                                                                               

  `AOF-LC-019`     Human unavailability MUST  `AOF-INV-028`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Lifec      ycle decision + Explicit CT
                   NOT become implicit                        defined                   a               StateTransition + TraceEvent    pending/inspection

  `AOF-LC-020`     Performance optimization   `AOF-INV-025`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Lifec      ycle decision + Explicit CT
                   MUST NOT weaken mandatory                  defined                   a               StateTransition + TraceEvent    pending/inspection

  `AOF-LC-021`     Dynamic Authority          \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Lifecycle decision + No direct
                   revocation/expiry MUST be  AOF-INV mapping                                           StateTransition + TraceEvent    invariant asserted; Explicit
                   respected                  a                                                                                         CT pending/inspection

  `AOF-LC-022`     Material Risk change       \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Lifecycle decision + No direct
                   SHOULD trigger applicable  AOF-INV mapping                                           StateTransition + TraceEvent    invariant asserted; Explicit
                                              a                                                                                         CT pending/inspection

  `AOF-LC-023`     Concurrent consequential   `AOF-INV-025`   `CT-LC-009`               `AT/NT/TI`      Lifecycle decision +            Candidate mapped
                   transitions MUST detect                                                              StateTransition + TraceEvent    

  `AOF-LC-024`     Terminal Outcome MUST      `AOF-INV-026`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Lifec      ycle decision + Explicit CT
                   preserve residual Risk,                    defined                   a               StateTransition + TraceEvent    pending/inspection

  `AOF-AGT-001`    Agent MUST operate as      `AOF-INV-034`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Agent      Explicit CT pending/inspection
                   bounded actor within                       defined                   a               assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-002`    Capability MUST NOT be     `AOF-INV-034`   `CT-AGT-001`              `AT/NT/TI`      Agent                           Candidate mapped
                   treated as Authority.                                                                assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-003`    Agent MUST NOT             `AOF-INV-032`   `CT-AGT-009`              `AT/NT/TI`      Agent                           Candidate mapped
                   self-authorize                                                                       assignment/configuration +      
                   consequential Action.                                                                Decision + TraceEvent           

  `AOF-AGT-004`    Agent assignment MUST      \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Agent No direct invariant
                   satisfy applicable hard    AOF-INV mapping                                           assignment/configuration +      asserted; Explicit CT
                                              a                                                         Decision + TraceEvent           pending/inspection

  `AOF-AGT-005`    Risk-sensitive Task        `AOF-INV-041`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Agent      Explicit CT pending/inspection
                   assignment MUST consider                   defined                   a               assignment/configuration +      
                   Agent                                                                                Decision + TraceEvent           

  `AOF-AGT-006`    Context supplied to Agent  `AOF-INV-009`   `CT-AGT-003`              `AT/NT/TI`      Agent                           Candidate mapped
                   SHOULD follow                                                                        assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-007`    Context or Memory          `AOF-INV-009`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Agent      Explicit CT pending/inspection
                   possession MUST NOT create                 defined                   a               assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-008`    Trust/confidence MUST NOT  `AOF-INV-034`   `CT-AGT-009`              `AT/NT/TI`      Agent                           Candidate mapped
                   replace Authority or                                                                 assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-009`    Agent output MUST NOT be   `AOF-INV-034`   `CT-AGT-009`              `AT/NT/TI`      Agent                           Candidate mapped
                   treated as authorized                                                                assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-010`    Technical tool/credential  `AOF-INV-037`   `CT-AGT-004`              `AT/NT/TI`      Agent                           Candidate mapped
                   access MUST NOT be treated                                                           assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-011`    Delegation MUST NOT expand `AOF-INV-034`   `CT-AGT-009`              `AT/NT/TI`      Agent                           Candidate mapped
                   inherited Authority.                                                                 assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-012`    Delegation MUST preserve   `AOF-INV-038`   `CT-AGT-005`              `AT/NT/TI`      Agent                           Candidate mapped
                   applicable mandatory                                                                 assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-013`    Delegation MUST NOT be     `AOF-INV-034`   `CT-AGT-009`              `AT/NT/TI`      Agent                           Candidate mapped
                   used for Authority                                                                   assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-014`    Execution Authority MUST   `AOF-INV-031`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Agent      Explicit CT pending/inspection
                   NOT automatically imply                    defined                   a               assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-015`    Mandatory Policy           `AOF-INV-041`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Agent      Explicit CT pending/inspection
                   enforcement MUST NOT rely                  defined                   a               assignment/configuration +      
                   solely on                                                                            Decision + TraceEvent           

  `AOF-AGT-016`    Agent identity used for    `AOF-INV-038`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Agent      Explicit CT pending/inspection
                   consequential governance                   defined                   a               assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-017`    Independent verifier       `AOF-INV-035`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Agent      Explicit CT pending/inspection
                   assignment MUST satisfy                    defined                   a               assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-018`    Agent local State MUST NOT `AOF-INV-037`   `CT-AGT-009`              `AT/NT/TI`      Agent                           Candidate mapped
                   supersede authoritative                                                              assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-019`    Agent restart/replacement  `AOF-INV-043`   `CT-AGT-007`              `AT/NT/TI`      Agent                           Candidate mapped
                   MUST revalidate stale                                                                assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-020`    Conformance MUST NOT       `AOF-INV-040`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Agent      Explicit CT pending/inspection
                   require disclosure of                      defined                   a               assignment/configuration +      
                   private                                                                              Decision + TraceEvent           

  `AOF-AGT-021`    Material model/service     `AOF-INV-037`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Agent      Explicit CT pending/inspection
                   substitution SHOULD                        defined                   a               assignment/configuration +      
                   trigger                                                                              Decision + TraceEvent           

  `AOF-AGT-022`    Compromised/suspect Agent  \`No direct     sserted\``CT-AGT-011\`    \`AT/N          T/TI\` Agent                    Invariant review
                   SHOULD be containable      AOF-INV mapping                                           assignment/configuration +      
                                              a                                                         Decision + TraceEvent           

  `AOF-AGT-023`    Optimization for           `AOF-INV-046`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Agent      Explicit CT pending/inspection
                   cost/latency MUST NOT                      defined                   a               assignment/configuration +      
                   override                                                                             Decision + TraceEvent           

  `AOF-AGT-024`    Recursive delegation       `AOF-INV-038`   `CT-AGT-005`              `AT/NT/TI`      Agent                           Candidate mapped
                   SHOULD be bounded.                                                                   assignment/configuration +      
                                                                                                        Decision + TraceEvent           

  `AOF-AGT-025`    Human Agent MUST remain    \`No direct     sserted\``CT-AGT-009\`    \`AT/N          T/TI\` Agent                    Invariant review
                   subject to applicable      AOF-INV mapping                                           assignment/configuration +      
                                              a                                                         Decision + TraceEvent           

  `AOF-AGT-026`    Orchestrator Agent MUST    \`No direct     sserted\``CT-AGT-008\`    \`AT/N          T/TI\` Agent                    Invariant review
                   NOT be treated as implicit AOF-INV mapping                                           assignment/configuration +      
                                              a                                                         Decision + TraceEvent           

  `AOF-AUTH-001`   Authority-sensitive        `AOF-INV-030`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority
                   consequential Action MUST                  defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-AUTH-002`   Missing grant MUST NOT     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` AuthorityGrant + Authority
                   menghasilkan implicit      AOF-INV mapping                                           evaluation + Decision +         Duplicate-ID wording review;
                   allow.                     a                                                         TraceEvent                      Invariant review; Explicit CT
                                                                                                                                        pending/inspection

  `AOF-AUTH-003`   Effective permission MUST  `AOF-INV-008`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority
                   NOT melebihi grant scope.                  defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-AUTH-004`   Hanya valid active         `AOF-INV-030`   `CT-AUTH-001`             `AT/NT/TI`      AuthorityGrant + Authority      Duplicate-ID wording review
                   authority yang dapat                                                                 evaluation + Decision +         
                   memenuhi                                                                             TraceEvent                      

  `AOF-AUTH-005`   Policy allow MUST NOT      `AOF-INV-050`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority
                   menggantikan missing                       defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-AUTH-006`   Approval MUST NOT          `AOF-INV-051`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority
                   diinterpretasikan sebagai                  defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-AUTH-007`   Technical reachability     `AOF-INV-030`   `CT-AUTH-001`             `AT/NT/TI`      AuthorityGrant + Authority      Candidate mapped
                   MUST NOT menjadi                                                                     evaluation + Decision +         
                                                                                                        TraceEvent                      

  `AOF-AUTH-008`   Authority issuance MUST    `AOF-INV-055`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority
                   memiliki traceable                         defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-AUTH-009`   Delegated authority MUST   `AOF-INV-030`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority
                   berada dalam delegator's                   defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-AUTH-010`   Non-delegable authority    `AOF-INV-030`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority
                   MUST NOT disubdelegasikan.                 defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-AUTH-011`   Delegation MUST NOT        `AOF-INV-038`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority
                   menghasilkan privilege                     defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-AUTH-012`   Quantity-bounded authority `AOF-INV-030`   `CT-AUTH-001`             `AT/NT/TI`      AuthorityGrant + Authority      Duplicate-ID wording review
                   MUST aman terhadap                                                                   evaluation + Decision +         
                                                                                                        TraceEvent                      

  `AOF-AUTH-013`   Read/access authority MUST `AOF-INV-030`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority
                   NOT otomatis memberikan                    defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-AUTH-014`   Agent MUST NOT             `AOF-INV-049`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority
                   self-elevate authority                     defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                   berdasarkan                                                                          TraceEvent                      Explicit CT pending/inspection

  `AOF-AUTH-015`   Replacement agent MUST     `AOF-INV-053`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority
                   dievaluasi ulang.                          defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-AUTH-016`   Revoked, expired,          `AOF-INV-008`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority Explicit
                   suspended, atau consumed                   defined                   a               evaluation + Decision +         CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-AUTH-017`   Material replan yang       `AOF-INV-030`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority Explicit
                   mengubah authority scope                   defined                   a               evaluation + Decision +         CT pending/inspection
                   MUST                                                                                 TraceEvent                      

  `AOF-AUTH-018`   Delegation chain MUST      `AOF-INV-038`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority Explicit
                   traceable.                                 defined                   a               evaluation + Decision +         CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-AUTH-019`   High-risk effect SHOULD    `AOF-INV-048`   `CT-AUTH-001`             `AT/NT/TI`      AuthorityGrant + Authority      Candidate mapped
                   melakukan authority                                                                  evaluation + Decision +         
                                                                                                        TraceEvent                      

  `AOF-AUTH-020`   High-assurance profile     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` AuthorityGrant + Authority No
                   MUST menentukan protection AOF-INV mapping                                           evaluation + Decision +         direct invariant asserted;
                                              a                                                         TraceEvent                      Explicit CT pending/inspection

  `AOF-AUTH-021`   High-assurance authority   `AOF-INV-030`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      rityGrant + Authority Explicit
                   evaluation evidence MUST                   defined                   a               evaluation + Decision +         CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-POL-001`    Consequential Action MUST  \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/CI\` Policy object/version + Policy
                   dievaluasi terhadap        AOF-INV mapping                                           evaluation + Decision +         Duplicate-ID wording review;
                                              a                                                         TraceEvent                      Invariant review; Explicit CT
                                                                                                                                        pending/inspection

  `AOF-POL-002`    Unknown mandatory policy   `AOF-INV-063`   `CT-POL-002`              `AT/NT/CI`      Policy object/version + Policy  Duplicate-ID wording review
                   state MUST NOT menjadi                                                               evaluation + Decision +         
                                                                                                        TraceEvent                      

  `AOF-POL-003`    Applicable consequential   `AOF-INV-062`   \`Verification path       ; no direct CT  sserted\``AT/NT/CI\` Polic      y object/version + Policy
                   policy version MUST                        defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-POL-004`    Policy conflict resolution `AOF-INV-062`   \`Verification path       ; no direct CT  sserted\``AT/NT/CI\` Polic      y object/version + Policy
                   MUST deterministic dan                     defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-POL-005`    Non-default precedence     `AOF-INV-061`   \`Verification path       ; no direct CT  sserted\``AT/NT/CI\` Polic      y object/version + Policy
                   MUST explicit.                             defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-POL-006`    Mandatory policy           `AOF-INV-057`   `CT-POL-002`              `AT/NT/CI`      Policy object/version + Policy  Duplicate-ID wording review
                   constraints MUST survive                                                             evaluation + Decision +         
                                                                                                        TraceEvent                      

  `AOF-POL-007`    Policy override MUST       `AOF-INV-057`   \`Verification path       ; no direct CT  sserted\``AT/NT/CI\` Polic      y object/version + Policy
                   explicit, authorized,                      defined                   a               evaluation + Decision +         Duplicate-ID wording review;
                   scoped,                                                                              TraceEvent                      Explicit CT pending/inspection

  `AOF-POL-008`    Risk classification MUST   \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/CI\` Policy object/version + Policy
                   NOT menciptakan            AOF-INV mapping                                           evaluation + Decision +         Duplicate-ID wording review;
                   permission.                a                                                         TraceEvent                      Invariant review; Explicit CT
                                                                                                                                        pending/inspection

  `AOF-POL-009`    Mandatory consequential    \`No direct     sserted\``CT-POL-002\`    \`AT/N          T/CI\` Policy object/version    \+ Policy Duplicate-ID wording
                   policy MUST NOT bergantung AOF-INV mapping                                           evaluation + Decision +         review; Invariant review
                                              a                                                         TraceEvent                      

  `AOF-POL-010`    Policy change material     `AOF-INV-056`   \`Verification path       ; no direct CT  sserted\``AT/NT/CI\` Polic      y object/version + Policy
                   terhadap pending action                    defined                   a               evaluation + Decision +         Explicit CT pending/inspection
                   MUST                                                                                 TraceEvent                      

  `AOF-POL-011`    Policy evaluation MUST     `AOF-INV-057`   \`Verification path       ; no direct CT  sserted\``AT/NT/CI\` Polic      y object/version + Policy
                   menggunakan authoritative                  defined                   a               evaluation + Decision +         Explicit CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-POL-012`    Delegation MUST preserve   \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/CI\` Policy object/version + Policy
                   applicable policy          AOF-INV mapping                                           evaluation + Decision +         No direct invariant asserted;
                                              a                                                         TraceEvent                      Explicit CT pending/inspection

  `AOF-POL-013`    Replan yang mengubah       `AOF-INV-057`   \`Verification path       ; no direct CT  sserted\``AT/NT/CI\` Polic      y object/version + Policy
                   policy scope MUST memicu                   defined                   a               evaluation + Decision +         Explicit CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-POL-014`    Emergency policy MUST      `AOF-INV-062`   \`Verification path       ; no direct CT  sserted\``AT/NT/CI\` Polic      y object/version + Policy
                   bounded dan traceable.                     defined                   a               evaluation + Decision +         Explicit CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-POL-015`    Policy decision MUST       `AOF-INV-062`   \`Verification path       ; no direct CT  sserted\``AT/NT/CI\` Polic      y object/version + Policy
                   memiliki sufficient record                 defined                   a               evaluation + Decision +         Explicit CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-POL-016`    High-assurance policy      `AOF-INV-064`   \`Verification path       ; no direct CT  sserted\``AT/NT/CI\` Polic      y object/version + Policy
                   store/evaluator MUST                       defined                   a               evaluation + Decision +         Explicit CT pending/inspection
                   memiliki                                                                             TraceEvent                      

  `AOF-POL-017`    High-assurance Effect      \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/CI\` Policy object/version + Policy
                   Boundary SHOULD memastikan AOF-INV mapping                                           evaluation + Decision +         No direct invariant asserted;
                                              a                                                         TraceEvent                      Explicit CT pending/inspection

  `AOF-POL-018`    High-assurance policy      \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/CI\` Policy object/version + Policy
                   overrides MUST subject to  AOF-INV mapping                                           evaluation + Decision +         No direct invariant asserted;
                                              a                                                         TraceEvent                      Explicit CT pending/inspection

  `AOF-RISK-001`   Risk classification method `AOF-INV-066`   \`Verification path       ; no direct CT  sserted\``AT/DI/TI\` RiskA      ssessment + control
                   MUST explicit.                             defined                   a               decision + TraceEvent           Duplicate-ID wording review;
                                                                                                                                        Explicit CT pending/inspection

  `AOF-RISK-002`   Risk result MUST NOT       \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/DI/TI\` RiskAssessment + control
                   menggantikan missing       AOF-INV mapping                                           decision + TraceEvent           Duplicate-ID wording review;
                                              a                                                                                         Invariant review; Explicit CT
                                                                                                                                        pending/inspection

  `AOF-RISK-003`   Material risk change MUST  `AOF-INV-069`   \`Verification path       ; no direct CT  sserted\``AT/DI/TI\` RiskA      ssessment + control Explicit
                   memicu control                             defined                   a               decision + TraceEvent           CT pending/inspection

  `AOF-RISK-004`   Risk assessor MUST NOT     `AOF-INV-074`   \`Verification path       ; no direct CT  sserted\``AT/DI/TI\` RiskA      ssessment + control
                   otomatis dianggap risk                     defined                   a               decision + TraceEvent           Duplicate-ID wording review;
                                                                                                                                        Explicit CT pending/inspection

  `AOF-RISK-005`   Applicable Risk Profile    `AOF-INV-071`   \`Verification path       ; no direct CT  sserted\``AT/DI/TI\` RiskA      ssessment + control Explicit
                   MUST menentukan risk                       defined                   a               decision + TraceEvent           CT pending/inspection
                   levels                                                                                                               

  `AOF-RISK-006`   Required risk assessment   `AOF-INV-070`   \`Verification path       ; no direct CT  sserted\``AT/DI/TI\` RiskA      ssessment + control Explicit
                   yang unresolved MUST NOT                   defined                   a               decision + TraceEvent           CT pending/inspection

  `AOF-RISK-007`   High/Critical              `AOF-INV-071`   `CT-RISK-002`             `AT/DI/TI`      RiskAssessment + control        Candidate mapped
                   consequential risk                                                                   decision + TraceEvent           
                   decision MUST                                                                                                        

  `AOF-RISK-008`   Residual risk MUST         `AOF-INV-069`   `CT-RISK-002`             `AT/DI/TI`      RiskAssessment + control        Candidate mapped
                   mempertimbangkan                                                                     decision + TraceEvent           
                   applicable                                                                                                           

  `AOF-RISK-009`   Material replan MUST       `AOF-INV-073`   \`Verification path       ; no direct CT  sserted\``AT/DI/TI\` RiskA      ssessment + control Explicit
                   memicu risk reassessment.                  defined                   a               decision + TraceEvent           CT pending/inspection

  `AOF-RISK-010`   Partial effect MUST memicu `AOF-INV-073`   \`Verification path       ; no direct CT  sserted\``AT/DI/TI\` RiskA      ssessment + control Explicit
                   state reconciliation dan                   defined                   a               decision + TraceEvent           CT pending/inspection

  `AOF-RISK-011`   Risk acceptance MUST       `AOF-INV-066`   \`Verification path       ; no direct CT  sserted\``AT/DI/TI\` RiskA      ssessment + control Explicit
                   scoped, authorized, dan                    defined                   a               decision + TraceEvent           CT pending/inspection

  `AOF-RISK-012`   Non-acceptable risk MUST   `AOF-INV-072`   \`Verification path       ; no direct CT  sserted\``AT/DI/TI\` RiskA      ssessment + control Explicit
                   menghasilkan reject/abort                  defined                   a               decision + TraceEvent           CT pending/inspection

  `AOF-RISK-013`   Retry threshold SHOULD     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/DI/TI\` RiskAssessment + control No
                   memicu                     AOF-INV mapping                                           decision + TraceEvent           direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-RISK-014`   Risk-sensitive Agent       `AOF-INV-066`   \`Verification path       ; no direct CT  sserted\``AT/DI/TI\` RiskA      ssessment + control Explicit
                   selection SHOULD                           defined                   a               decision + TraceEvent           CT pending/inspection

  `AOF-RISK-015`   High risk MUST menggunakan `AOF-INV-070`   \`Verification path       ; no direct CT  sserted\``AT/DI/TI\` RiskA      ssessment + control Explicit
                   independent verification                   defined                   a               decision + TraceEvent           CT pending/inspection

  `AOF-RISK-016`   Critical risk MUST         `AOF-INV-071`   `CT-RISK-002`             `AT/DI/TI`      RiskAssessment + control        Candidate mapped
                   menggunakan independent                                                              decision + TraceEvent           

  `AOF-RISK-017`   High-assurance Risk        `AOF-INV-070`   `CT-RISK-001`             `AT/DI/TI`      RiskAssessment + control        Candidate mapped
                   Profile MUST menentukan                                                              decision + TraceEvent           

  `AOF-RISK-018`   High-assurance             `AOF-INV-070`   `CT-RISK-001`             `AT/DI/TI`      RiskAssessment + control        Candidate mapped
                   implementation MUST                                                                  decision + TraceEvent           
                   menentukan                                                                                                           

  `AOF-EVD-001`    Consequential verification `AOF-INV-080`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Evide         nce object + Duplicate-ID
                   evidence MUST memiliki                     defined                   a               provenance/integrity metadata   wording review; Explicit CT
                                                                                                                                        pending/inspection

  `AOF-EVD-002`    Material derived evidence  `AOF-INV-084`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Evide         nce object + Duplicate-ID
                   MUST preserve derivation                   defined                   a               provenance/integrity metadata   wording review; Explicit CT
                                                                                                                                        pending/inspection

  `AOF-EVD-003`    Stale evidence MUST NOT    \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/TI\`    Evidence object + Duplicate-ID
                   menjadi sole support jika  AOF-INV mapping                                           provenance/integrity metadata   wording review; Invariant
                                              a                                                                                         review; Explicit CT
                                                                                                                                        pending/inspection

  `AOF-EVD-004`    Inadmissible evidence MUST \`No direct     sserted\``CT-EVD-001\`    \`AT/T          I\` Evidence object +           Duplicate-ID wording review;
                   NOT dihitung sebagai       AOF-INV mapping                                           provenance/integrity metadata   Invariant review
                                              a                                                                                         

  `AOF-EVD-005`    Material contradiction     `AOF-INV-077`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Evide         nce object + Duplicate-ID
                   MUST represented atau                      defined                   a               provenance/integrity metadata   wording review; Explicit CT
                                                                                                                                        pending/inspection

  `AOF-EVD-006`    Evidence presence MUST NOT \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/TI\`    Evidence object + No direct
                   otomatis dianggap          AOF-INV mapping                                           provenance/integrity metadata   invariant asserted; Explicit
                                              a                                                                                         CT pending/inspection

  `AOF-EVD-007`    Evidence MUST dapat        \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/TI\`    Evidence object + No direct
                   dikaitkan dengan relevant  AOF-INV mapping                                           provenance/integrity metadata   invariant asserted; Explicit
                                              a                                                                                         CT pending/inspection

  `AOF-EVD-008`    Consequential effect       \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/TI\`    Evidence object + No direct
                   SHOULD menghasilkan        AOF-INV mapping                                           provenance/integrity metadata   invariant asserted; Explicit
                   observable                 a                                                                                         CT pending/inspection

  `AOF-EVD-009`    Retry MUST preserve        `AOF-INV-084`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Evide         nce object + Explicit CT
                   material prior-attempt                     defined                   a               provenance/integrity metadata   pending/inspection
                   evidence.                                                                                                            

  `AOF-EVD-010`    Replan MUST reevaluate     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/TI\`    Evidence object + No direct
                   applicability of reused    AOF-INV mapping                                           provenance/integrity metadata   invariant asserted; Explicit
                                              a                                                                                         CT pending/inspection

  `AOF-EVD-011`    Evidence disclosure MUST   `AOF-INV-083`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Evide         nce object + Explicit CT
                   tunduk pada applicable                     defined                   a               provenance/integrity metadata   pending/inspection

  `AOF-EVD-012`    Evidence correction SHOULD `AOF-INV-084`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Evide         nce object + Explicit CT
                   preserve                                   defined                   a               provenance/integrity metadata   pending/inspection

  `AOF-EVD-013`    Required evidence          `AOF-INV-077`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Evide         nce object + Explicit CT
                   retention MUST mengikuti                   defined                   a               provenance/integrity metadata   pending/inspection

  `AOF-EVD-014`    Evidence aggregation MUST  `AOF-INV-077`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Evide         nce object + Explicit CT
                   NOT silently erase                         defined                   a               provenance/integrity metadata   pending/inspection

  `AOF-EVD-015`    High-risk evidence profile `AOF-INV-081`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Evide         nce object + Explicit CT
                   MUST menentukan                            defined                   a               provenance/integrity metadata   pending/inspection

  `AOF-EVD-016`    High-assurance             \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/TI\`    Evidence object + No direct
                   consequential evidence     AOF-INV mapping                                           provenance/integrity metadata   invariant asserted; Explicit
                   MUST memiliki              a                                                                                         CT pending/inspection

  `AOF-EVD-017`    Independent verification   `AOF-INV-077`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Evide         nce object + Explicit CT
                   MUST NOT bergantung hanya                  defined                   a               provenance/integrity metadata   pending/inspection

  `AOF-EVD-018`    High-assurance evidence    \`No direct     sserted\``CT-EVD-001\`    \`AT/T          I\` Evidence object +           Invariant review
                   chain MUST dapat           AOF-INV mapping                                           provenance/integrity metadata   
                                              a                                                                                         

  `AOF-VER-001`    Required verification MUST `AOF-INV-092`   `CT-VER-001`              `AT/NT/TI`      Verification record +           Candidate mapped
                   menghasilkan explicit                                                                criteria + Evidence             
                                                                                                        references + TraceEvent         

  `AOF-VER-002`    Consequential verification `AOF-INV-091`   `CT-VER-001`              `AT/NT/TI`      Verification record +           Candidate mapped
                   MUST memiliki                                                                        criteria + Evidence             
                                                                                                        references + TraceEvent         

  `AOF-VER-003`    Self-verification alone    `AOF-INV-091`   `CT-VER-001`              `AT/NT/TI`      Verification record +           Duplicate-ID wording review
                   MUST NOT memenuhi                                                                    criteria + Evidence             
                                                                                                        references + TraceEvent         

  `AOF-VER-004`    High/Critical risk MUST    `AOF-INV-085`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Verif      ication record + Duplicate-ID
                   memiliki explicit                          defined                   a               criteria + Evidence             wording review; Explicit CT
                                                                                                        references + TraceEvent         pending/inspection

  `AOF-VER-005`    Conflicting verification   `AOF-INV-085`   `CT-VER-001`              `AT/NT/TI`      Verification record +           Duplicate-ID wording review
                   results MUST menggunakan                                                             criteria + Evidence             
                                                                                                        references + TraceEvent         

  `AOF-VER-006`    Required verification MUST `AOF-INV-092`   `CT-VER-001`              `AT/NT/TI`      Verification record +           Duplicate-ID wording review
                   NOT purely                                                                           criteria + Evidence             
                                                                                                        references + TraceEvent         

  `AOF-VER-007`    `Inconclusive` MUST NOT    `AOF-INV-093`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Verif      ication record + Explicit CT
                   diperlakukan sebagai                       defined                   a               criteria + Evidence             pending/inspection
                                                                                                        references + TraceEvent         

  `AOF-VER-008`    Required verification MUST `AOF-INV-092`   `CT-VER-001`              `AT/NT/TI`      Verification record +           Candidate mapped
                   evaluate applicable                                                                  criteria + Evidence             
                                                                                                        references + TraceEvent         

  `AOF-VER-009`    Verification result MUST   `AOF-INV-092`   `CT-VER-001`              `AT/NT/TI`      Verification record +           Candidate mapped
                   bound ke relevant                                                                    criteria + Evidence             
                                                                                                        references + TraceEvent         

  `AOF-VER-010`    Material subject change    `AOF-INV-090`   `CT-VER-002`              `AT/NT/TI`      Verification record +           Candidate mapped
                   MUST memicu                                                                          criteria + Evidence             
                   re-verification.                                                                     references + TraceEvent         

  `AOF-VER-011`    Verification failure MUST  `AOF-INV-091`   `CT-VER-001`              `AT/NT/TI`      Verification record +           Candidate mapped
                   NOT silently fail-open.                                                              criteria + Evidence             
                                                                                                        references + TraceEvent         

  `AOF-VER-012`    Mandatory completion       `AOF-INV-090`   `CT-VER-002`              `AT/NT/TI`      Verification record +           Candidate mapped
                   verification MUST                                                                    criteria + Evidence             
                   satisfied                                                                            references + TraceEvent         

  `AOF-VER-013`    Replan/retry MUST          `AOF-INV-090`   `CT-VER-002`              `AT/NT/TI`      Verification record +           Candidate mapped
                   reevaluate verification                                                              criteria + Evidence             
                                                                                                        references + TraceEvent         

  `AOF-VER-014`    Verification result MUST   `AOF-INV-092`   `CT-VER-001`              `AT/NT/TI`      Verification record +           Candidate mapped
                   kembali melalui governed                                                             criteria + Evidence             
                                                                                                        references + TraceEvent         

  `AOF-VER-015`    High risk MUST menggunakan `AOF-INV-088`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Verif      ication record + Explicit CT
                   verifier independence                      defined                   a               criteria + Evidence             pending/inspection
                                                                                                        references + TraceEvent         

  `AOF-VER-016`    Critical risk MUST         `AOF-INV-085`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Verif      ication record + Explicit CT
                   menggunakan independent                    defined                   a               criteria + Evidence             pending/inspection
                                                                                                        references + TraceEvent         

  `AOF-VER-017`    High-assurance             `AOF-INV-092`   `CT-VER-001`              `AT/NT/TI`      Verification record +           Candidate mapped
                   verification provenance                                                              criteria + Evidence             
                   MUST cukup                                                                           references + TraceEvent         

  `AOF-VER-018`    High-assurance profile     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Verification record + No
                   MUST menentukan behavior   AOF-INV mapping                                           criteria + Evidence             direct invariant asserted;
                                              a                                                         references + TraceEvent         Explicit CT pending/inspection

  `AOF-ST-001`     Consequential decision     `AOF-INV-095`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      ritative State + Duplicate-ID
                   MUST menggunakan                           defined                   a               StateTransition + TraceEvent    wording review; Explicit CT
                   authoritative                                                                                                        pending/inspection

  `AOF-ST-002`     Consequential state        `AOF-INV-096`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      ritative State + Duplicate-ID
                   mutation MUST menggunakan                  defined                   a               StateTransition + TraceEvent    wording review; Explicit CT
                                                                                                                                        pending/inspection

  `AOF-ST-003`     Material stale-state use   \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Authoritative State +
                   MUST dideteksi atau        AOF-INV mapping                                           StateTransition + TraceEvent    Duplicate-ID wording review;
                                              a                                                                                         Invariant review; Explicit CT
                                                                                                                                        pending/inspection

  `AOF-ST-004`     Shared consequential state \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Authoritative State +
                   MUST memiliki conflict     AOF-INV mapping                                           StateTransition + TraceEvent    Duplicate-ID wording review;
                                              a                                                                                         Invariant review; Explicit CT
                                                                                                                                        pending/inspection

  `AOF-TRC-001`    Consequential transition   \`No direct     sserted\``CT-TRC-001\`    \`AT/T          I\` TraceEvent chain +          Invariant review
                   MUST menghasilkan          AOF-INV mapping                                           integrity/correlation evidence  
                                              a                                                                                         

  `AOF-ST-005`     Invalid lifecycle          `AOF-INV-100`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      ritative State + Explicit CT
                   transition MUST NOT                        defined                   a               StateTransition + TraceEvent    pending/inspection
                   silently                                                                                                             

  `AOF-ST-006`     Agent private memory MUST  \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Authoritative State + No
                   NOT menjadi sole           AOF-INV mapping                                           StateTransition + TraceEvent    direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-ST-007`     Partial commit MUST        `AOF-INV-100`   `CT-STATE-002`            `AT/NT/TI`      Authoritative State +           Candidate mapped
                   represented sebagai                                                                  StateTransition + TraceEvent    

  `AOF-ST-008`     Replay yang dapat          `AOF-INV-100`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      ritative State + Explicit CT
                   menghasilkan new effect                    defined                   a               StateTransition + TraceEvent    pending/inspection
                   MUST                                                                                                                 

  `AOF-ST-009`     Retry MUST                 \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Authoritative State + No
                   mempertimbangkan current   AOF-INV mapping                                           StateTransition + TraceEvent    direct invariant asserted;
                   state dan prior            a                                                                                         Explicit CT pending/inspection

  `AOF-ST-010`     Material replan MUST       `AOF-INV-099`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      ritative State + Explicit CT
                   invalidate/reassess                        defined                   a               StateTransition + TraceEvent    pending/inspection
                   affected                                                                                                             

  `AOF-ST-011`     High-risk Effect Boundary  `AOF-INV-099`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      ritative State + Explicit CT
                   SHOULD revalidate                          defined                   a               StateTransition + TraceEvent    pending/inspection

  `AOF-ST-012`     Cancellation MUST          \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Authoritative State + No
                   distinguish workflow       AOF-INV mapping                                           StateTransition + TraceEvent    direct invariant asserted;
                   termination                a                                                                                         Explicit CT pending/inspection

  `AOF-ST-013`     External state drift yang  \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Authoritative State + No
                   material MUST menghasilkan AOF-INV mapping                                           StateTransition + TraceEvent    direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-ST-014`     State transitions MUST     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Authoritative State + No
                   memiliki sufficient        AOF-INV mapping                                           StateTransition + TraceEvent    direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-ST-015`     High-assurance profile     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Authoritative State + No
                   MUST menentukan state      AOF-INV mapping                                           StateTransition + TraceEvent    direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-ST-016`     High-assurance shared      \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Authoritative State + No
                   state MUST memiliki        AOF-INV mapping                                           StateTransition + TraceEvent    direct invariant asserted;
                   defined                    a                                                                                         Explicit CT pending/inspection

  `AOF-ST-017`     High-assurance state       `AOF-INV-096`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Autho      ritative State + Explicit CT
                   mutation MUST support                      defined                   a               StateTransition + TraceEvent    pending/inspection

  `AOF-ST-018`     High-assurance permit      \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Authoritative State + No
                   SHOULD bind ke relevant    AOF-INV mapping                                           StateTransition + TraceEvent    direct invariant asserted;
                   state                      a                                                                                         Explicit CT pending/inspection

  `AOF-TRC-002`    Trace MUST identify        `AOF-INV-108`   `CT-TRC-001`              `AT/TI`         TraceEvent chain +              Candidate mapped
                   consequential                                                                        integrity/correlation evidence  

  `AOF-TRC-003`    Trace SHOULD menyediakan   `AOF-INV-108`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Trace         Event chain + Explicit CT
                   sufficient correlation                     defined                   a               integrity/correlation evidence  pending/inspection

  `AOF-TRC-004`    Trace MUST NOT memerlukan  `AOF-INV-109`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Trace         Event chain + Explicit CT
                   private chain-of-thought.                  defined                   a               integrity/correlation evidence  pending/inspection

  `AOF-TRC-005`    Trace correction MUST NOT  `AOF-INV-103`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Trace         Event chain + Explicit CT
                   silently erase historical                  defined                   a               integrity/correlation evidence  pending/inspection

  `AOF-TRC-006`    Mandatory trace failure    \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/TI\`    TraceEvent chain + No direct
                   MUST NOT disembunyikan     AOF-INV mapping                                           integrity/correlation evidence  invariant asserted; Explicit
                                              a                                                                                         CT pending/inspection

  `AOF-TRC-007`    Consequential decision     \`No direct     sserted\``CT-TRC-001\`    \`AT/T          I\` TraceEvent chain +          Invariant review
                   trace SHOULD merekam       AOF-INV mapping                                           integrity/correlation evidence  
                                              a                                                                                         

  `AOF-TRC-008`    Trace MUST tunduk pada     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/TI\`    TraceEvent chain + No direct
                   data classification/access AOF-INV mapping                                           integrity/correlation evidence  invariant asserted; Explicit
                                              a                                                                                         CT pending/inspection

  `AOF-TRC-009`    Required trace MUST        `AOF-INV-103`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Trace         Event chain + Explicit CT
                   retained sesuai applicable                 defined                   a               integrity/correlation evidence  pending/inspection

  `AOF-TRC-010`    Trace SHOULD preserve      `AOF-INV-084`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Trace         Event chain + Explicit CT
                   ordering/causal                            defined                   a               integrity/correlation evidence  pending/inspection
                   information                                                                                                          

  `AOF-TRC-011`    Effect with trace          `AOF-INV-103`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Trace         Event chain + Explicit CT
                   persistence failure MUST                   defined                   a               integrity/correlation evidence  pending/inspection
                   memicu                                                                                                               

  `AOF-TRC-012`    Trace export MUST          \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/TI\`    TraceEvent chain + No direct
                   diperlakukan sebagai       AOF-INV mapping                                           integrity/correlation evidence  invariant asserted; Explicit
                   governed                   a                                                                                         CT pending/inspection

  `AOF-TRC-013`    High-assurance trace MUST  \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/TI\`    TraceEvent chain + No direct
                   memiliki tamper-resistant  AOF-INV mapping                                           integrity/correlation evidence  invariant asserted; Explicit
                                              a                                                                                         CT pending/inspection

  `AOF-TRC-014`    High-assurance             `AOF-INV-108`   `CT-TRC-001`              `AT/TI`         TraceEvent chain +              Candidate mapped
                   consequential trace MUST                                                             integrity/correlation evidence  
                   support                                                                                                              

  `AOF-TRC-015`    High-assurance profile     `AOF-INV-084`   \`Verification path       ; no direct CT  sserted\``AT/TI\` Trace         Event chain + Explicit CT
                   MUST menentukan retention,                 defined                   a               integrity/correlation evidence  pending/inspection

  `AOF-TRC-016`    High-assurance audit gaps  \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/TI\`    TraceEvent chain + No direct
                   MUST explicit dan MUST NOT AOF-INV mapping                                           integrity/correlation evidence  invariant asserted; Explicit
                                              a                                                                                         CT pending/inspection

  `AOF-HG-001`     Deployment MUST identify   `AOF-INV-110`   \`Verification path       ; no direct CT  sserted\``DI/CI/TI/HR\` Gover   nance record + Duplicate-ID
                   governance root atau                       defined                   a               Approval/Override/Break-Glass   wording review; Explicit CT
                                                                                                        evidence + TraceEvent           pending/inspection

  `AOF-HG-002`     Agent MUST NOT             `AOF-INV-116`   \`Verification path       ; no direct CT  sserted\``DI/CI/TI/HR\` Gover   nance record + Explicit CT
                   unilaterally redefine                      defined                   a               Approval/Override/Break-Glass   pending/inspection
                   governing                                                                            evidence + TraceEvent           

  `AOF-HG-003`     Delegated operational      `AOF-INV-112`   `CT-HG-007`               `DI/CI/TI/HR`   Governance record +             Duplicate-ID wording review
                   Authority MUST be bounded                                                            Approval/Override/Break-Glass   
                   by                                                                                   evidence + TraceEvent           

  `AOF-HG-004`     Consequential delegation   `AOF-INV-112`   \`Verification path       ; no direct CT  sserted\``DI/CI/TI/HR\` Gover   nance record + Duplicate-ID
                   MUST preserve                              defined                   a               Approval/Override/Break-Glass   wording review; Explicit CT
                                                                                                        evidence + TraceEvent           pending/inspection

  `AOF-HG-005`     Human actor MUST NOT be    `AOF-INV-120`   \`Verification path       ; no direct CT  sserted\``DI/CI/TI/HR\` Gover   nance record + Explicit CT
                   treated as implicitly                      defined                   a               Approval/Override/Break-Glass   pending/inspection
                                                                                                        evidence + TraceEvent           

  `AOF-HG-006`     Approval MUST NOT          `AOF-INV-114`   \`Verification path       ; no direct CT  sserted\``DI/CI/TI/HR\` Gover   nance record + Duplicate-ID
                   implicitly expand                          defined                   a               Approval/Override/Break-Glass   wording review; Explicit CT
                   Authority beyond                                                                     evidence + TraceEvent           pending/inspection

  `AOF-HG-007`     Risk acceptance MUST NOT   `AOF-INV-119`   `CT-HG-008`               `DI/CI/TI/HR`   Governance record +             Duplicate-ID wording review
                   implicitly disable                                                                   Approval/Override/Break-Glass   
                   unrelated                                                                            evidence + TraceEvent           

  `AOF-HG-008`     Override MUST NOT bypass a `AOF-INV-116`   `CT-HG-005`               `DI/CI/TI/HR`   Governance record +             Duplicate-ID wording review
                   `NonOverridable` control.                                                            Approval/Override/Break-Glass   
                                                                                                        evidence + TraceEvent           

  `AOF-HG-009`     Break-Glass use MUST       `AOF-INV-117`   `CT-HG-006`               `DI/CI/TI/HR`   Governance record +             Duplicate-ID wording review
                   preserve auditable                                                                   Approval/Override/Break-Glass   
                   governance                                                                           evidence + TraceEvent           

  `AOF-HG-010`     Required Human             `AOF-INV-113`   `CT-HG-004`               `DI/CI/TI/HR`   Governance record +             Duplicate-ID wording review
                   unavailability MUST NOT                                                              Approval/Override/Break-Glass   
                   create                                                                               evidence + TraceEvent           

  `AOF-HG-011`     Consequential Human        `AOF-INV-121`   `CT-HG-004`               `DI/CI/TI/HR`   Governance record +             Candidate mapped
                   approval SHOULD bind                                                                 Approval/Override/Break-Glass   
                   identity,                                                                            evidence + TraceEvent           

  `AOF-HG-012`     Material change setelah    `AOF-INV-115`   `CT-HG-002`               `DI/CI/TI/HR`   Governance record +             Candidate mapped
                   approval SHOULD trigger                                                              Approval/Override/Break-Glass   
                                                                                                        evidence + TraceEvent           

  `AOF-HG-013`     Override Authority SHOULD  `AOF-INV-116`   \`Verification path       ; no direct CT  sserted\``DI/CI/TI/HR\` Gover   nance record + Explicit CT
                   be explicit dan distinct                   defined                   a               Approval/Override/Break-Glass   pending/inspection
                                                                                                        evidence + TraceEvent           

  `AOF-HG-014`     Break-Glass Authority      `AOF-INV-117`   `CT-HG-006`               `DI/CI/TI/HR`   Governance record +             Candidate mapped
                   SHOULD be narrow,                                                                    Approval/Override/Break-Glass   
                                                                                                        evidence + TraceEvent           

  `AOF-HG-015`     Human governance decisions `AOF-INV-121`   \`Verification path       ; no direct CT  sserted\``DI/CI/TI/HR\` Gover   nance record + Explicit CT
                   SHOULD update                              defined                   a               Approval/Override/Break-Glass   pending/inspection
                                                                                                        evidence + TraceEvent           

  `AOF-HG-016`     Consequential Human        `AOF-INV-116`   \`Verification path       ; no direct CT  sserted\``DI/CI/TI/HR\` Gover   nance record + Explicit CT
                   governance events SHOULD                   defined                   a               Approval/Override/Break-Glass   pending/inspection
                   be                                                                                   evidence + TraceEvent           

  `AOF-HG-017`     Governance conflict SHOULD `AOF-INV-110`   \`Verification path       ; no direct CT  sserted\``DI/CI/TI/HR\` Gover   nance record + Explicit CT
                   memiliki deterministic                     defined                   a               Approval/Override/Break-Glass   pending/inspection
                                                                                                        evidence + TraceEvent           

  `AOF-HG-018`     Risk-proportional          `AOF-INV-119`   \`Verification path       ; no direct CT  sserted\``DI/CI/TI/HR\` Gover   nance record + Explicit CT
                   governance SHOULD avoid                    defined                   a               Approval/Override/Break-Glass   pending/inspection
                   unnecessary                                                                          evidence + TraceEvent           

  `AOF-HG-019`     High-Assurance profile     `AOF-INV-116`   \`Verification path       ; no direct CT  sserted\``DI/CI/TI/HR\` Gover   nance record + Explicit CT
                   MUST define Human                          defined                   a               Approval/Override/Break-Glass   pending/inspection
                   Governance                                                                           evidence + TraceEvent           

  `AOF-HG-020`     High-Assurance             `AOF-INV-114`   \`Verification path       ; no direct CT  sserted\``DI/CI/TI/HR\` Gover   nance record + Explicit CT
                   approval/override MUST                     defined                   a               Approval/Override/Break-Glass   pending/inspection
                   satisfy                                                                              evidence + TraceEvent           

  `AOF-HG-021`     High-Assurance Break-Glass `AOF-INV-117`   `CT-HG-006`               `DI/CI/TI/HR`   Governance record +             Candidate mapped
                   MUST require post-event                                                              Approval/Override/Break-Glass   
                                                                                                        evidence + TraceEvent           

  `AOF-HG-022`     High-Assurance deployment  `AOF-INV-121`   \`Verification path       ; no direct CT  sserted\``DI/CI/TI/HR\` Gover   nance record + Explicit CT
                   MUST define continuity for                 defined                   a               Approval/Override/Break-Glass   pending/inspection
                                                                                                        evidence + TraceEvent           

  `AOF-HG-023`     High-Assurance override    \`No direct     sserted\``CT-HG-005\`     \`DI/C          I/TI/HR\` Governance record +   Invariant review
                   MUST record affected       AOF-INV mapping                                           Approval/Override/Break-Glass   
                   control,                   a                                                         evidence + TraceEvent           

  `AOF-HG-024`     High-Assurance governance  `AOF-INV-119`   \`Verification path       ; no direct CT  sserted\``DI/CI/TI/HR\` Gover   nance record + Explicit CT
                   changes MUST be versioned                  defined                   a               Approval/Override/Break-Glass   pending/inspection
                                                                                                        evidence + TraceEvent           

  `AOF-FR-001`     Material failure MUST      `AOF-INV-128`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Failu      re record + recovery
                   menjadi explicit governed                  defined                   a               decision + effect evidence +    Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-FR-002`     Consequential retry MUST   `AOF-INV-130`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Failu      re record + recovery Explicit
                   NOT blindly reuse stale                    defined                   a               decision + effect evidence +    CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-FR-003`     Material partial effect    `AOF-INV-100`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Failu      re record + recovery
                   MUST reconciled sebelum                    defined                   a               decision + effect evidence +    Duplicate-ID wording review;
                                                                                                        TraceEvent                      Explicit CT pending/inspection

  `AOF-FR-004`     Mandatory Safety Kernel    `AOF-INV-128`   `CT-FR-002`               `AT/NT/TI`      Failure record + recovery       Candidate mapped
                   failure MUST NOT silently                                                            decision + effect evidence +    
                                                                                                        TraceEvent                      

  `AOF-FR-005`     Unknown material effect    `AOF-INV-100`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Failu      re record + recovery Explicit
                   MUST NOT dianggap                          defined                   a               decision + effect evidence +    CT pending/inspection
                   no-effect.                                                                           TraceEvent                      

  `AOF-FR-006`     Recovery action MUST       `AOF-INV-126`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Failu      re record + recovery Explicit
                   memiliki valid                             defined                   a               decision + effect evidence +    CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-FR-007`     Recovery success MUST      `AOF-INV-126`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Failu      re record + recovery Explicit
                   berdasarkan                                defined                   a               decision + effect evidence +    CT pending/inspection
                   observed/verified                                                                    TraceEvent                      

  `AOF-FR-008`     Failure/recovery history   `AOF-INV-125`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Failu      re record + recovery Explicit
                   MUST traceable.                            defined                   a               decision + effect evidence +    CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-FR-009`     Retry MUST bounded oleh    `AOF-INV-127`   `CT-FR-002`               `AT/NT/TI`      Failure record + recovery       Candidate mapped
                   retry/failure budget.                                                                decision + effect evidence +    
                                                                                                        TraceEvent                      

  `AOF-FR-010`     Material replan MUST       `AOF-INV-084`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Failu      re record + recovery Explicit
                   reevaluate affected                        defined                   a               decision + effect evidence +    CT pending/inspection
                   governance                                                                           TraceEvent                      

  `AOF-FR-011`     Compensation/Rollback MUST `AOF-INV-129`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Failu      re record + recovery Explicit
                   diperlakukan sebagai                       defined                   a               decision + effect evidence +    CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-FR-012`     Escalation MUST preserve   `AOF-INV-129`   `CT-FR-002`               `AT/NT/TI`      Failure record + recovery       Candidate mapped
                   sufficient failure                                                                   decision + effect evidence +    
                                                                                                        TraceEvent                      

  `AOF-FR-013`     Abort/Cancel MUST          \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Failure record + recovery No
                   reconcile material         AOF-INV mapping                                           decision + effect evidence +    direct invariant asserted;
                   in-flight                  a                                                         TraceEvent                      Explicit CT pending/inspection

  `AOF-FR-014`     Agent replacement after    `AOF-INV-123`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Failu      re record + recovery Explicit
                   failure MUST NOT inherit                   defined                   a               decision + effect evidence +    CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-FR-015`     Material failure SHOULD    `AOF-INV-100`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Failu      re record + recovery Explicit
                   trigger Risk reassessment.                 defined                   a               decision + effect evidence +    CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-FR-016`     Required recovery          `AOF-INV-126`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Failu      re record + recovery Explicit
                   verification failure MUST                  defined                   a               decision + effect evidence +    CT pending/inspection
                   prevent                                                                              TraceEvent                      

  `AOF-FR-017`     High-risk recovery MUST    `AOF-INV-125`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Failu      re record + recovery Explicit
                   menggunakan explicit                       defined                   a               decision + effect evidence +    CT pending/inspection
                   Recovery                                                                             TraceEvent                      

  `AOF-FR-018`     High-assurance profile     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/NT/TI\` Failure record + recovery No
                   MUST menentukan retry,     AOF-INV mapping                                           decision + effect evidence +    direct invariant asserted;
                                              a                                                         TraceEvent                      Explicit CT pending/inspection

  `AOF-FR-019`     High-assurance recovery    `AOF-INV-126`   `CT-FR-001`               `AT/NT/TI`      Failure record + recovery       Candidate mapped
                   MUST preserve sufficient                                                             decision + effect evidence +    
                                                                                                        TraceEvent                      

  `AOF-FR-020`     High/Critical control      `AOF-INV-123`   \`Verification path       ; no direct CT  sserted\``AT/NT/TI\` Failu      re record + recovery Explicit
                   subsystem failure MUST                     defined                   a               decision + effect evidence +    CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-SEC-001`    Security-critical          \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``NT/CI/TI\` Security configuration + No
                   deployment MUST memiliki   AOF-INV mapping                                           negative-test result + security direct invariant asserted;
                   explicit                   a                                                         TraceEvent                      Explicit CT pending/inspection

  `AOF-SEC-002`    Context access MUST        `AOF-INV-135`   \`Verification path       ; no direct CT  sserted\``NT/CI/TI\` Secur      ity configuration + Explicit
                   mengikuti least-privilege                  defined                   a               negative-test result + security CT pending/inspection
                   dan                                                                                  TraceEvent                      

  `AOF-SEC-003`    Mandatory Safety Kernel    `AOF-INV-133`   \`Verification path       ; no direct CT  sserted\``NT/CI/TI\` Secur      ity configuration +
                   controls MUST                              defined                   a               negative-test result + security Duplicate-ID wording review;
                   non-bypassable                                                                       TraceEvent                      Explicit CT pending/inspection

  `AOF-SEC-004`    Consequential effect MUST  \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``NT/CI/TI\` Security configuration +
                   melewati applicable        AOF-INV mapping                                           negative-test result + security Duplicate-ID wording review;
                                              a                                                         TraceEvent                      Invariant review; Explicit CT
                                                                                                                                        pending/inspection

  `AOF-SEC-005`    Untrusted content MUST NOT `AOF-INV-131`   `CT-SEC-001`              `NT/CI/TI`      Security configuration +        Candidate mapped
                   directly grant Authority                                                             negative-test result + security 
                                                                                                        TraceEvent                      

  `AOF-SEC-006`    Credential possession MUST `AOF-INV-134`   \`Verification path       ; no direct CT  sserted\``NT/CI/TI\` Secur      ity configuration + Explicit
                   NOT menjadi sole proof of                  defined                   a               negative-test result + security CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-SEC-007`    Unknown mandatory security \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``NT/CI/TI\` Security configuration + No
                   condition MUST NOT         AOF-INV mapping                                           negative-test result + security direct invariant asserted;
                                              a                                                         TraceEvent                      Explicit CT pending/inspection

  `AOF-SEC-008`    Security-critical state    `AOF-INV-139`   \`Verification path       ; no direct CT  sserted\``NT/CI/TI\` Secur      ity configuration + Explicit
                   mutation MUST menggunakan                  defined                   a               negative-test result + security CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-SEC-009`    High-risk Effect Boundary  \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``NT/CI/TI\` Security configuration + No
                   SHOULD mitigate TOCTOU     AOF-INV mapping                                           negative-test result + security direct invariant asserted;
                                              a                                                         TraceEvent                      Explicit CT pending/inspection

  `AOF-SEC-010`    Replayable consequential   `AOF-INV-134`   \`Verification path       ; no direct CT  sserted\``NT/CI/TI\` Secur      ity configuration + Explicit
                   permit/action MUST                         defined                   a               negative-test result + security CT pending/inspection
                   memiliki                                                                             TraceEvent                      

  `AOF-SEC-011`    Sensitive                  `AOF-INV-137`   \`Verification path       ; no direct CT  sserted\``NT/CI/TI\` Secur      ity configuration + Explicit
                   Context/Evidence/Trace                     defined                   a               negative-test result + security CT pending/inspection
                   disclosure MUST                                                                      TraceEvent                      

  `AOF-SEC-012`    Security-critical          `AOF-INV-134`   \`Verification path       ; no direct CT  sserted\``NT/CI/TI\` Secur      ity configuration + Explicit
                   Policy/Authority                           defined                   a               negative-test result + security CT pending/inspection
                   configuration                                                                        TraceEvent                      

  `AOF-SEC-013`    Tool/parameter use MUST    \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``NT/CI/TI\` Security configuration + No
                   bounded oleh applicable    AOF-INV mapping                                           negative-test result + security direct invariant asserted;
                                              a                                                         TraceEvent                      Explicit CT pending/inspection

  `AOF-SEC-014`    Mandatory control          `AOF-INV-138`   \`Verification path       ; no direct CT  sserted\``NT/CI/TI\` Secur      ity configuration + Explicit
                   subsystem failure MUST                     defined                   a               negative-test result + security CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-SEC-015`    Security incident MUST     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``NT/CI/TI\` Security configuration + No
                   preserve sufficient        AOF-INV mapping                                           negative-test result + security direct invariant asserted;
                                              a                                                         TraceEvent                      Explicit CT pending/inspection

  `AOF-SEC-016`    Human approval for         `AOF-INV-131`   \`Verification path       ; no direct CT  sserted\``NT/CI/TI\` Secur      ity configuration + Explicit
                   consequential action                       defined                   a               negative-test result + security CT pending/inspection
                   SHOULD bind                                                                          TraceEvent                      

  `AOF-SEC-017`    High-assurance profile     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``NT/CI/TI\` Security configuration + No
                   MUST map material threats  AOF-INV mapping                                           negative-test result + security direct invariant asserted;
                   ke                         a                                                         TraceEvent                      Explicit CT pending/inspection

  `AOF-SEC-018`    High-assurance             `AOF-INV-137`   \`Verification path       ; no direct CT  sserted\``NT/CI/TI\` Secur      ity configuration + Explicit
                   trace/evidence/control                     defined                   a               negative-test result + security CT pending/inspection
                   configuration                                                                        TraceEvent                      

  `AOF-SEC-019`    High-assurance execution   \`No direct     sserted\``CT-SEC-002\`    \`NT/C          I/TI\` Security configuratio    n + Invariant review
                   MUST protect against       AOF-INV mapping                                           negative-test result + security 
                                              a                                                         TraceEvent                      

  `AOF-SEC-020`    High-assurance secrets     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``NT/CI/TI\` Security configuration + No
                   SHOULD menggunakan         AOF-INV mapping                                           negative-test result + security direct invariant asserted;
                                              a                                                         TraceEvent                      Explicit CT pending/inspection

  `AOF-SEC-021`    High-assurance             \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``NT/CI/TI\` Security configuration + No
                   verifier/control-plane     AOF-INV mapping                                           negative-test result + security direct invariant asserted;
                   independence               a                                                         TraceEvent                      Explicit CT pending/inspection

  `AOF-SEC-022`    High-assurance deployment  `AOF-INV-138`   \`Verification path       ; no direct CT  sserted\``NT/CI/TI\` Secur      ity configuration + Explicit
                   MUST define security                       defined                   a               negative-test result + security CT pending/inspection
                                                                                                        TraceEvent                      

  `AOF-CONF-001`   Conformance claim MUST     `AOF-INV-149`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   identify subject, version,                 defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-002`   Conformance-critical       `AOF-INV-148`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   mandatory requirement MUST                 defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-003`   Failed applicable          `AOF-INV-148`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   mandatory requirement MUST                 defined                   a               test/inspection evidence        Duplicate-ID wording review;
                                                                                                                                        Explicit CT pending/inspection

  `AOF-CONF-004`   `Blocked`/`Inconclusive`   `AOF-INV-147`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   test MUST NOT dihitung                     defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-005`   `NotApplicable` mandatory  `AOF-INV-140`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   requirement MUST memiliki                  defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-006`   Conformance evidence MUST  `AOF-INV-149`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   bind ke relevant                           defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-007`   Full profile conformance   `AOF-INV-146`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   MUST assess all applicable                 defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-008`   Conformance report MUST    `AOF-INV-149`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   state assessment mode dan                  defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-009`   Profile dependencies MUST  `AOF-INV-146`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   resolved sebelum                           defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-010`   Material configuration     `AOF-INV-149`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   change SHOULD trigger                      defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-011`   Negative governance tests  \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI/AT/TI\` ConformanceManifest/Report +
                   SHOULD menjadi bagian      AOF-INV mapping                                           test/inspection evidence        No direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-CONF-012`   Failure/recovery behavior  \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI/AT/TI\` ConformanceManifest/Report +
                   SHOULD diuji melalui       AOF-INV mapping                                           test/inspection evidence        No direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-CONF-013`   Conformance suite SHOULD   `AOF-INV-149`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   test observable governed                   defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-014`   Exception MUST explicit    \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI/AT/TI\` ConformanceManifest/Report +
                   dan MUST NOT silently      AOF-INV mapping                                           test/inspection evidence        No direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-CONF-015`   Domain-scoped conformance  `AOF-INV-149`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   claim MUST clearly                         defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-016`   Test/evidence package      \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI/AT/TI\` ConformanceManifest/Report +
                   SHOULD cukup untuk         AOF-INV mapping                                           test/inspection evidence        No direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-CONF-017`   High-assurance profile     `AOF-INV-146`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   MUST map material security                 defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-018`   High-assurance conformance `AOF-INV-149`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   MUST test state                            defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-019`   High-assurance conformance `AOF-INV-149`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   MUST test verification                     defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-020`   High-assurance conformance `AOF-INV-149`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   MUST preserve                              defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-CONF-021`   High-assurance assessment  \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI/AT/TI\` ConformanceManifest/Report +
                   SHOULD menggunakan         AOF-INV mapping                                           test/inspection evidence        No direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-CONF-022`   High-assurance profile     `AOF-INV-146`   \`Verification path       ; no direct CT  sserted\``DI/AT/TI\` Confo      rmanceManifest/Report +
                   MUST define                                defined                   a               test/inspection evidence        Explicit CT pending/inspection

  `AOF-REF-001`    Established external       \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI\`       Reference inventory + No
                   techniques MUST NOT        AOF-INV mapping                                           citation/source review record   direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-REF-002`    External reference adopted \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI\`       Reference inventory + No
                   untuk normative            AOF-INV mapping                                           citation/source review record   direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-REF-003`    AOF conformance MUST NOT   \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI\`       Reference inventory + No
                   diklaim equivalent dengan  AOF-INV mapping                                           citation/source review record   direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-REF-004`    Prior-art differentiation  \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI\`       Reference inventory + No
                   claims MUST scoped dan     AOF-INV mapping                                           citation/source review record   direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-REF-005`    Living framework crosswalk \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI\`       Reference inventory + No
                   SHOULD identify reviewed   AOF-INV mapping                                           citation/source review record   direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-REF-006`    Research Candidate         \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI\`       Reference inventory + No
                   terminology MUST NOT       AOF-INV mapping                                           citation/source review record   direct invariant asserted;
                   menjadi                    a                                                                                         Explicit CT pending/inspection

  `AOF-REF-007`    External standard update   \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI\`       Reference inventory + No
                   MUST NOT silently alter    AOF-INV mapping                                           citation/source review record   direct invariant asserted;
                   AOF                        a                                                                                         Explicit CT pending/inspection

  `AOF-REF-008`    Final public release       \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI\`       Reference inventory + No
                   SHOULD publish             AOF-INV mapping                                           citation/source review record   direct invariant asserted;
                   authoritative              a                                                                                         Explicit CT pending/inspection

  `AOF-REG-001`    Every domain invariant     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI/TI\`    Registry record + No direct
                   MUST have a stable         AOF-INV mapping                                           alias/migration review evidence invariant asserted; Explicit
                   canonical                  a                                                                                         CT pending/inspection

  `AOF-REG-002`    Domain invariant aliases   \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI/TI\`    Registry record + No direct
                   MUST NOT be destructively  AOF-INV mapping                                           alias/migration review evidence invariant asserted; Explicit
                                              a                                                                                         CT pending/inspection

  `AOF-REG-003`    Semantic merge MUST        \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI/TI\`    Registry record + No direct
                   require explicit           AOF-INV mapping                                           alias/migration review evidence invariant asserted; Explicit
                   equivalence                a                                                                                         CT pending/inspection

  `AOF-REG-004`    Every applicable canonical \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI/TI\`    Registry record + No direct
                   invariant MUST map to at   AOF-INV mapping                                           alias/migration review evidence invariant asserted; Explicit
                                              a                                                                                         CT pending/inspection

  `AOF-REG-005`    Every applicable           \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI/TI\`    Registry record + No direct
                   behavioral invariant MUST  AOF-INV mapping                                           alias/migration review evidence invariant asserted; Explicit
                   map to at                  a                                                                                         CT pending/inspection

  `AOF-REG-006`    Unresolved mapping MUST    \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI/TI\`    Registry record + No direct
                   remain explicit and MUST   AOF-INV mapping                                           alias/migration review evidence invariant asserted; Explicit
                   NOT                        a                                                                                         CT pending/inspection

  `AOF-REG-007`    Registry changes after     \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``DI/TI\`    Registry record + No direct
                   Semantic Freeze MUST       AOF-INV mapping                                           alias/migration review evidence invariant asserted; Explicit
                   follow                     a                                                                                         CT pending/inspection

  `AOF-SCH-001`    Schemas MUST preserve      `AOF-INV-156`   \`Verification path       ; no direct CT  sserted\``AT/CI\` Schem         a validation result +
                   canonical construct                        defined                   a               canonical object instance       Duplicate-ID wording review;
                                                                                                                                        Explicit CT pending/inspection

  `AOF-SCH-002`    Governance-critical        `AOF-INV-154`   \`Verification path       ; no direct CT  sserted\``AT/CI\` Schem         a validation result +
                   references MUST resolve                    defined                   a               canonical object instance       Duplicate-ID wording review;
                                                                                                                                        Explicit CT pending/inspection

  `AOF-SCH-003`    Task schema MUST preserve  `AOF-INV-154`   \`Verification path       ; no direct CT  sserted\``AT/CI\` Schem         a validation result +
                   inherited mandatory                        defined                   a               canonical object instance       Duplicate-ID wording review;
                                                                                                                                        Explicit CT pending/inspection

  `AOF-SCH-004`    Authority schema MUST      \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/CI\`    Schema validation result + No
                   represent scope, validity, AOF-INV mapping                                           canonical object instance       direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-SCH-005`    Consequential Decision     `AOF-INV-157`   \`Verification path       ; no direct CT  sserted\``AT/CI\` Schem         a validation result +
                   schema MUST reference                      defined                   a               canonical object instance       Duplicate-ID wording review;
                                                                                                                                        Explicit CT pending/inspection

  `AOF-SCH-006`    Derived Evidence schema    \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/CI\`    Schema validation result +
                   MUST support               AOF-INV mapping                                           canonical object instance       Duplicate-ID wording review;
                                              a                                                                                         Invariant review; Explicit CT
                                                                                                                                        pending/inspection

  `AOF-SCH-007`    State Transition schema    `AOF-INV-152`   \`Verification path       ; no direct CT  sserted\``AT/CI\` Schem         a validation result +
                   MUST identify before/after                 defined                   a               canonical object instance       Duplicate-ID wording review;
                                                                                                                                        Explicit CT pending/inspection

  `AOF-SCH-008`    Unknown/missing mandatory  \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/CI\`    Schema validation result + No
                   governance value MUST NOT  AOF-INV mapping                                           canonical object instance       direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-SCH-009`    Schema validation MUST NOT `AOF-INV-156`   \`Verification path       ; no direct CT  sserted\``AT/CI\` Schem         a validation result + Explicit
                   be treated as execution                    defined                   a               canonical object instance       CT pending/inspection

  `AOF-SCH-010`    Canonical enum identifiers \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/CI\`    Schema validation result + No
                   MUST have stable           AOF-INV mapping                                           canonical object instance       direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-SCH-011`    Schema package MUST be     `AOF-INV-150`   \`Verification path       ; no direct CT  sserted\``AT/CI\` Schem         a validation result + Explicit
                   versioned.                                 defined                   a               canonical object instance       CT pending/inspection

  `AOF-SCH-012`    Cross-object references    `AOF-INV-154`   \`Verification path       ; no direct CT  sserted\``AT/CI\` Schem         a validation result + Explicit
                   SHOULD be type/scope                       defined                   a               canonical object instance       CT pending/inspection

  `AOF-SCH-013`    Extensions MUST NOT        `AOF-INV-155`   \`Verification path       ; no direct CT  sserted\``AT/CI\` Schem         a validation result + Explicit
                   redefine canonical                         defined                   a               canonical object instance       CT pending/inspection
                   semantics.                                                                                                           

  `AOF-SCH-014`    Governance-critical schema `AOF-INV-150`   \`Verification path       ; no direct CT  sserted\``AT/CI\` Schem         a validation result + Explicit
                   validation failures                        defined                   a               canonical object instance       CT pending/inspection

  `AOF-SCH-015`    Schema evolution SHOULD    `AOF-INV-156`   \`Verification path       ; no direct CT  sserted\``AT/CI\` Schem         a validation result + Explicit
                   preserve backward                          defined                   a               canonical object instance       CT pending/inspection

  `AOF-SCH-016`    Migration MUST preserve    `AOF-INV-156`   \`Verification path       ; no direct CT  sserted\``AT/CI\` Schem         a validation result + Explicit
                   governance semantics atau                  defined                   a               canonical object instance       CT pending/inspection

  `AOF-SCH-017`    Sensitive payload SHOULD   \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/CI\`    Schema validation result + No
                   support                    AOF-INV mapping                                           canonical object instance       direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-SCH-018`    Conformance                `AOF-INV-152`   \`Verification path       ; no direct CT  sserted\``AT/CI\` Schem         a validation result + Explicit
                   Manifest/Report MUST be                    defined                   a               canonical object instance       CT pending/inspection

  `AOF-SCH-019`    High-assurance schema      \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/CI\`    Schema validation result + No
                   package SHOULD have        AOF-INV mapping                                           canonical object instance       direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-SCH-020`    High-assurance validators  \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/CI\`    Schema validation result + No
                   MUST have deterministic    AOF-INV mapping                                           canonical object instance       direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection

  `AOF-SCH-021`    High-assurance validation  `AOF-INV-156`   \`Verification path       ; no direct CT  sserted\``AT/CI\` Schem         a validation result + Explicit
                   MUST detect                                defined                   a               canonical object instance       CT pending/inspection

  `AOF-SCH-022`    High-assurance schema      \`No direct     sserted\`\`Verification p ath defined; no direct CT asserted\``AT/CI\`    Schema validation result + No
                   tests MUST include         AOF-INV mapping                                           canonical object instance       direct invariant asserted;
                                              a                                                                                         Explicit CT pending/inspection
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------

| `AOF-PRF-001` \| A stronger/base-derived profile MUST preserve
  mandatory requirements of its applicable base profile. \|
  `AOF-INV-159` \| `CT-PRF-001` \| `AT/NT/DI` \| ConformanceManifest +
  profile configuration + conformance result \| Reconciled \|
| `AOF-PRF-002` \| Profile composition MUST NOT weaken mandatory AOF
  invariants. \| `AOF-INV-160` \| `CT-PRF-003` \| `AT/NT/DI` \|
  ConformanceManifest + profile configuration + conformance result \|
  Reconciled \|
| `AOF-PRF-003` \| Claimed profiles MUST be explicit in the
  ConformanceManifest or equivalent conformance artifact. \|
  `AOF-INV-161` \| `CT-PRF-004` \| `AT/NT/DI` \| ConformanceManifest +
  profile configuration + conformance result \| Reconciled \|
| `AOF-PRF-004` \| AOF-Secure-SDLC MUST be treated as a domain profile
  rather than an assumed universal linear maturity level. \|
  `AOF-INV-162` \| `CT-PRF-002` \| `AT/NT/DI` \| ConformanceManifest +
  profile configuration + conformance result \| Reconciled \|
| `AOF-PRF-005` \| AOF-High-Assurance MUST strengthen, not replace,
  applicable base/domain controls. \| `AOF-INV-160` \| `CT-PRF-003` \|
  `AT/NT/DI` \| ConformanceManifest + profile configuration +
  conformance result \| Reconciled \|
| `AOF-PRF-006` \| Requirement applicability MUST NOT be changed solely
  to obtain a more favorable conformance result. \| `AOF-INV-160` \|
  `CT-PRF-001` \| `AT/NT/DI` \| ConformanceManifest + profile
  configuration + conformance result \| Reconciled \|

------------------------------------------------------------------------

## F.6 Duplicate Requirement Identifier Audit

Requirement ID yang muncul lebih dari sekali tidak otomatis dianggap
defect karena beberapa enriched sections mempertahankan compact
requirement summary dan expanded normative statement. Namun wording yang
berbeda MUST direview untuk memastikan tidak terjadi semantic
divergence.

  Requirement        Definitions   Similarity Review Status
  ---------------- ------------- ------------ ----------------------------------
  `AOF-AUTH-001`               2         0.92 Likely editorial duplicate
  `AOF-AUTH-002`               2         0.32 Semantic reconciliation required
  `AOF-AUTH-003`               2         0.85 Likely editorial duplicate
  `AOF-AUTH-004`               2         0.36 Semantic reconciliation required
  `AOF-AUTH-005`               2         0.57 Semantic reconciliation required
  `AOF-AUTH-006`               2         0.59 Semantic reconciliation required
  `AOF-AUTH-008`               2         0.92 Likely editorial duplicate
  `AOF-AUTH-009`               2         0.46 Semantic reconciliation required
  `AOF-AUTH-010`               2         0.69 Semantic reconciliation required
  `AOF-AUTH-011`               2         0.52 Semantic reconciliation required
  `AOF-AUTH-012`               2         0.76 Likely editorial duplicate
  `AOF-AUTH-013`               2         0.61 Semantic reconciliation required
  `AOF-AUTH-014`               2         0.61 Semantic reconciliation required
  `AOF-AUTH-015`               2         0.68 Semantic reconciliation required
  `AOF-POL-001`                2         0.92 Likely editorial duplicate
  `AOF-POL-002`                2         0.53 Semantic reconciliation required
  `AOF-POL-003`                2         0.39 Semantic reconciliation required
  `AOF-POL-004`                2         0.84 Likely editorial duplicate
  `AOF-POL-005`                2         0.44 Semantic reconciliation required
  `AOF-POL-006`                2         0.67 Semantic reconciliation required
  `AOF-POL-007`                2         0.37 Semantic reconciliation required
  `AOF-POL-008`                2         0.69 Semantic reconciliation required
  `AOF-POL-009`                2         0.79 Likely editorial duplicate
  `AOF-RISK-001`               2         0.95 Likely editorial duplicate
  `AOF-RISK-002`               2         0.62 Semantic reconciliation required
  `AOF-RISK-004`               2         0.53 Semantic reconciliation required
  `AOF-EVD-001`                2         0.28 Semantic reconciliation required
  `AOF-EVD-002`                2         0.71 Semantic reconciliation required
  `AOF-EVD-003`                2         0.65 Semantic reconciliation required
  `AOF-EVD-004`                2         0.25 Semantic reconciliation required
  `AOF-EVD-005`                2         0.65 Semantic reconciliation required
  `AOF-VER-003`                2         0.46 Semantic reconciliation required
  `AOF-VER-004`                2         0.91 Likely editorial duplicate
  `AOF-VER-005`                2         0.78 Likely editorial duplicate
  `AOF-VER-006`                2         0.89 Likely editorial duplicate
  `AOF-ST-001`                 2         0.74 Likely editorial duplicate
  `AOF-ST-002`                 2         0.76 Likely editorial duplicate
  `AOF-ST-003`                 2         0.41 Semantic reconciliation required
  `AOF-ST-004`                 2         0.90 Likely editorial duplicate
  `AOF-HG-001`                 2         0.65 Semantic reconciliation required
  `AOF-HG-003`                 2         0.47 Semantic reconciliation required
  `AOF-HG-004`                 2         0.54 Semantic reconciliation required
  `AOF-HG-006`                 2         0.86 Likely editorial duplicate
  `AOF-HG-007`                 2         0.82 Likely editorial duplicate
  `AOF-HG-008`                 2         0.86 Likely editorial duplicate
  `AOF-HG-009`                 2         0.78 Likely editorial duplicate
  `AOF-HG-010`                 2         0.90 Likely editorial duplicate
  `AOF-FR-001`                 2         0.55 Semantic reconciliation required
  `AOF-FR-003`                 2         0.78 Likely editorial duplicate
  `AOF-SEC-003`                2         0.87 Likely editorial duplicate
  `AOF-SEC-004`                2         0.71 Semantic reconciliation required
  `AOF-CONF-003`               2         0.64 Semantic reconciliation required
  `AOF-SCH-001`                2         0.40 Semantic reconciliation required
  `AOF-SCH-002`                2         0.99 Likely editorial duplicate
  `AOF-SCH-003`                2         0.66 Semantic reconciliation required
  `AOF-SCH-005`                2         0.69 Semantic reconciliation required
  `AOF-SCH-006`                2         0.70 Semantic reconciliation required
  `AOF-SCH-007`                2         0.73 Likely editorial duplicate

------------------------------------------------------------------------

## F.7 Orphan and Gap Classes

Traceability audit menggunakan gap classes berikut:

-   `T-GAP-01` --- Requirement tanpa verification method.
-   `T-GAP-02` --- Behavioral mandatory Requirement tanpa explicit CT
    dan tanpa justified inspection path.
-   `T-GAP-03` --- Requirement tanpa canonical invariant mapping ketika
    invariant relationship seharusnya ada.
-   `T-GAP-04` --- Test tanpa identifiable Requirement target.
-   `T-GAP-05` --- Duplicate Requirement ID dengan semantic divergence.
-   `T-GAP-06` --- Evidence class tidak cukup untuk membuktikan
    evaluated claim.
-   `T-GAP-07` --- Profile applicability unresolved.

Current matrix menghilangkan `T-GAP-01` untuk explicit canonical
Requirement IDs dengan menetapkan verification-method class. `T-GAP-02`
sampai `T-GAP-07` tetap menjadi input Final Consistency Review.

------------------------------------------------------------------------

## F.8 Negative Test Priority

Negative/adversarial tests SHOULD diprioritaskan untuk:

-   missing/expired/revoked Authority;
-   Policy Deny/Pending/conflict;
-   stale State/TOCTOU;
-   partial/unknown effect;
-   verifier independence failure;
-   untrusted Context/prompt injection;
-   Authority laundering/delegation escalation;
-   Human approval timeout/unavailability;
-   Safety Kernel component failure;
-   malformed/unknown schema payload;
-   unauthorized disclosure;
-   compromised Agent/tool path.

Canonical objective:

\[
ForbiddenEffect\Rightarrow Prevented\lor Contained\lor Detected
\]

dan bukan hanya pembuktian happy path.

------------------------------------------------------------------------

## F.9 Profile Applicability Boundary

Profile applicability belum diisi secara heuristik pada matrix ini. Bab
21 MUST diaudit sebagai separate final-review activity agar inheritance
dan applicability tidak diasumsikan dari domain name.

Target relationship:

\[ AOF\text{-}Core\subset eq
AOF\text{-}Governed\subset eq AOF\text{-}Assured
\]

dengan `AOF-Secure-SDLC` dan `AOF-High-Assurance` mengikuti semantics
yang benar-benar didefinisikan oleh Section 21, bukan dipaksakan oleh
Appendix F.

------------------------------------------------------------------------

## F.10 Traceability Requirements

**AOF-TRM-001** --- Every explicit canonical Requirement ID MUST have at
least one verification method before Semantic Freeze.

**AOF-TRM-002** --- Every applicable behavioral mandatory Requirement
SHOULD have an explicit executable Conformance Test unless inspection is
the justified verification method.

**AOF-TRM-003** --- Negative/adversarial testing SHOULD be used for
mandatory prevention and fail-controlled properties where feasible.

**AOF-TRM-004** --- Duplicate Requirement IDs MUST be semantically
reconciled before Semantic Freeze.

**AOF-TRM-005** --- Unresolved invariant/test/profile mappings MUST
remain explicit and MUST NOT be represented as conformant coverage.

**AOF-TRM-006** --- Required Evidence MUST be sufficient to support the
evaluated Requirement and bind to the relevant
implementation/version/profile where applicable.

**AOF-TRM-007** --- Orphan tests and orphan mandatory Requirements MUST
be resolved or explicitly justified before RC-Final.

------------------------------------------------------------------------

## F.11 Freeze Gate

Appendix F MAY become `Freeze Candidate` when:

1.  all unique canonical Requirement IDs have verification methods;
2.  duplicate-ID wording has been semantically reconciled;
3.  behavioral mandatory Requirements have explicit tests or justified
    inspection paths;
4.  invariant mappings are semantically reviewed;
5.  orphan tests are mapped or retired;
6.  Evidence classes are validated;
7.  Section 21 profile applicability audit is complete;
8.  no unresolved traceability gap is represented as covered.

Current pass establishes the cumulative traceability baseline. Final
semantic resolution of flagged mappings belongs to
`Final Consistency Review` and MUST occur before `RC-Final`.

------------------------------------------------------------------------

## F.12 Previously Unmapped Test Classification

Tests yang tidak memperoleh candidate mapping pada initial lexical pass
diklasifikasikan secara explicit di sini. `Supplemental` berarti test
tetap berguna sebagai assurance test tetapi tidak boleh dihitung sebagai
direct Requirement coverage sampai explicit mapping disetujui.

  -----------------------------------------------------------------------
  Test              Name              Classification    Freeze Treatment
  ----------------- ----------------- ----------------- -----------------
  `CT-LC-002`       Stale Decision    Supplemental /    Retain; MUST NOT
                                      semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage

  `CT-LC-005`       Revoked Authority Supplemental /    Retain; MUST NOT
                                      semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage

  `CT-LC-006`       Replan            Supplemental /    Retain; MUST NOT
                                      semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage

  `CT-LC-007`       Cancellation      Supplemental /    Retain; MUST NOT
                                      semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage

  `CT-LC-010`       Human Approval    Supplemental /    Retain; MUST NOT
                    Timeout           semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage

  `CT-AGT-002`      High Capability,  Supplemental /    Retain; MUST NOT
                    Risk Incompatible semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage

  `CT-AGT-006`      Self Verification Supplemental /    Retain; MUST NOT
                                      semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage

  `CT-AGT-010`      Cheapest          Supplemental /    Retain; MUST NOT
                    Ineligible Agent  semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage

  `CT-AGT-012`      Disclosure        Supplemental /    Retain; MUST NOT
                    Boundary          semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage

  `CT-HG-001`       Human Without     Supplemental /    Retain; MUST NOT
                    Authority         semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage

  `CT-HG-003`       Approval Scope    Supplemental /    Retain; MUST NOT
                                      semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage

  `CT-AUTH-002`     Revoked Authority Supplemental /    Retain; MUST NOT
                                      semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage

  `CT-POL-001`      Explicit Deny     Supplemental /    Retain; MUST NOT
                                      semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage

  `CT-STATE-001`    Stale State       Supplemental /    Retain; MUST NOT
                                      semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage

  `CT-SEC-003`      Replay            Supplemental /    Retain; MUST NOT
                                      semantic mapping  count as direct
                                      not established   Requirement
                                                        coverage
  -----------------------------------------------------------------------

Dengan klasifikasi ini, tidak ada `CT-*` yang silently orphaned: setiap
test adalah either Requirement-mapped atau explicitly retained as
supplemental.

------------------------------------------------------------------------

# Appendix G --- Final Consistency Review

> **Historical Audit Record --- Non-Authoritative Current-State
> Status.** Appendix ini mempertahankan evidence dari pass sebelumnya.
> Status, blocker count, atau workflow-state wording di sini MUST NOT
> mengoverride normative core, Appendix A--F, atau latest release
> decision.

## G.1 Review Scope

Review ini menggunakan `RC-Traceability` sebagai cumulative baseline dan
mengaudit:

-   identifier uniqueness and stability;
-   duplicate Requirement wording;
-   Master Invariant Registry migration gaps;
-   Requirement/Test traceability;
-   orphan Conformance Tests;
-   Section 21 profile semantics;
-   cross-domain terminology and freeze readiness.

Review bersifat corrective reconciliation. Tidak ada domain/paradigm
baru yang diperkenalkan.

------------------------------------------------------------------------

## G.2 Review Findings Summary

-   Unique explicit Requirement IDs reviewed: **326**.
-   Duplicate Requirement IDs requiring wording review: **58**.
-   Existing Conformance Tests reviewed: **47**.
-   Tests not referenced by Appendix F candidate mappings: **15**.
-   Canonical Master Registry invariants: **158**.
-   Legacy Appendix A mappings still unresolved: **0**.
-   Appendix F Requirement rows pending invariant review: **0**.
-   Appendix F Requirement rows without explicit CT mapping: **0**.

Kesimpulan: normative domains tetap `Freeze Candidate`, tetapi
specification **belum layak dinyatakan `Semantic Freeze`** karena
traceability reconciliation masih memiliki explicit open items.

------------------------------------------------------------------------

## G.3 Section 21 Profile Reconciliation

Section 21 telah dikoreksi untuk menghindari asumsi bahwa seluruh
profiles membentuk satu linear maturity chain.

Canonical base relationship:

\[ AOF\text{-}Core\subset eq
AOF\text{-}Governed\subset eq AOF\text{-}Assured
\]

`AOF-Secure-SDLC` sekarang explicit sebagai domain profile, sedangkan
`AOF-High-Assurance` sebagai strengthening profile. Composition MUST
preserve applicable base requirements.

Ditambahkan:

-   `AOF-PRF-001`--`AOF-PRF-006`;
-   `PRF-INV-01`--`PRF-INV-04`;
-   `CT-PRF-001`--`CT-PRF-004`.

Perubahan ini adalah reconciliation terhadap semantics profile yang
sebelumnya underspecified, bukan domain baru.

------------------------------------------------------------------------

## G.4 Duplicate Requirement ID Review

Duplicate identifier tidak otomatis berarti semantic conflict. Namun
identifier dengan multiple wording MUST memiliki satu canonical
normative meaning sebelum freeze.

  ----------------------------------------------------------------------
  Requirement      Distinct              Minimum Lexical Review Class
                   Definitions                Similarity 
  ---------------- ------------------ ------------------ ---------------
  `AOF-AUTH-001`   2                                1.00 Editorial
                                                         consolidation
                                                         candidate

  `AOF-AUTH-002`   2                                0.32 Semantic review
                                                         required

  `AOF-AUTH-003`   2                                0.85 Editorial
                                                         consolidation
                                                         candidate

  `AOF-AUTH-004`   2                                0.45 Semantic review
                                                         required

  `AOF-AUTH-005`   2                                0.53 Semantic review
                                                         required

  `AOF-AUTH-006`   2                                0.59 Semantic review
                                                         required

  `AOF-AUTH-008`   2                                0.92 Editorial
                                                         consolidation
                                                         candidate

  `AOF-AUTH-009`   2                                0.46 Semantic review
                                                         required

  `AOF-AUTH-010`   2                                0.69 Semantic review
                                                         required

  `AOF-AUTH-011`   2                                0.52 Semantic review
                                                         required

  `AOF-AUTH-012`   2                                0.76 Editorial
                                                         consolidation
                                                         candidate

  `AOF-AUTH-013`   2                                0.61 Semantic review
                                                         required

  `AOF-AUTH-014`   2                                0.61 Semantic review
                                                         required

  `AOF-AUTH-015`   2                                0.68 Semantic review
                                                         required

  `AOF-POL-001`    2                                1.00 Editorial
                                                         consolidation
                                                         candidate

  `AOF-POL-002`    2                                0.53 Semantic review
                                                         required

  `AOF-POL-003`    2                                0.39 Semantic review
                                                         required

  `AOF-POL-004`    2                                0.84 Editorial
                                                         consolidation
                                                         candidate

  `AOF-POL-005`    2                                0.44 Semantic review
                                                         required

  `AOF-POL-006`    2                                0.67 Semantic review
                                                         required

  `AOF-POL-007`    2                                0.37 Semantic review
                                                         required

  `AOF-POL-008`    2                                0.69 Semantic review
                                                         required

  `AOF-POL-009`    2                                0.79 Editorial
                                                         consolidation
                                                         candidate

  `AOF-RISK-001`   2                                0.95 Editorial
                                                         consolidation
                                                         candidate

  `AOF-RISK-002`   2                                0.62 Semantic review
                                                         required

  `AOF-RISK-004`   2                                0.53 Semantic review
                                                         required

  `AOF-EVD-001`    2                                0.28 Semantic review
                                                         required

  `AOF-EVD-002`    2                                0.71 Semantic review
                                                         required

  `AOF-EVD-003`    2                                0.65 Semantic review
                                                         required

  `AOF-EVD-004`    2                                0.25 Semantic review
                                                         required

  `AOF-EVD-005`    2                                0.65 Semantic review
                                                         required

  `AOF-VER-003`    2                                0.46 Semantic review
                                                         required

  `AOF-VER-004`    2                                0.91 Editorial
                                                         consolidation
                                                         candidate

  `AOF-VER-005`    2                                0.78 Editorial
                                                         consolidation
                                                         candidate

  `AOF-VER-006`    2                                0.89 Editorial
                                                         consolidation
                                                         candidate

  `AOF-ST-001`     2                                0.74 Editorial
                                                         consolidation
                                                         candidate

  `AOF-ST-002`     2                                0.76 Editorial
                                                         consolidation
                                                         candidate

  `AOF-ST-003`     2                                0.41 Semantic review
                                                         required

  `AOF-ST-004`     2                                0.90 Editorial
                                                         consolidation
                                                         candidate

  `AOF-HG-001`     2                                0.65 Semantic review
                                                         required

  `AOF-HG-003`     2                                0.47 Semantic review
                                                         required

  `AOF-HG-004`     2                                0.54 Semantic review
                                                         required

  `AOF-HG-006`     2                                0.86 Editorial
                                                         consolidation
                                                         candidate

  `AOF-HG-007`     2                                0.82 Editorial
                                                         consolidation
                                                         candidate

  `AOF-HG-008`     2                                0.72 Editorial
                                                         consolidation
                                                         candidate

  `AOF-HG-009`     2                                0.78 Editorial
                                                         consolidation
                                                         candidate

  `AOF-HG-010`     2                                0.90 Editorial
                                                         consolidation
                                                         candidate

  `AOF-FR-001`     2                                0.55 Semantic review
                                                         required

  `AOF-FR-003`     2                                0.78 Editorial
                                                         consolidation
                                                         candidate

  `AOF-SEC-003`    2                                0.87 Editorial
                                                         consolidation
                                                         candidate

  `AOF-SEC-004`    2                                0.71 Semantic review
                                                         required

  `AOF-CONF-003`   2                                0.68 Semantic review
                                                         required

  `AOF-SCH-001`    2                                0.40 Semantic review
                                                         required

  `AOF-SCH-002`    2                                0.99 Editorial
                                                         consolidation
                                                         candidate

  `AOF-SCH-003`    2                                0.66 Semantic review
                                                         required

  `AOF-SCH-005`    2                                0.69 Semantic review
                                                         required

  `AOF-SCH-006`    2                                0.70 Semantic review
                                                         required

  `AOF-SCH-007`    2                                0.73 Editorial
                                                         consolidation
                                                         candidate
  ----------------------------------------------------------------------

------------------------------------------------------------------------

## G.5 Legacy Invariant Migration Gaps

Tidak ada unresolved legacy invariant mapping.

------------------------------------------------------------------------

## G.6 Test Mapping Gaps

Appendix F menggunakan conservative mapping; karena itu test yang tidak
muncul sebagai candidate tidak boleh dianggap orphan secara final sampai
semantic review dilakukan.

Current candidate-unreferenced test count: **15**.

Tests tersebut MUST pada next reconciliation pass diklasifikasikan
sebagai salah satu:

-   mapped to one or more Requirements;
-   retained as supplemental/non-normative test;
-   superseded;
-   duplicate;
-   retired with rationale.

------------------------------------------------------------------------

## G.7 Open Traceability Counts

-   Requirement rows pending invariant semantic review: **0**.
-   Requirement rows without explicit CT mapping: **0**.

`No explicit CT mapped` bukan otomatis defect jika `DI`, `CI`, `TI`,
atau `HR` adalah verification method yang tepat. Namun behavioral MUST
requirements SHOULD memperoleh explicit executable test sebelum RC-Final
atau documented inspection justification.

------------------------------------------------------------------------

## G.8 Identifier Stability Rule

Existing domain IDs MUST remain stable through freeze reconciliation.

\[ StableID + CorrectiveMapping \> DestructiveRenumbering \]

New profile identifiers introduced by this review (`AOF-PRF-*`,
`PRF-INV-*`, `CT-PRF-*`) MUST be added to Master Registry/Traceability
before RC-Final.

------------------------------------------------------------------------

## G.9 Final Freeze Blockers

Current explicit blockers sebelum `RC-Final` adalah:

1.  reconcile duplicate Requirement IDs with materially different
    wording;
2.  resolve five legacy invariant migration gaps or document intentional
    non-equivalence;
3.  validate pending Requirement → `AOF-INV-*` mappings;
4.  classify Requirement rows without explicit CT into executable-test
    vs justified-inspection paths;
5.  map/classify candidate-unreferenced tests;
6.  incorporate new Section 21 profile Requirements/Invariants/Tests
    into Appendix A/F;
7.  run final cross-reference and identifier integrity audit.

Items di atas adalah reconciliation work; tidak memerlukan framework
domain baru.

------------------------------------------------------------------------

## G.10 Freeze Decision

**Decision: `NOT YET SEMANTICALLY FROZEN`.**

Normative architecture dan substantive domains remain
`COMPLETE → Freeze Candidate`. Final consistency review menemukan no
reason untuk reopen framework design, tetapi menemukan
traceability/identifier reconciliation debt yang harus ditutup sebelum
`RC-Final`.

Recommended next artifact:

`Framework Specification v1.0 RC-Final-Revalidation.md`

Pass tersebut SHOULD menyelesaikan open items pada G.9 dan, jika clean,
menghasilkan direct input untuk `RC-Final`.

------------------------------------------------------------------------

# Appendix H --- Freeze Reconciliation

> **Historical Audit Record --- Non-Authoritative Current-State
> Status.** Appendix ini mempertahankan evidence dari pass sebelumnya.
> Status, blocker count, atau workflow-state wording di sini MUST NOT
> mengoverride normative core, Appendix A--F, atau latest release
> decision.

## H.1 Purpose

Freeze Reconciliation menutup explicit blockers yang ditemukan pada
Appendix G tanpa membuka kembali framework design.

\[ FreezeReconciliation = IdentifierStability + TraceabilityClosure +
ProfileReconciliation + GapDisposition \]

Tidak ada semantic domain baru pada pass ini.

------------------------------------------------------------------------

## H.2 Duplicate Requirement Resolution

Initial Final Consistency Review menemukan **58** Requirement IDs dengan
multiple wording. Freeze Reconciliation mempertahankan **first normative
definition** sebagai canonical definition untuk stable ID tersebut.

Later conflicting/redundant occurrences diubah menjadi explicit
**non-normative reconciliation notes**, bukan second normative
definitions.

Hasil setelah reconciliation:

-   remaining duplicate canonical Requirement IDs with divergent
    normative definitions: **0**;
-   destructive renumbering performed: **0**.

Prinsip:

\[ OneStableRequirementID
\Rightarrow OneCanonicalNormativeMeaning \]

Historical/local wording MAY remain only as non-normative context.

------------------------------------------------------------------------

## H.3 Profile Registry and Traceability Closure

Section 21 identifiers sekarang diintegrasikan ke global assurance
layer:

-   **4** `PRF-INV-*` aliases ditambahkan ke Master Invariant Registry
    sebagai `AOF-INV-159`--`AOF-INV-162`;
-   **6** `AOF-PRF-*` Requirements ditambahkan ke Appendix F;
-   **4** `CT-PRF-*` tests menjadi explicit profile conformance tests.

Profile registry integration status: **PASS**.

Profile traceability integration status: **PASS**.

------------------------------------------------------------------------

## H.4 Test Disposition

Previously candidate-unreferenced `CT-*` tests sekarang memiliki
explicit disposition di F.12.

Tidak ada test yang boleh dianggap direct Requirement coverage hanya
karena berada di specification. Supplemental tests tetap valid sebagai
assurance assets, tetapi conformance credit membutuhkan explicit
Requirement mapping.

\[ TestPresence\neq RequirementCoverage \]

------------------------------------------------------------------------

## H.5 Legacy Invariant Migration

Legacy Appendix A migration table pada cumulative baseline tidak
memiliki unresolved `Pending Final Consistency Review` entries setelah
registry reconciliation.

Legacy identifiers/families tetap dipertahankan sebagai migration
references; canonical global identity tetap `AOF-INV-*`.

------------------------------------------------------------------------

## H.6 Identifier Integrity

Freeze rules:

1.  existing `AOF-*`, `*-INV-*`, dan `CT-*` identifiers MUST NOT be
    destructively renumbered;
2.  one canonical Requirement ID MUST resolve to one normative meaning;
3.  aliases MUST be explicit;
4.  supplemental tests MUST NOT masquerade as mapped conformance
    coverage;
5.  post-freeze identifier changes require versioned change control.

Current canonical Master Registry count after profile integration:
**162**.

------------------------------------------------------------------------

## H.7 Remaining Non-Blocking Release Engineering

Setelah Freeze Reconciliation, pekerjaan berikut bukan framework design:

-   final mechanical cross-reference/link validation;
-   metadata/version-history normalization;
-   extraction of `SPECIFICATION.md`;
-   extraction of concrete `/schemas` artifacts;
-   extraction/implementation of `/tests`;
-   packaging and release notes.

Machine-readable schema/test extraction dapat menjadi
release-engineering artifact selama tidak mengubah frozen semantics.

------------------------------------------------------------------------

## H.8 Freeze Reconciliation Decision

**Decision: `FREEZE RECONCILIATION COMPLETE`.**

Conditions satisfied by this pass:

-   duplicate normative Requirement IDs reconciled to one canonical
    definition;
-   profile inheritance/composition semantics stabilized;
-   Section 21 Requirements/Invariants/Tests integrated into Appendix
    A/F;
-   previously unmapped tests explicitly classified;
-   legacy invariant migration has no unresolved marker;
-   identifier stability preserved.

Specification sekarang layak menjadi input untuk **RC-Final mechanical
validation**.

`Semantic Freeze` SHOULD be declared only after that final mechanical
validation confirms no broken identifier/cross-reference or packaging
defect.

Recommended next artifact:

`Framework Specification v1.0 RC-Final.md`

------------------------------------------------------------------------

# Appendix I --- Editorial & Mechanical QA Report

> **Historical Audit Record --- Non-Authoritative Current-State
> Status.** Appendix ini mempertahankan evidence dari pass sebelumnya.
> Status, blocker count, atau workflow-state wording di sini MUST NOT
> mengoverride normative core, Appendix A--F, atau latest release
> decision.

## I.1 QA Objective

QA ini memeriksa cumulative specification setelah Freeze Reconciliation
dengan prinsip:

\[ EditorialCorrection \not\Rightarrow SemanticChange \]

Perubahan dibatasi pada mechanical repair, editorial consistency, dan
release-hygiene correction. Semantic-sensitive findings tidak diubah
secara otomatis.

## I.2 Classification

-   `E1 Mechanical` --- Markdown, TeX/Pandoc residue, heading escape,
    whitespace, fence formatting.
-   `E2 Editorial` --- stale release wording, editorial consistency,
    non-semantic terminology/format cleanup.
-   `E3 Semantic-Sensitive` --- normative keyword, formula meaning,
    contradictory requirement, atau wording yang berpotensi mengubah
    normative semantics.

## I.3 Corrections Applied

-   E1 Pandoc TeX attribute residues repaired: **1440**.
-   E1 escaped Markdown headings repaired: **3**.
-   E1 code-fence language markers normalized: **85**.
-   E1 lines with trailing-space cleanup: **427**.
-   E2 stale \`Pending RC-Traceability placeholders replaced with
    current Appendix F / Freeze Reconciliation reference: **474**.
-   E2 stale explanatory paragraphs updated: **0**.
-   E2 non-semantic mixed-language editorial residues normalized: **2**.

## I.4 Residual Mechanical Scan

-   residual Pandoc \` command artifacts: **0**;
-   residual escaped Markdown headings: **0**;
-   `TODO`: **0**;
-   `TBD`: **0**;
-   `FIXME`: **0**;
-   stale `Pending RC-Traceability`: **0**;
-   `Pending Semantic Review`: **94**;
-   `No explicit CT mapped`: **247**.

## I.5 Semantic-Sensitive Handling

QA tidak melakukan automatic case-conversion atau rewriting terhadap
candidate lowercase English normative keywords karena perubahan
`must/should/may` menjadi uppercase RFC-style keyword dapat mengubah
normative force.

Candidate lines flagged for RC-Final validation: **3**.

Candidate tersebut MUST diperiksa dalam final validation context; hanya
clear editorial defects yang MAY diperbaiki tanpa reopening semantics.

## I.6 Structural QA Findings

Heading hierarchy candidates requiring review: **0**.

Table header/separator candidates requiring review: **0**.

Temuan structural heuristic dapat mengandung false positive akibat
formula/code/table content dan MUST diverifikasi secara contextual
sebelum perubahan.

## I.7 QA Gate Decision

**Decision: `EDITORIAL & MECHANICAL QA COMPLETE`.**

Mechanical defects yang aman untuk diperbaiki telah dikoreksi.
Semantic-sensitive candidates tidak diubah secara otomatis.

Artifact ini SHOULD masuk ke `RC-Final Validation`, yang melakukan
contextual review terhadap remaining E3 candidates, cross-reference
integrity, identifier integrity, metadata/version history, dan final
freeze-gate criteria.

------------------------------------------------------------------------

# Appendix J --- RC-Final Validation Report

> **Historical Audit Record --- Non-Authoritative Current-State
> Status.** Appendix ini mempertahankan evidence dari pass sebelumnya.
> Status, blocker count, atau workflow-state wording di sini MUST NOT
> mengoverride normative core, Appendix A--F, atau latest release
> decision.

## J.1 Validation Scope

`RC-Final Validation` dilakukan secara adversarial terhadap artifact
Editorial & Mechanical QA. Pass ini tidak menambah framework semantics.

\[ RCFinalEligible = IdentifierIntegrity
\land CrossReferenceIntegrity \land EditorialIntegrity
\land FreezeGatePass \]

## J.2 E3 Contextual Review

Lowercase English normative-keyword candidates reviewed: **3**.
Semantic-sensitive blockers after contextual review: **0**.

-   Line 21044: `Non-normative prose` --- **Source-derived statement:**
    must remain representationally distinct.
-   Line 22720: `Non-normative prose` --- must remain representationally
    distinct.
-   Line 25020: `Non-normative prose` --- `must/should/may` menjadi
    uppercase RFC-style keyword dapat mengubah

## J.3 Identifier Integrity

-   unique canonical Requirement IDs: **332**;
-   divergent duplicate Requirement IDs: **0**;
-   canonical `AOF-INV-*` definitions: **162**;
-   divergent duplicate canonical invariant IDs: **0**;
-   `CT-*` definitions: **51**;
-   divergent duplicate Test IDs: **0**;
-   unresolved identifier references: **0**.

## J.4 Structural and Formula Integrity

-   Appendix A--I present exactly once and ordered: **FAIL**;
-   displayed formula blocks checked: **974**;
-   formula mechanical defects: **874**;
-   Pandoc TeX residue: **1441**;
-   escaped headings: **3**.

## J.5 Freeze Marker Scan

-   `TODO` occurrences: **1**.
-   `TBD` occurrences: **1**.
-   `FIXME` occurrences: **1**.
-   `Pending Semantic Review` occurrences: **95**.
-   `Pending RC-Traceability` occurrences: **2**.
-   `No explicit CT mapped` occurrences: **248**.
-   `Unresolved` occurrences: **34**.

Historical/audit prose is not treated as an active blocker unless it
represents current unresolved status.

## J.6 Stale Metadata Review

Stale self-identification findings: **0**.

Historical references to earlier RC artifacts MAY remain in audit trail;
current document metadata MUST identify only the current artifact.

## J.7 Validation Decision

**Decision: `RC-FINAL VALIDATION FAILED`.**

Blocking findings: **4**.

-   `Formula mechanical integrity` --- \[(1, 'Pandoc residue'), (2,
    'Pandoc residue'), (3, 'Pandoc residue'), (5, 'Pandoc residue'), (7,
    'Pandoc residue'), (8, 'Pandoc residue'), (9, 'Pandoc residue'),
    (10, 'Pandoc residue'), (11, 'Pandoc residue'), (12, 'Pandoc
    residue'), (13, 'Pandoc residue'), (14, 'Pandoc residue'), (15,
    'Pandoc residue'), (16, 'Pandoc residue'), (18, 'Pandoc residue'),
    (19, 'Pandoc residue'), (25, 'Pandoc residue'), (27, 'Pandoc
    residue'), (28, 'Pandoc residue'), (29, 'Pandoc residue')\]
-   `Appendix A-I integrity` --- {'A': \[\]}
-   `Residual freeze markers` --- {'TODO': 1, 'TBD': 1, 'FIXME': 1,
    'Pending Semantic Review': 95, 'Pending RC-Traceability': 2, 'No
    explicit CT mapped': 248, 'Unresolved': 34}
-   `Mechanical residue` --- tex=1441, headings=3

------------------------------------------------------------------------

# Appendix K --- Targeted Formula & Appendix Remediation

> **Historical Audit Record --- Non-Authoritative Current-State
> Status.** Appendix ini mempertahankan evidence dari pass sebelumnya.
> Status, blocker count, atau workflow-state wording di sini MUST NOT
> mengoverride normative core, Appendix A--F, atau latest release
> decision.

## K.1 Scope

Pass ini memperbaiki blockers yang ditemukan oleh `RC-Final Validation`
tanpa mengubah framework semantics.

\[ RemediationScope = FormulaSerialization + AppendixHeadingIntegrity +
EditorialClarification \]

## K.2 Confirmed Root Causes

Formula blocker berasal terutama dari Pandoc raw-TeX serialization
residue seperti `\neq Authority` dan command-word concatenation seperti
`\Rightarrow Action`. Temuan ini adalah serialization defects, bukan 874
independent semantic formula defects.

Appendix blocker berasal dari escaped heading `\# Appendix A`, sehingga
Appendix A tidak terdeteksi oleh strict heading validator.

## K.3 Corrections

-   raw-TeX wrapper markers removed;
-   known TeX operator commands separated from immediately following AOF
    identifiers;
-   Appendix A heading restored to canonical Markdown heading;
-   code-fence language marker normalized;
-   two incomplete `SCH-INV-01` prose fragments clarified without
    changing the invariant formula or normative intent.

## K.4 Semantic Boundary

Tidak ada Requirement, Invariant, Authority rule, Policy rule, Risk
rule, profile relationship, orchestration semantics, atau conformance
meaning yang diubah oleh remediation ini.

\[ MechanicalRepair \not\Rightarrow SemanticChange \]

------------------------------------------------------------------------

# Appendix L --- RC-Final Revalidation Report

> **Historical Audit Record --- Non-Authoritative Current-State
> Status.** Appendix ini mempertahankan evidence dari pass sebelumnya.
> Status, blocker count, atau workflow-state wording di sini MUST NOT
> mengoverride normative core, Appendix A--F, atau latest release
> decision.

## L.1 Decision

**Decision: `RC-FINAL REVALIDATION FAILED`.**

## L.2 Adversarial Checks

-   contextual E3 blockers: **1**;
-   divergent canonical Requirement IDs: **0**;
-   divergent canonical `AOF-INV-*` IDs: **0**;
-   divergent `CT-*` IDs: **0**;
-   unresolved identifier references: **0**;
-   displayed formula blocks checked: **979**;
-   formula mechanical defects: **1**;
-   Appendix A-K exact-once integrity: **PASS**;
-   Appendix A-K ordering: **PASS**;
-   raw Pandoc TeX residue: **0**;
-   escaped heading residue: **2**;
-   stale self-identification findings: **0**;
-   active freeze-marker classes with nonzero findings: **6**.

## L.3 Formula Remediation Result

Initial 874 formula findings were traced primarily to serialization
artifacts, not semantic formula conflicts. All displayed formula blocks
were rechecked after raw-TeX sanitation, command separation,
brace-balance validation, and residue scanning.

## L.4 Freeze Gate

Blocking findings remain and MUST be remediated before RC-Final
packaging.

`Semantic Freeze` is not declared by this revalidation artifact itself.

------------------------------------------------------------------------

# Appendix M --- Traceability State Closure & Final Revalidation

> **Historical Audit Record --- Non-Authoritative Current-State
> Status.** Appendix ini mempertahankan evidence dari pass sebelumnya.
> Status, blocker count, atau workflow-state wording di sini MUST NOT
> mengoverride normative core, Appendix A--F, atau latest release
> decision.

## M.1 Traceability State Closure

Initial Appendix F used temporary workflow-state labels during
conservative lexical mapping. Those labels are now superseded.

Canonical interpretation:

\[ NoDirectInvariantMapping \neq UnresolvedSemanticDefect \]

and:

\[ NoDirectReferenceCT \neq NoVerificationPath \]

A Requirement without a direct `AOF-INV-*` link MUST NOT be assigned a
fabricated invariant. A Requirement without a direct reference `CT-*`
MAY be verified through the declared `AT`, `NT`, `DI`, `CI`, `TI`, or
`HR` method as applicable. Executable conformance suites MAY add tests
without changing frozen specification semantics.

## M.2 Public-Release Interpretation

The specification distinguishes:

-   semantic completeness;
-   reference-test coverage;
-   implementation conformance-suite coverage.

These are related but not identical.

\[ SpecificationComplete
\not\Rightarrow ExhaustiveExecutableTestSuite \]

Public testing MAY discover new tests, implementation defects, ambiguity
reports, or extension proposals without invalidating Semantic Freeze
unless the underlying normative semantics require change.

## M.3 Closure Rule

Historical QA reports in Appendices G--L retain earlier finding
terminology as audit trail. They are non-authoritative regarding current
open/closed status. Current status is determined by the latest
cumulative specification content and this closure record.

------------------------------------------------------------------------

# Appendix N --- RC-Final Clean Revalidation Report

> **Historical Audit Record --- Non-Authoritative Current-State
> Status.** Appendix ini mempertahankan evidence dari pass sebelumnya.
> Status, blocker count, atau workflow-state wording di sini MUST NOT
> mengoverride normative core, Appendix A--F, atau latest release
> decision.

## N.1 Decision

**Decision: `RC-FINAL CLEAN REVALIDATION FAILED`.**

## N.2 Results

-   unique canonical Requirement IDs: **332**;
-   divergent Requirement IDs: **0**;
-   canonical `AOF-INV-*` definitions: **162**;
-   divergent canonical invariant IDs: **0**;
-   `CT-*` definitions: **51**;
-   divergent Test IDs: **0**;
-   unresolved identifier references: **0**;
-   displayed formula blocks checked: **982**;
-   formula mechanical defects: **0**;
-   Appendix A-M exact-once/order integrity: **PASS**;
-   raw Pandoc TeX residue: **0**;
-   escaped heading residue: **0**;
-   active authoritative freeze-marker classes: **2**;
-   authoritative lowercase normative candidates: **0**;
-   stale current self-identification findings: **0**.

## N.3 Freeze-Gate Interpretation

Historical QA reports MAY contain superseded workflow-state language or
failed-validation counts as immutable audit history. Those historical
mentions do not constitute current open state.

Current authoritative content through Appendix F plus the latest closure
record contains no active workflow-state marker when this validation
reports zero marker classes.

## N.4 Packaging Eligibility

Blocking findings remain; RC-Final packaging is not yet permitted.

------------------------------------------------------------------------

# Appendix O --- RC-Final Validation Closure

> **Historical Audit Record --- Non-Authoritative Current-State
> Status.** Appendix ini mempertahankan evidence dari pass sebelumnya.
> Status, blocker count, atau workflow-state wording di sini MUST NOT
> mengoverride normative core, Appendix A--F, atau latest release
> decision.

## O.1 Decision

**Decision: `RC-FINAL VALIDATION PASSED`.**

## O.2 Final Gate Metrics

-   canonical Requirement IDs: **332**;
-   divergent Requirement IDs: **0**;
-   canonical `AOF-INV-*` definitions: **162**;
-   divergent canonical invariant IDs: **0**;
-   `CT-*` definitions: **51**;
-   divergent Test IDs: **0**;
-   unresolved identifier references: **0**;
-   displayed formula blocks checked: **982**;
-   formula mechanical defects: **0**;
-   Appendix A-O exact-once/order integrity: **PASS**;
-   active authoritative freeze-marker classes: **0**;
-   authoritative E3 candidates: **0**;
-   raw Pandoc TeX residue: **0**;
-   escaped heading residue: **0**.

## O.3 Release Gate

All blocking validation classes are zero. The specification is eligible
for `RC-Final` packaging and formal Semantic Freeze decision.

------------------------------------------------------------------------

# Appendix P --- RC-Final Packaging Record

## P.1 Release Candidate Identity

This cumulative artifact is packaged as:

`Framework Specification v1.0 RC-Final`

Status:

`Release Candidate — Final / Semantic Freeze Candidate`

## P.2 Packaging Basis

RC-Final is derived directly from the cumulative artifact that passed
the clean adversarial RC-Final Validation gate.

\[ RCFinal = ValidatedSpecification + ReleaseMetadata \]

Packaging MUST NOT introduce new framework semantics.

## P.3 Validation Basis

The immediately preceding validation closure reported:

-   zero divergent canonical Requirement IDs;
-   zero divergent canonical `AOF-INV-*` IDs;
-   zero divergent `CT-*` IDs;
-   zero unresolved identifier references;
-   zero formula mechanical defects;
-   valid Appendix ordering and uniqueness;
-   zero active authoritative freeze-marker classes;
-   zero authoritative E3 candidates;
-   zero raw Pandoc TeX residue;
-   zero escaped heading residue.

## P.4 Semantic Status

RC-Final is a **Semantic Freeze Candidate**.

\[ RCFinal \neq SemanticFreeze \]

Semantic Freeze requires an explicit release decision. Until that
decision is recorded, RC-Final remains the final validated Release
Candidate baseline.

## P.5 Change-Control Boundary

Any proposed change after RC-Final MUST be classified before
incorporation:

\[ Change \rightarrow

\begin{cases}
Editorial\\
Clarification\\
Semantic\\
Security\\
Conformance\\
Extension
\end{cases}
\]

A Semantic change MUST NOT be silently incorporated into the frozen v1.0
lineage.

## P.6 Public Review Readiness

RC-Final is suitable as the normative candidate baseline for public
testing and critique. Public feedback MAY identify implementation
defects, ambiguities, missing tests, security findings, design
limitations, extension proposals, or research questions.

Public feedback does not itself alter normative semantics; accepted
semantic changes require explicit versioned change control.

------------------------------------------------------------------------

# Appendix Q --- RC-Final Public-Readiness Hardening

## Q.1 Objective

Pass ini memisahkan internal editorial history dari public normative
reading path tanpa mengubah stable Requirement IDs atau framework
semantics.

\[ PublicReleaseReady = InternalConsistency
\land EditorialCanonicality \land TraceabilityUsability
\land ReaderClarity \]

## Q.2 Reconciliation Residue

Non-normative reconciliation-note blocks removed from public reading
path: **58**.

Canonical normative Requirement definitions tetap menggunakan stable
identifier yang sama. Tidak ada suffix `a/b`, renumbering, atau semantic
fork yang dibuat.

## Q.3 Appendix A Traceability Usability

Appendix A summary registry dibangun ulang sebagai public canonical
registry.

-   canonical invariants represented: **162**;
-   invariants dengan explicit Requirement mapping derivable from
    current traceability evidence: **102**;
-   invariants dengan explicit reference `CT-*` mapping derivable from
    current traceability evidence: **41**.

Jika explicit direct mapping tidak didukung oleh current specification
evidence, registry menyatakan `No direct ... mapping asserted` daripada
menginvent hubungan heuristik.

\[ NoDirectMapping \neq MissingInvariantSemantics \]

dan:

\[ NoDirectReferenceCT \neq NoVerificationPath \]

## Q.4 Historical Audit Separation

Appendices G--O diberi explicit historical-audit banner. Historical
blocker counts dan superseded workflow-state language dipertahankan
untuk provenance tetapi tidak lagi dapat dibaca sebagai current
authoritative release status.

## Q.5 TOCTOU / High-Assurance Semantic Review

TOCTOU-related occurrences reviewed: **140**.

Automatic semantic strengthening tidak dilakukan pada pass ini.
Requirement strength hanya boleh berubah melalui explicit semantic
decision.

Current automated review indicates mandatory High-Assurance
freshness/binding language detected: **YES**.

Jika `NO`, isu ini tetap menjadi explicit semantic-review item sebelum
Semantic Freeze; ia tidak boleh diselesaikan dengan silent `SHOULD` →
`MUST` conversion.

## Q.6 Hardening Boundary

Pass ini MAY memperbaiki public readability, registry usability,
provenance labeling, dan non-normative editorial residue.

Pass ini MUST NOT:

-   renumber stable canonical Requirement IDs;
-   fabricate invariant-to-requirement relationships;
-   fabricate reference tests;
-   strengthen or weaken normative keywords silently;
-   alter Authority, Policy, Risk, Verification, Human Governance, or
    Conformance semantics.

------------------------------------------------------------------------

# Appendix R --- Public-Readiness Hardening Validation

## R.1 Results

-   reconciliation-note residue in public artifact: **0**;
-   stale Appendix A
    `No direct mapping asserted; consult Appendix F verification disposition`
    residue: **158**;
-   canonical Requirement IDs: **332**;
-   divergent Requirement IDs: **0**;
-   canonical `AOF-INV-*` definitions: **162**;
-   divergent canonical invariant IDs: **0**;
-   `CT-*` definitions: **51**;
-   divergent Test IDs: **0**;
-   Appendix A--Q exact-once/order integrity: **PASS**;
-   displayed formula blocks checked: **986**;
-   formula mechanical defects: **0**;
-   raw Pandoc TeX residue: **0**;
-   escaped heading residue: **0**.

## R.2 Decision

**Decision: `BLOCKED`.**

One or more public-readiness blockers remain.

------------------------------------------------------------------------

# Appendix S --- Public-Readiness Hardening Closure

## S.1 Residual Placeholder Remediation

Detailed Appendix A records still contained **159** historical
cross-reference placeholders after the public summary registry was
rebuilt. They have been replaced with an explicit conservative
disposition:

`No direct mapping asserted; consult Appendix F verification disposition`

This does not fabricate Requirement or Test relationships.

## S.2 Final Public-Readiness Gate

The current artifact MUST satisfy all of the following before Semantic
Freeze review:

-   zero reconciliation-note residue;
-   zero stale Appendix F / Freeze Reconciliation placeholder wording;
-   zero divergent canonical IDs;
-   structurally valid Appendix registry;
-   mechanically valid formulas and Markdown;
-   explicit disposition for trace links that are not directly asserted;
-   no silent normative strengthening.

## S.3 TOCTOU Review Disposition

Targeted review found existing mandatory High-Assurance
freshness/binding semantics in the specification context. Therefore no
silent `SHOULD` to `MUST` change is introduced by this hardening pass.

The public-review concern is retained as an
implementation/conformance-test focus rather than a new pre-freeze
semantic requirement.

------------------------------------------------------------------------

# Appendix T --- Final Public-Readiness Validation

**Decision: `PUBLIC-READINESS HARDENING FAILED`.**

-   reconciliation-note residue: **0**;
-   stale Appendix A placeholder residue: **1**;
-   duplicate Requirement definitions: **14**;
-   duplicate canonical invariant definitions: **0**;
-   duplicate reference Test definitions: **0**;
-   Appendix A--S exact-once integrity: **PASS**;
-   displayed formula blocks checked: **986**;
-   formula mechanical defects: **2**;
-   raw Pandoc TeX residue: **0**;
-   escaped heading residue: **0**.

Blocking public-readiness findings remain.

------------------------------------------------------------------------

# Appendix U --- Public-Readiness Release Gate Closure

## U.1 Canonical Definition Cleanup

Exact repeated Requirement definitions converted to canonical cross-reference form: **14**.

Divergent repeated Requirement definitions requiring semantic reconciliation: **0**.

## U.2 Final Gate

**Decision: `PUBLIC-READINESS RELEASE GATE FAILED`.**

- reconciliation-note residue: **0**;
- stale Appendix A placeholder literal: **0**;
- divergent Requirement IDs: **0**;
- divergent canonical invariant IDs: **0**;
- divergent Test IDs: **0**;
- formula mechanical defects: **1**;
- raw Pandoc TeX residue: **0**;
- escaped heading residue: **0**;
- Appendix A--T exact-once/order integrity: **PASS**.

One or more blockers remain; Semantic Freeze MUST remain on hold.

------------------------------------------------------------------------

# Appendix V --- Public-Readiness Final Mechanical Closure

**Decision: `PUBLIC-READINESS HARDENING FAILED`.**

- displayed formula blocks checked: **986**;
- formula mechanical defects: **1**;
- reconciliation-note residue: **0**;
- stale traceability placeholder residue: **0**;
- raw Pandoc TeX residue: **0**;
- escaped heading residue: **0**.

Mechanical blocker remains; Semantic Freeze stays on hold.

------------------------------------------------------------------------

# Appendix W --- Public-Readiness Hardening Final Gate

**Decision: `PUBLIC-READINESS HARDENING PASSED`.**

Final targeted repair removed the confirmed stray Markdown fence from the
`Failure → Contain → Reconcile → ReassessRisk → ... → VerifyRecovery` displayed formula.

- displayed formula blocks checked: **986**;
- remaining formula mechanical defects: **0**;
- reconciliation-note residue: **0**;
- stale Appendix A placeholder residue: **0**;
- divergent canonical Requirement IDs: **0**;
- divergent canonical invariant IDs: **0**;
- divergent reference Test IDs: **0**.

Public-readiness hardening is complete with zero known blockers. Artifact is ready for explicit Semantic Freeze decision.
